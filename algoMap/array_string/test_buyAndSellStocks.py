import unittest
from buyAndSellStocks import Solution

class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        result = self.solution.bestTimeToBuyAndSellStocks(prices)
        print(f"Test case 1 - Expected: {expected}, Result: {result}")
        self.assertEqual(result, expected)

    def test_case_2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = self.solution.bestTimeToBuyAndSellStocks(prices)
        print(f"Test case 2 - Expected: {expected}, Result: {result}")
        self.assertEqual(result, expected)

    def test_case_3(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        result = self.solution.bestTimeToBuyAndSellStocks(prices)
        print(f"Test case 3 - Expected: {expected}, Result: {result}")
        self.assertEqual(result, expected)

    def test_case_4(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 4
        result = self.solution.bestTimeToBuyAndSellStocks(prices)
        print(f"Test case 4 - Expected: {expected}, Result: {result}")
        self.assertEqual(result, expected)

    def test_case_5(self):
        prices = [1]
        expected = 0
        result = self.solution.bestTimeToBuyAndSellStocks(prices)
        print(f"Test case 5 - Expected: {expected}, Result: {result}")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()