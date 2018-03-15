import unittest

class DemoTest(unittest.BaseTestSuite):

    @classmethod
    def setUpClass(cls):
        # I am called once before **any** test runs.
        pass
    
    @classmethod
    def tearDownClass(cls):
        # I am called once and am the last method to execute.
        # **I only execute if setUpClass was successful.**
        pass
    
    def setUp(self):
        # I am called before the execution of each test method.
        pass

    def tearDown(self):
        # I am called after the execution of each test method.
        pass
    
    def test_a_thing(self):
        # I am a test method
        pass
    
    def test_another_thing(self):
        # I am another test method
        pass