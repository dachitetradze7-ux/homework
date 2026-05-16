animals = ["tiger", "lion", "zebra", "elephant", "giraffe"]

first_letter_for = []
for animal in animals:
    first_letter_for.append(animal[0])
print(first_letter_for)

first_letter_comp = [animal[0] for animal in animals]
print(first_letter_comp)

start_e = [animal for animal in animals if animal.startswith("e")]
print(start_e)