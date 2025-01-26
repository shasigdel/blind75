import unittest
from isSubsequence import Solution

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_subsequence(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))
        self.assertFalse(self.solution.isSubsequence("abc", "ab"))

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", ""))
        self.assertTrue(self.solution.isSubsequence("", "a"))

    def test_empty_t(self):
        self.assertFalse(self.solution.isSubsequence("a", ""))
        self.assertFalse(self.solution.isSubsequence("abc", ""))

if __name__ == '__main__':
    unittest.main()