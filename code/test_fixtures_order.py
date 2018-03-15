import inspect
import unittest


class DemoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # I am called once before **any** test runs.
        method_name = inspect.stack()[0][3]
        cls.log_class_point(cls.__name__, method_name)
    
    @classmethod
    def tearDownClass(cls):
        # I am called once and am the last method to execute.
        # **I only execute if setUpClass was successful.**
        method_name = inspect.stack()[0][3]
        cls.log_class_point(cls.__name__, method_name)
    
    def setUp(self):
        # I am called before the execution of each test method.
        self.log_method()

    def tearDown(self):
        # I am called after the execution of each test method.
        self.log_method()
    
    def test_a_thing(self):
        # I am a test method
        self.log_method()
    
    def test_another_thing(self):
        # I am another test method
        self.log_method()
    
    @classmethod
    def log_class_point(cls, class_name, method_name):
        print('{class_name} - {method_name}'.format(
            class_name=class_name, method_name=method_name))
    
    def log_method(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('{0} - {1}'.format(
            self.__class__.__name__, callingFunction))


if __name__ == '__main__':
    unittest.main()