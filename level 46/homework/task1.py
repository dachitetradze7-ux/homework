# sentence = "1"
# sentences = []

# while sentence != "":
#     sentence = input("enter sentence:")
#     sentences.append(sentence)
# sentences.pop()

# file = "sentences.txt"

# with open(file, "w", encoding="utf-8")as file:
#     for sentence in sentences:
#         file.write(sentence + "\n")

# with open(file, "r", encoding="utf-8")as file:
#     lines = file.readlines()
#     count = []
#     for line in lines:
#         line = line.strip()
#         words = line.split(" ")
#         count.append(len(words))
#     longest = max(count)
#     longest_index = count.index(longest)
#     longest_line = lines[longest_index]
#     print(longest_line)
#     vowels = 'aeiou'
#     vowel_count = {}
#     for vowel in vowels:
#         vowel_count[vowel] =   0
#     for line in lines:
#         for char in line:
#             if char.lower() in vowels:
#                 vowel_count[char.lower()] +=  1
#     print(vowel_count)
#     for line in lines:
#         new_line = ''
#         for char in line:
            
#                 new_line += char
#         print(new_line)
# file = "sentences.txt"















