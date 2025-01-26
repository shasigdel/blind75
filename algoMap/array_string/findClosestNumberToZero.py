from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
if __name__ == "__main__":
    solObj = Solution()
    
    arr = [-4,-2,1,4,8,0] 
    print(solObj.findClosestNumber(arr));
    
