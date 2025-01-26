class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2)) 
        res = ""
        
        for j in range(min_len):
            res+=word1[j]+word2[j]
        
        
        if len(word1) > len(word2):
            res+=word1[min_len:]
        elif word2 > word1:
            res+=word2[min_len:]
            
        return res

sol = Solution()

word1 = "abcdef"
word2 = "pqr"
result = sol.mergeAlternately(word1, word2)
    

print(result)