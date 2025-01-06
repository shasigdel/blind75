from typing import List


class Solution:
    def buyAndSell(self, nums:List[int]) -> int:
        l,r = 0, 1
        maxP = 0

        while r < len(nums):
            if nums[l] < nums[r]:
                diff = nums[r] - nums[l]
                maxP = max(maxP, diff)
            else:
                l = r
            r += 1    
        return maxP

if __name__== '__main__':
    nums = [7,1,5,3,6,4]
    
    obj = Solution()

    result = obj.buyAndSell(nums)
    print(result)