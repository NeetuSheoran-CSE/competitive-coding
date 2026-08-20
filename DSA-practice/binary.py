#4. Recursive Binary Search
#Rewrite question 3, but implement 
#it recursively instead of iteratively.

def binarySearch(arr, target, low, high):

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binarySearch(arr, target, low, mid - 1)

    else:
        return binarySearch(arr, target, mid + 1, high)


# Example
arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binarySearch(arr, target, 0, len(arr) - 1)

print("Index:", result)



# First and Last Position
#Given a sorted list with duplicate elements,
#write a function that uses binary search to find the 
#first and last index of a given target value. (Hint: you'll
#need to modify the standard binary search to keep searching 
#left/right even after finding a match.) Return (-1, -1) if the 
#target isn't present.


def firstAndLastPosition(arr, target):
    first = -1
    last = -1

    # Find first position
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1       # Continue searching left

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    # Find last position
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1        # Continue searching right

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return (first, last)


# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(firstAndLastPosition(arr, target))




#6. Search in a Rotated Sorted Array

#Given a sorted array that has been rotated at some pivot (e.g., [4,5,6,7,0,1,2]), find the index of a target value using a modified binary search.

#python
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))  # Output: 4




#7. Find the Smallest Missing Number (Linear Search)

#Given an unsorted list of positive integers, find the smallest positive integer missing from it, using linear search logic.

#python
def smallest_missing(arr):
    num_set = set(arr)
    i = 1
    while i in num_set:
        i += 1
    return i

print(smallest_missing([3, 4, -1, 1]))  # Output: 2




8#8. Count Occurrences Using Binary Search

#Given a sorted array with duplicates, count how many times a target appears — using binary search (not linear scan) for efficiency.

#python
def count_occurrences(arr, target):
    def find_first(arr, target):
        low, high, result = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def find_last(arr, target):
        low, high, result = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = find_first(arr, target)
    if first == -1:
        return 0
    last = find_last(arr, target)
    return last - first + 1

print(count_occurrences([1,2,2,2,3,4,5], 2))  # Output: 3




# 9. Find Peak Element (Binary Search)

# A peak element is one that is greater than its neighbors. Given an unsorted array, find the index of any peak element in O(log n) time.

# python
def find_peak(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid  # peak is in left half (including mid)
        else:
            low = mid + 1  # peak is in right half
    return low

print(find_peak([1, 3, 20, 4, 1, 0]))  # Output: 2 (val



# 10. Search Insert Position (Binary Search)

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be inserted to keep the array sorted.

# python
def search_insert(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low  # insertion point

print(search_insert([1, 3, 5, 6], 5))  # Output: 2 (found)
print(search_insert([1, 3, 5, 6], 2))  # Output: 1 (ins




# 15. Binary Search on a 2D Sorted Matrix

# Given a matrix where each row is sorted left-to-right and each column is sorted top-to-bottom, search for a target value efficiently (better than checking every cell).

# python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1  # start top-right corner
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # eliminate this column
        else:
            row += 1  # eliminate this row
    return False

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16]
]
print(search_matrix(matrix, 5))  # Output: True