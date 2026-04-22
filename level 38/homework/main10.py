animals = ["tigers", " lion", "zebra", "elephant", "giraffe"]

first_letters = []
for animal in animals:
    first_letters.append(animal[0])

first_letters = [animal[0] for animal in animals]

e_animals = [animal for animal in animal if animal.startswith("e")]

print(e_animals)
print(f"comp: {first_letters}")
print(f"for: {first_letters}")