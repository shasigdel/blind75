def reverse_string(s: str) -> str:
    words = s.split()
    words.reverse()
    
    return ' '.join(words)

s1 = "the sky is blue"
result = reverse_string(s1)
print(result)