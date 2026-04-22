numbers = [1, 4, 7, 10, 13, 16, 19] 
new_list_for = []
for n in numbers:
    if n % 2 != 0:
        new_list_for.append(n * 2)

new_list_comp = [n * 2 for n in numbers if n % 2 != 0]
print(f"for: {new_list_for}")
print(f"comp: {new_list_comp}")