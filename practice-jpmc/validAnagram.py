from typing import Counter


def validAnagram(s: str, t: str) -> bool:
    # Your implementation here
    if len(s) != len(t):
        return False
    
    s1 = {}
    t1 = {}
    
    for n in range(len(s)):
        s1[s[n]] = 1 + s1.get(s[n], 0)
        t1[t[n]] = 1 + t1.get(t[n], 0)
        
    
    return s1 == t1

# Test cases
def test_validAnagram():
    assert validAnagram("anagram", "nagaram") == True
    assert validAnagram("rat", "car") == False
    assert validAnagram("a", "a") == True
    assert validAnagram("ab", "ba") == True
    assert validAnagram("abc", "cba") == True
    assert validAnagram("abcd", "dcba") == True
    assert validAnagram("abcd", "abce") == False

if __name__ == "__main__":
    test_validAnagram()
    print("All tests passed.")