words = ["apple", "banana", "cat", "elephant", "dog", "grapefruit"]
long_words_for = []
for word in words:
    if len(word) > 5:
        long_words_for.append(word)
print(long_words_for)

long_words_comp = [word for  word in words if len(word) > 5]
print(long_words_comp)