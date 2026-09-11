# 3. Basic Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift element right
            j -= 1
        arr[j + 1] = key  # insert key into correct position

arr = [9, 5, 1, 4, 3]
insertion_sort(arr)
print(arr)  # Output: [1, 3, 4, 5, 9]



# 6. Sort a List of Strings by Length

def insertion_sort_by_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(arr[j]) > len(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

words = ["banana", "kiwi", "apple", "fig", "watermelon"]
insertion_sort_by_length(words)
print(words)  # Output: ['fig', 'kiwi', 'apple', 'banana', 'watermelon']


# 7. Check if Array is Sorted (Helper Function)


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 2, 9, 1, 6]
bubble_sort(arr)
print(arr, "->", is_sorted(arr))  # Output: [1, 2, 5, 6, 9] -> True

# We walk through the array checking every adjacent pair — if any pair is out of order, it's not sorted. This is a handy sanity check to automate testing instead of manually inspecting output.

# 8. Insertion Sort with Step-by-Step Print

def insertion_sort_verbose(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"After inserting {key}: {arr}")

arr = [9, 5, 1, 4, 3]
insertion_sort_verbose(arr)

# Output:

# After inserting 5: [5, 9, 1, 4, 3]
# After inserting 1: [1, 5, 9, 4, 3]
# After inserting 4: [1, 4, 5, 9, 3]
# After inserting 3: [1, 3, 4, 5, 9]

# The print sits right after arr[j+1] = key, so you see the array right after each new element gets placed — a great way to visualize the "sorted portion growing left to right."

# 9. Bubble Sort a List of Tuples by Second Element


def bubble_sort_tuples_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][1] < arr[j + 1][1]:  # compare scores, descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

students = [("Alice", 85), ("Bob", 72), ("Carol", 90)]
bubble_sort_tuples_desc(students)
print(students)  # Output: [('Carol', 90), ('Alice', 85), ('Bob', 72)]

# We index into each tuple with [1] to compare only the score, and use < (instead of >) to sort descending — highest score bubbles to the front.

# 10. Which Algorithm Does Fewer Comparisons?

def bubble_sort_count_comparisons(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

def insertion_sort_count_comparisons(arr):
    arr = arr.copy()
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

data = [5, 1, 4, 2, 8]
b_comps = bubble_sort_count_comparisons(data)
i_comps = insertion_sort_count_comparisons(data)

print(f"Bubble sort comparisons: {b_comps}")
print(f"Insertion sort comparisons: {i_comps}")

if b_comps < i_comps:
    print("Bubble sort made fewer comparisons")
elif i_comps < b_comps:
    print("Insertion sort made fewer comparisons")
else:
    print("Both made the same number of comparisons")
    
    
    
    # 11. Insertion Sort on a Linked List (Conceptual + Array Simulation)
    
#     def insertion_sort_count_shifts(arr):
#     shifts = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             shifts += 1
#             j -= 1
#         arr[j + 1] = key
#     return shifts

# arr = [5, 1, 4, 2, 8]
# shifts = insertion_sort_count_shifts(arr)
# print(arr, "Shifts:", shifts)  # Output: [1, 2, 4, 5, 8] Shifts: 4


# 12. Detect if Only One Swap Away From Sorted

def one_swap_away(arr):
    sorted_arr = sorted(arr)
    diff_indices = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]
    if len(diff_indices) == 0:
        return True  # already sorted
    if len(diff_indices) == 2:
        i, j = diff_indices
        return arr[i] == sorted_arr[j] and arr[j] == sorted_arr[i]
    return False

print(one_swap_away([1, 5, 3, 4, 2]))  # Output: False
print(one_swap_away([1, 4, 3, 2, 5]))  # Output: True


# 13. Insertion Sort — Find the Position Using Binary Search

def binary_search_pos(arr, key, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search_pos(arr, key, i - 1)
        j = i - 1
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1
        arr[pos] = key

arr = [9, 5, 1, 4, 3]
binary_insertion_sort(arr)
print(arr)  # Output: [1, 3, 4, 5, 9]


# 14. Sort Only the Odd-Indexed Elements

def sort_odd_indices(arr):
    odd_values = [arr[i] for i in range(1, len(arr), 2)]

    # bubble sort the extracted odd-indexed values
    n = len(odd_values)
    for i in range(n):
        for j in range(n - i - 1):
            if odd_values[j] > odd_values[j + 1]:
                odd_values[j], odd_values[j + 1] = odd_values[j + 1], odd_values[j]

    # place sorted values back into odd indices
    for idx, val in enumerate(odd_values):
        arr[2 * idx + 1] = val

    return arr

arr = [5, 8, 3, 1, 9, 2]
print(sort_odd_indices(arr))  # Output: [5, 1, 3, 2, 9, 8]

# 15. Insertion Sort — Sort Based on Absolute Difference from a Target

def sort_odd_indices(arr):
    odd_values = [arr[i] for i in range(1, len(arr), 2)]

    # bubble sort the extracted odd-indexed values
    n = len(odd_values)
    for i in range(n):
        for j in range(n - i - 1):
            if odd_values[j] > odd_values[j + 1]:
                odd_values[j], odd_values[j + 1] = odd_values[j + 1], odd_values[j]

    # place sorted values back into odd indices
    for idx, val in enumerate(odd_values):
        arr[2 * idx + 1] = val

    return arr

arr = [5, 8, 3, 1, 9, 2]
print(sort_odd_indices(arr))  # Output: [5, 1, 3, 2, 9, 8]



# 6. Cocktail Shaker Sort (Bidirectional Bubble Sort)

def cocktail_sort(arr):
    n = len(arr)
    start, end = 0, n - 1
    swapped = True

    while swapped:
        swapped = False

        # forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1

        if not swapped:
            break

        # backward pass
        swapped = False
        for i in range(end, start, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        start += 1

    return arr

arr = [5, 1, 4, 2, 8, 0, 2]
print(cocktail_sort(arr))  # Output: [0, 1, 2, 2, 4, 5, 8]



# 17. Insertion Sort — Count Inversions

def count_inversions_insertion(arr):
    inversions = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            inversions += 1
            j -= 1
        arr[j + 1] = key
    return inversions

arr = [2, 4, 1, 3, 5]
print(count_inversions_insertion(arr))  # Output: 3


# 18. Bubble Sort with a Custom Comparator Function

def bubble_sort_custom(arr, comparator):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if comparator(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ascending
arr1 = [5, 2, 9, 1]
bubble_sort_custom(arr1, lambda a, b: a > b)
print(arr1)  # Output: [1, 2, 5, 9]

# descending
arr2 = [5, 2, 9, 1]
bubble_sort_custom(arr2, lambda a, b: a < b)
print(arr2)  # Output: [9, 5, 2, 1]

# sort strings by length
arr3 = ["kiwi", "fig", "banana"]
bubble_sort_custom(arr3, lambda a, b: len(a) > len(b))
print(arr3)  # Output: ['fig', 'kiwi', 'banana']