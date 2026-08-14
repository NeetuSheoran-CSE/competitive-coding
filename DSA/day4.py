def linearSearch(arr, target):
    positions = []

    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)

    return positions


def binarySearchFirst(arr, target):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first


def binarySearchLast(arr, target):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last


def binarySearch(arr, target):
    first = binarySearchFirst(arr, target)
    last = binarySearchLast(arr, target)

    if first == -1:
        return []

    positions = []

    for i in range(first, last + 1):
        positions.append(i)

    return positions


if __name__ == "__main__":

    arr = [10,20,20,20,30,40,40,50,60,70,70,70]

    target = int(input("enter target: "))

    linear_positions = linearSearch(arr, target)
    binary_positions = binarySearch(arr, target)

    print("Linear Search")
    print("Index:", linear_positions)
    print("Occurrences:", len(linear_positions))

    print("Binary Search")
    print("Index:", binary_positions)
    print("Occurrences:", len(binary_positions))