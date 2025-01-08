from typing import List


def longest(nums: List[int]) -> int:
    sett = set(nums)
    longest = 0
    
    for n in nums:
        if n - 1 not in sett:
            length = 0
            while (length + n) in sett:
                length+=1
            longest = max(longest, length)
    
    return longest
            

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    result = longest(nums)
    print(result)