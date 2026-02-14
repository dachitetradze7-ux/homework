nums = (1, 2, 3, 2, 4, 2, 5)
print(type(nums))
print(nums.count(2))
print(nums.index(5))

def manual_count(sequence, target):
    count = 0
    for item in sequence:
        if item == target:
            count += 1
            return count
        print(manual_count(nums,2))
