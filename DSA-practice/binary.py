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