from typing import Counter


class Solution:
    def longest_palindrome(self, s:str) -> int:
        counter_s = Counter(s)
        total = 0
        oddexist = False
        
        for char in counter_s:
            if counter_s[char] %2 == 0:
                total+= counter_s[char] 
            else:
                total += counter_s[char] - 1
                oddexist = True
        
        return total + 1 if oddexist else total





if __name__ == "__main__":
    obj = Solution()
    s = 'abccccddza'
    result = obj.longest_palindrome(s)
    print(result)
