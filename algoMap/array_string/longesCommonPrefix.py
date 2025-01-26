from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_ = sorted(strs)
        
        first = sorted_[0]
        last = sorted_[-1]
        
        index = 0
        
        while index < len(first):
            if first[index] == last[index]:
                index+=1
            else:
                 break
        if index == 0:
            return ""

        return first[0:index]
