# Given a sorted array nums and a target, return the index of target, or -1 if it isn't present.


def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
print(binary_search([1, 3, 5, 7, 9, 11], 4))   # -1

# Time: O(log n), Space: O(1)

# Q2. First and Last Position of an Element

# Given a sorted array with duplicates, find the first and last index of target. Return [-1, -1] if not found.


def search_range(nums, target):
    def find(is_first):
        low, high, ans = 0, len(nums) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                if is_first:
                    high = mid - 1   # keep looking left
                else:
                    low = mid + 1    # keep looking right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    return [find(True), find(False)]

print(search_range([5, 7, 7, 8, 8, 8, 10], 8))  # [3, 5]
print(search_range([5, 7, 7, 8, 8, 8, 10], 6))  # [-1, -1]

# Time: O(log n), Space: O(1)

# Q3. Search Insert Position

# Given a sorted array of distinct integers and a target, return the index where it is found, or the index where it would be inserted to keep the order.

def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low   # insertion point

print(search_insert([1, 3, 5, 6], 5))  # 2
print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4

# Trick: When the loop ends, low is always the correct insertion position.

# Q4. Square Root of a Number (Integer)

# Given a non-negative integer x, return its square root rounded down, without using sqrt() or **0.5.

def my_sqrt(x):
    low, high, ans = 0, x, 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= x:
            ans = mid          # possible answer, try bigger
            low = mid + 1
        else:
            high = mid - 1
    return ans

print(my_sqrt(16))  # 4
print(my_sqrt(8))   # 2
print(my_sqrt(0))   # 0

# Idea: Binary search on the answer range (0 to x), not on an array. This pattern is called "binary search on answer".

# Q5. Search in a Rotated Sorted Array

# A sorted array of distinct values has been rotated at some pivot (e.g., [0,1,2,4,5,6,7] becomes [4,5,6,7,0,1,2]). Find the index of target in O(log n).

def search_rotated(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # -1