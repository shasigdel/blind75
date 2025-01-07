# Two Pointers
def maxProfit(prices):
    left, right = 0, 1
    maxP = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(profit, maxP)
        else:
            left = right
        
        right+=1 
    
    return maxP
    
    
if __name__ == "__main__":
    # Test case
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Test case 1 - Expected: 5, Got: {maxProfit(prices)}")
    
    prices = [7, 6, 4, 3, 1]
    print(f"Test case 2 - Expected: 0, Got: {maxProfit(prices)}")