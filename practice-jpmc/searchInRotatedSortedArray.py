from typing import List


def rotatedSortedArray(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        
        #left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        #right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l= mid + 1
                
    return -1
    
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    
    result = rotatedSortedArray(nums, target);
    
    print(result)