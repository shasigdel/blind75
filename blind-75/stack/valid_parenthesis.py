class Solution:
    def valid_parenthesis(self, s:str) -> bool:
        isValid = {'}':'{',
                   ']':'[',
                   ')':'('}
        stack_ = []
        
        for char in s:
            if char in isValid:
                if stack_ and stack_[-1] == isValid[char]:
                    stack_.pop()
                else:
                    return False
            else:
                stack_.append(char)

        return True if not stack_ else False
    
if __name__ == "__main__":
    obj = Solution()
    result = obj.valid_parenthesis('{[()]}')
    print(result)
