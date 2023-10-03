import unittest

from palindrome_checker.palindrome import check_maximum_palindromes_length

class PalindromeCheckerTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(check_maximum_palindromes_length(""), "")

    def test_simple_cases(self):
        self.assertEqual(check_maximum_palindromes_length("a"), "a")
        self.assertEqual(check_maximum_palindromes_length("abc"), "a")

    def test_usecase_0(self):
        self.assertEqual(check_maximum_palindromes_length("aba"), "aba")
        self.assertEqual(check_maximum_palindromes_length("kayak"), "kayak")
    
    def test_usecase_1(self):
        self.assertEqual(check_maximum_palindromes_length("aa"), "aa")
    
    def test_usecase_2(self):
        self.assertEqual(check_maximum_palindromes_length("hiertyuuytreih"), "hiertyuuytreih")
        self.assertEqual(check_maximum_palindromes_length("hiertyujuytreih"), "hiertyujuytreih")
        self.assertEqual(check_maximum_palindromes_length("aaabbvbbfff"), "bbvbb")
        self.assertEqual(check_maximum_palindromes_length("aaabaanabaaa"), "aabaa")
        self.assertEqual(check_maximum_palindromes_length("aaaaaaa"), "aaaaaaa")

if __name__ is "__main__":
    unittest.main()