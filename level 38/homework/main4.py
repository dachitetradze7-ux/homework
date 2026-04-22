animal = {
    "breed": "lion",
    "habit": "africa"
}

animal_copy = animal.copy()
print(f"animal: {animal}")
print(f"copy animal: {animal_copy}")

animal.clear()
animal_copy.clear()


print(f"animal after clear: [animal]")
print(f"copy animal after clear: {animal_copy}")