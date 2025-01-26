import unittest
from findClosestNumberToZero import Solution  # Import your implementation

class TestFindClosestNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [-4, -2, 1, 4, 8, 0]
        self.assertEqual(self.solution.findClosestNumber(nums), 0)

    def test_positive_numbers(self):
        nums = [2, 3, 4, 5]
        self.assertEqual(self.solution.findClosestNumber(nums), 2)

    def test_negative_numbers(self):
        nums = [-4, -3, -2, -1]
        self.assertEqual(self.solution.findClosestNumber(nums), -1)

    def test_tie_positive_and_negative(self):
        nums = [-2, 2, -3, 3]
        self.assertEqual(self.solution.findClosestNumber(nums), 2)

    def test_single_positive_element(self):
        nums = [42]
        self.assertEqual(self.solution.findClosestNumber(nums), 42)

    def test_single_negative_element(self):
        nums = [-42]
        self.assertEqual(self.solution.findClosestNumber(nums), -42)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.solution.findClosestNumber(nums), 0)

    def test_large_positive_and_negative(self):
        nums = [-1000, 1000, -2000, 2000]
        self.assertEqual(self.solution.findClosestNumber(nums), 1000)

    def test_zero_and_negatives(self):
        nums = [0, -1, -2, -3]
        self.assertEqual(self.solution.findClosestNumber(nums), 0)

    def test_large_random_array(self):
        nums = [-10, 15, -20, 25, 30, -5]
        self.assertEqual(self.solution.findClosestNumber(nums), -5)

if __name__ == "__main__":
    unittest.main()
