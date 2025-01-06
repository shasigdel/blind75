from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high, target, nums):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binary_search(low +1, high, target, nums)
            else:
                return binary_search(low, high-1, target, nums)
            
        return binary_search(0, len(nums) - 1, target, nums)


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    obj = Solution()
    result = obj.search(nums, target)
    print(result)