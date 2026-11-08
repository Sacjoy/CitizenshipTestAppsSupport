import unittest
from _ops.wait_for_pages import deployment_state


class DeploymentTests(unittest.TestCase):
    def test_waits_for_matching_pages_commit(self):
        self.assertEqual('pending', deployment_state([], 'abc'))
        self.assertEqual('pending', deployment_state([{'name':'Visibility readiness','head_sha':'abc','status':'completed','conclusion':'success','id':1}], 'abc'))
        self.assertEqual('pending', deployment_state([{'name':'pages build and deployment','head_sha':'old','status':'completed','conclusion':'success','id':1}], 'abc'))

    def test_returns_latest_matching_state(self):
        first = dict(name='pages build and deployment',head_sha='abc',id=1,status='completed',conclusion='success')
        self.assertEqual('success', deployment_state([first], 'abc'))
        latest = dict(first, id=2, status='in_progress', conclusion=None)
        self.assertEqual('pending', deployment_state([first, latest], 'abc'))
        self.assertEqual('failure', deployment_state([dict(first,conclusion='failure')], 'abc'))
