# def search(arr, target):
#     n = len(arr)
#     comparisons = 0

#     for i in range(n):
#         comparisons += 1

#         if arr[i] == target:
#             return i, comparisons

#     return -1, comparisons


# def binarySearch(arr, target, low, high):
#     index = -1
#     comparisons = 0

#     while low <= high:
#         mid = low + (high - low) // 2
#         comparisons += 1

#         if arr[mid] == target:
#             index = mid
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return index, comparisons


# def compare_search_algorithms(arr, target):

#     linear_index, linear_comparisons = search(arr, target)

  
#     n = len(arr)
#     binary_index, binary_comparisons = binarySearch(
#         arr, target, 0, n - 1
#     )

#     if linear_comparisons < binary_comparisons:
#         better = "Linear Search"
#     elif binary_comparisons < linear_comparisons:
#         better = "Binary Search"
#     else:
#         better = "Both Equal"

#     return [
#         "Search Comparison Report",
#         "Linear Search",
#         "Index: " + str(linear_index),
#         "Comparisons: " + str(linear_comparisons),
#         "Binary Search",
#         "Index: " + str(binary_index),
#         "Comparisons: " + str(binary_comparisons),
#         "Better Algorithm: " + better
#     ]



# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#     target = int(input())

#     result = compare_search_algorithms(arr, target)

#     for line in result:
#         print(line)
    
    
   
def compare_search_algorithms(arr, target):

    # Linear Search
    linear_index = -1
    linear_count = 0
    occurrences = 0

    for i in range(len(arr)):
        linear_count += 1

        if arr[i] == target:
            if linear_index == -1:
                linear_index = i
            occurrences += 1

    # Binary Search
    binary_index = -1
    binary_count = 0

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        binary_count += 1

        if arr[mid] == target:
            binary_index = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    # Find better algorithm
    if linear_count < binary_count:
        better = "Linear Search"
    elif binary_count < linear_count:
        better = "Binary Search"
    else:
        better = "Both Equal"

    return [
        "Search Comparison Report",
        "Linear Search",
        "Index: " + str(linear_index),
        "Comparisons: " + str(linear_count),
        "Binary Search",
        "Index: " + str(binary_index),
        "Comparisons: " + str(binary_count),
        "Occurrences: " + str(occurrences),
        "Better Algorithm: " + better
    ]


# Testing
arr = [10, 20, 20, 20, 40, 50, 60, 70, 70, 70]

target = int(input("Enter target: "))

result = compare_search_algorithms(arr, target)

for line in result:
    print(line)