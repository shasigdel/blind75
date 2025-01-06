from typing import List

class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isValid(self, s:str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l+=1
            while r>l  and not self.alphaNum(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False

            l,r = l+1, r-1

        return True


if __name__ == '__main__':
    obj = Solution()
    result = obj.isValid("A man, a plan, a canal: Panama")
    print(result)