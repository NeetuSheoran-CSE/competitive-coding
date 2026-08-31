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