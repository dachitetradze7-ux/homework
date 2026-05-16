nums = list(range(1, 21))

square_for = [] 
for num in nums:
    square_for.append(num**2)
print(square_for)

square_comp = [num**2 for num in nums]
print(square_comp)