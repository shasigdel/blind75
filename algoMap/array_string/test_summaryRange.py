import unittest
from summaryRange import Solution

class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_summaryRanges(self):
        test_cases = [
            ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
            ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
            ([], []),
            ([-1], ["-1"]),
            ([0], ["0"]),
            ([1, 3, 5, 7], ["1", "3", "5", "7"]),
            ([1, 2, 3, 4, 5], ["1->5"])
        ]

        for nums, expected in test_cases:
            actual = self.solution.summaryRanges(nums)
            print(f"Input: {nums}\nExpected: {expected}\nActual: {actual}\n")
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()