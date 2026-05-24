def get_element_by_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "mistake: out of list"
my_list = [10,20,30]
print(get_element_by_index(my_list, 10))