from typing import List


def topK(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        
    for n, c in count.items():
        freq[c].append(n)
        
    res = []
    
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    
nums = [1,1,2,2,2,3,100]
k = 2
result = topK(nums, k)
print(result)