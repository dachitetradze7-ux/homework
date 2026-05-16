mixed = [2, 5, 8, 11, 14, 17, 20]
evens = [num for num in mixed if num % 2 == 0]
odds = [num for num in mixed if num % 2 != 0]
print(evens)
print(odds)