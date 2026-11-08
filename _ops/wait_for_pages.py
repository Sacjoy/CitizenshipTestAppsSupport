"""Wait for GitHub's built-in Pages deployment of the current workflow commit."""
import json
import os
import sys
import time
from urllib.request import Request, urlopen


def deployment_state(runs, sha):
    matches = [run for run in runs if run['name'] == 'pages build and deployment' and run['head_sha'] == sha]
    if not matches:
        return 'pending'
    latest = max(matches, key=lambda run: run['id'])
    return latest['conclusion'] if latest['status'] == 'completed' else 'pending'


def main():
    repo, sha = os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_SHA']
    url = f'https://api.github.com/repos/{repo}/actions/runs?head_sha={sha}&per_page=100'
    headers = {'Accept':'application/vnd.github+json', 'User-Agent':'MentionRise-ReadinessCheck/1.0'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer '+os.environ['GH_TOKEN']
    for attempt in range(20):
        # Transport/API errors fail this job; never report an unverified deploy as success.
        with urlopen(Request(url, headers=headers), timeout=20) as response:
            state = deployment_state(json.load(response)['workflow_runs'], sha)
        print(f'Pages deployment {sha[:12]}: {state}', flush=True)
        if state == 'success':
            return 0
        if state != 'pending':
            return 1
        if attempt < 19:
            time.sleep(15)
    print('Timed out waiting for Pages deployment', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
