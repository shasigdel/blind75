import unittest
from longesCommonPrefix import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(self.solution.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(self.solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]), "inters")
        self.assertEqual(self.solution.longestCommonPrefix(["throne", "throne"]), "throne")
        self.assertEqual(self.solution.longestCommonPrefix(["throne", "dungeon"]), "")
        self.assertEqual(self.solution.longestCommonPrefix(["throne", "throne", "throne"]), "throne")
        self.assertEqual(self.solution.longestCommonPrefix(["", ""]), "")
        self.assertEqual(self.solution.longestCommonPrefix(["a"]), "a")
        self.assertEqual(self.solution.longestCommonPrefix(["ab", "a"]), "a")

if __name__ == '__main__':
    unittest.main()