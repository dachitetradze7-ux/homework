nums = list(range(1, 21))

squares = []
for n in nums:
    squares.append(n**2)

squares = [n**2 for n in nums]

print(f"for: {squares}")
print(f"comp: {squares}")