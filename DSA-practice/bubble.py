# 1. Basic Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
print(arr)  # Output: [1, 2, 5, 5, 6, 9]


# . Optimized Bubble Sort (Early Exit)

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # array is already sorted, stop early

arr = [1, 2, 3, 5, 4]
bubble_sort_optimized(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]


# 4. Count Swaps in Bubble Sort

def bubble_sort_count_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return swap_count

arr = [4, 3, 2, 1]
swaps = bubble_sort_count_swaps(arr)
print(arr)          # Output: [1, 2, 3, 4]
print(swaps)        # Output: 6



# 5. Sort in Descending Order

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  # flipped: < instead of >
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:  # flipped: < instead of >
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr1 = [5, 2, 9, 1, 6]
bubble_sort_desc(arr1)
print(arr1)  # Output: [9, 6, 5, 2, 1]

arr2 = [5, 2, 9, 1, 6]
insertion_sort_desc(arr2)
print(arr2)  # Output: [9, 6, 5, 2, 1]