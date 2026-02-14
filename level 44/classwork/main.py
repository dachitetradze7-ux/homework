def insertion_sort(arr):

    for index in range(len(arr)):
        j = index 


        while arr[j - 1] > arr[j] and j > 0:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

print(insertion_sort([6, 3, 7, 5, 4]))