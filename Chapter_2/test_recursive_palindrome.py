from unittest import TestCase
import recursive_palindrome

class Test(TestCase):
    def test_is_palindrome(self):
        p_input = 'ewe'
        self.assertTrue(recursive_palindrome.is_palindrome(p_input))
        self.assertFalse(recursive_palindrome.is_palindrome('ewok'))
