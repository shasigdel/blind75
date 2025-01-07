# Sliding Window

def length_of_longest_substring(s: str) -> int:
    charSet = set()
    
    left = 0
    res = 0
    
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        
        res = max(res, right - left + 1)
    return res

s = "abcabcbb"
result = length_of_longest_substring(s)
print(result)  # 3
