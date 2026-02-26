# fruit = ["apple", "grapes", "orange","banana"]

# def manual_index(sequence, target):
#     for index in range(len(sequence)):
#         if sequence[index] == target:
#             return index
        
#         return -1
    
# print(manual_index(fruit,"apple"))

# scores = (15, 18, 28, 36)

# john,jane, *others=scores

# print(john)
# print(jane)
# print(*others)

# score = (15, 10, 18, 25)
# pirveli, meore, *others = score
# print(min(score))
# print(max(score))


# nums = {5, 12, 76, 12, 12, 5, 25}

# elemnts = ["a", "d", "a", "c"]

# nums = {1, 2, 2, 4, 4, 4, 5}

# numss = set(nums)
# print(numss)


# nums = {5, 12, 76, 80}

# nums.add(4)
# nums.remove(76)
# print(nums)

# nums1 = {1,3,5,7,8}
# nums2 = {1,2,7,9}
# result = nums1.symmetric_difference(nums2)
# print(result) 


# nums_union = nums1.union(nums2) 
# print(nums_union) #გაეთიანება

# print(nums1.intersection(nums2))#თანაკვეთა
# print(nums1.difference(nums2))#სხვაობა
# print(nums1.symmetric_difference(nums2)) #გაერთიანება თანაკვეთა

# list - #list aris(mutable) shecvladi
# tuple - #tafli aris(immutable) sheucvladi
# set - aris tuples shebrunebuli da shecvla sheileba

# my_numbers = [5, 151, 12, 76, 12, 56, 25]

# sorted_nums = sorted(my_numbers)
# print(sorted_nums)

# print("5".isnumeric())

# print(my_numbers.sort())



# friends = {"anna", "merry",  "merry", "nana"}
# friends.clear()
# print(friends)


# set1 = {"apple", "banana"}
# set2 = {"banana", "cherry"}
# combined_set = set1.union(set2)
# print(combined_set)

set1 = {"apple", "orange", 'cherry', "banana"}
set2 = {"banana", "orange"}
unique = set1.difference(set2)
print(unique)