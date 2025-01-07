def longestPalindrome(s: str) -> str:
    def center(left: int, right:int) -> int:
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-= 1
            right+=1
        return s[left + 1: right]

    if not s:
        return ""

    longest = ""
    
    for i in range(len(s)):
        pali1 = center(i, i)
        pali2 = center(i, i + 1)
    
        if len(pali1) > len(longest):
            longest = pali1
        if len(pali2) > len(longest):
            longest = pali2
    return longest
    
# Test cases
if __name__ == "__main__":
    test_cases = [
        ("babad", "bab"),  # or "aba"
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),  # or "c"
        ("", ""),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = longestPalindrome(input_str)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")