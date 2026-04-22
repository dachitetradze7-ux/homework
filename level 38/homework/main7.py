words = ["apple", "banana", "cat", "elephant", "dog", "grapefruit"] 

words_for = []
for word in words:
    if len(word) > 5:
        words_for.append(word)

words_comp = [word for word in words if len(word) > 5]

print(f"for: {words_for}")
print(f"comp: {words_comp}")