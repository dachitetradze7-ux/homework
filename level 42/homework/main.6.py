my_list = [5, 10, 15]
try:
    print(my_list[10])
except IndexError:
    print("incorrect index!")