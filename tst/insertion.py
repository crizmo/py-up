import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

# Test the function
arr = np.array([4, 3, 2, 10, 12, 1, 5, 6])
sorted_arr = insertion_sort(arr)
print(sorted_arr)