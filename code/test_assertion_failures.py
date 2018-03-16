import unittest


class TestAssertions(unittest.TestCase):

    def test_assert_equal_failure(self):
        self.assertEqual(1, 2)
    
    def test_assert_true(self):
        # This is essentially the same as the standard 'assert' keyword
        self.assertTrue(False)
    
    def test_assert_is_none(self):
        self.assertIsNone(1)
    
    def test_assert_in(self):
        self.assertIn(0, [1, 2, 3, 4, 5])
    
    def test_assert_raises(self):
        with self.assertRaises(TypeError):
            pass
    
    def test_fail(self):
        # Not an assertion, but an interesting example to show
        self.fail('Because I asked the code to fail.')

