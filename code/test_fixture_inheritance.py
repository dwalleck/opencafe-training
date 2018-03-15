import inspect
import unittest


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        method_name = inspect.stack()[0][3]
        cls.log_class_point(
            cls.__bases__[0].__name__, method_name)

    @classmethod
    def tearDownClass(cls):
        cls.log_class_point(
            cls.__bases__[0].__name__, inspect.stack()[0][3])

    @classmethod
    def log_class_point(cls, class_name, method_name):
        print('{class_name} - {method_name}'.format(
            class_name=class_name, method_name=method_name))

class TestDemo(TestBase):

    @classmethod
    def setUpClass(cls):
        super(TestDemo, cls).setUpClass()
        method_name = inspect.stack()[0][3]
        cls.log_class_point(cls.__name__, method_name)

    @classmethod
    def tearDownClass(cls):
        super(TestDemo, cls).tearDownClass()
        method_name = inspect.stack()[0][3]
        cls.log_class_point(cls.__name__, method_name)
    
    def setUp(self):
        self.log_method()
    
    def tearDown(self):
        self.log_method()
    
    def test_first_thing(self):
        self.log_method()
    
    def test_second_thing(self):
        self.log_method()
    
    def log_method(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('{0} - {1}'.format(
            self.__class__.__name__, callingFunction))


if __name__ == '__main__':
    unittest.main()
