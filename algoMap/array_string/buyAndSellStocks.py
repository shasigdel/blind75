from typing import List


class Solution:
    def bestTimeToBuyAndSellStocks(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxProfit = 0
        
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
            j+=1
        
        return maxProfit