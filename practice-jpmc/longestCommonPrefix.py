from typing import List


def longestCommon(s: List[str]) -> str:
    sorted_str = sorted(s)
    
    s1 = sorted_str[0]
    s2 = sorted_str[-1]
    
    index = 0
    
    while index < len(s1):
        if (s1[index] == s2[index]):
            index +=1
        else:
            break
        
    if index == 0:
        return ""
    else:
        return s1[0:index]    
    
    
    
strs = ["flower","flow","flight"]

result = longestCommon(strs)

print(result)
