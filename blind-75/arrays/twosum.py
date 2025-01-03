from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[val] = idx
        
if __name__ == "__main__":
    list_ = [4,5,6]
    target = 10

    tsObj = TwoSum()
    result = tsObj.twoSum(list_, target)
    print(result)
