from epicsrec.tests import *

class TestChooseController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='choose', action='index'))
        # Test response...
