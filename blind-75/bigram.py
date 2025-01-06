def find_bigrams(sentence):
    words = sentence.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return bigrams


text = 'Machine learning algorithms provide valuable insights.'
result = find_bigrams(text)

print(result)