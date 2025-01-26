import unittest
from mergeAlternately import Solution

class TestMergeAlternately(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        word1 = "abc"
        word2 = "pqr"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "apbqcr")
        
    def test_case_2(self):
        word1 = "ab"
        word2 = "pqrs"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "apbqrs")
        
    def test_case_3(self):
        word1 = "abcd"
        word2 = "pq"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "apbqcd")
        
    def test_case_4(self):
        word1 = "a"
        word2 = "xyz"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "axyz")
        
    def test_case_5(self):
        word1 = "hello"
        word2 = "world"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "hweolrllod")
        
    def test_case_6(self):
        word1 = ""
        word2 = "abc"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "abc")
        
    def test_case_7(self):
        word1 = "abc"
        word2 = ""
        self.assertEqual(self.solution.mergeAlternately(word1, word2), "abc")

if __name__ == "__main__":
    unittest.main()