def manual_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
        return -1
    

nums = [14, 16, 20, 40]
print(manual_index(nums,20))



def manual_count(lst, value):
    count = 0
    for number in lst:
        if number == value:
            count += 1
    return count

nums= [17, 30, 12, 50]
print(manual_count(nums, 12))


fruits = ['banana', 'apple', 'cherry']
cities = ['new york', 'berlin', 'paris' ]
numbers = [2, 3, 18, 70]

print(fruits.index('banana'))
print(fruits.count('cherry'))


numbers.sort()
print(numbers)





print(sorted(cities))


print(min(numbers))
print(max(numbers))


fruits = ['apple', 'banana', 'banana', 'banana']
print(fruits.count('banana'))


animals = ("lion", "wolf", "fox", "monkey")
print(animals.count("fox"))
print(animals.index("monkey"))


tuple_info = ("goa", 5, False)

print(tuple_info)
print(len(tuple_info))
print(type(tuple_info))


student = ("dachi", 20, "python")

name, age, curse = student

print(name)
print(age)
print(curse)



g = (14, 19, 25, 30)

numbers = list(g)
numbers.append(28)


g = tuple(numbers)
print(g)


numbers = {15, 20, 25}
numbers.add(30)
numbers.remove(20)

even_numbers = {15, 40, 60}

print(numbers.union(even_numbers))
print(numbers.intersection(even_numbers))
print(numbers.difference(even_numbers))
