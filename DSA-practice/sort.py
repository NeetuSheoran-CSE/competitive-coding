# find the first and last position of element in sorted array 

class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        l = 0
        r=n-1
        ans = n
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] >= target:
                ans = mid 
                r = mid-1
            else:
                l = mid+1
        
        return ans
    

    def upperBound(self, nums, target):
        n = len(nums)
        l = 0
        r=n-1
        ans = n
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] > target:
                ans = mid 
                r = mid-1
            else:
                l = mid+1
        
        return ans
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)
        
        if lb==ub:
            # element not present in array
            return [-1,-1]
        else:
            return [lb,ub-1]
      
s = Solution()

print(s.searchRange([1,3,4,5,6],4))
print(s.searchRange([1,3,4,5,6],7))
print(s.searchRange([1,3,4,5,6],0))




#11.Find Minimum in Rotated Sorted Array

#Given a sorted array rotated at an unknown pivot (no duplicates), find the minimum element in O(log n) time.

#python
def find_min(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1  # min is in right half
        else:
            high = mid  # min is in left half (including mid)
    return arr[low]

print(find_min([4, 5, 6, 7, 0, 1, 2]))  # Output: 0



# 12. Two Sum on Sorted Array (Two-Pointer + Search Logic)

# Given a sorted array, find two numbers that add up to a target sum. Return their indices.

# python
def two_sum_sorted(arr, target):
    low, high = 0, len(arr) - 1
    while low < high:
        current_sum = arr[low] + arr[high]
        if current_sum == target:
            return (low, high)
        elif current_sum < target:
            low += 1  # need a bigger sum, move left pointer right
        else:
            high -= 1  # need a smaller sum, move right pointer left
    return (-1, -1)

print(two_sum_sorted([2, 7, 11, 15], 9))  # Output: (0, 1)




# 13. Square Root Using Binary Search

# Find the integer square root of a non-negative number n (i.e., the largest integer x such that x*x <= n), without using n**0.5.

# python
def integer_sqrt(n):
    if n < 2:
        return n
    low, high = 1, n
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid  # mid could be the answer, keep track
            low = mid + 1
        else:
            high = mid - 1
    return result

print(integer_sqrt(28))  # Output: 5 (since 5*5=25 <= 28 < 36=6*6




# 14. Find the Majority Element (Linear Search / Counting)

# Given an array, find the element that appears more than n/2 times. Assume it always exists. Use the Boyer-Moore Voting technique (a clever linear scan).

# python
def majority_element(arr):
    count = 0
    candidate = None
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2


#21. Search in a Sorted Array with Infinite Duplicates

#python
def search_with_duplicates(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # if we can't tell which side is sorted, shrink both ends
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_with_duplicates([1, 1, 1, 1, 1, 2, 3], 2)) 



# 22. Find the Missing Number in a Sorted Array (1 to N)

def find_missing(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # if no numbers are missing before index mid, arr[mid] should equal mid+1
        if arr[mid] == mid + 1:
            low = mid + 1  # missing number is to the right
        else:
            high = mid - 1  # missing number is at or before mid
    return low + 1  # the missing number

print(find_missing([1, 2, 3, 5, 6]))  # Output: 4




# 23. Allocate Minimum Pages (Binary Search on Answer)

def allocate_books(arr, m):
    def is_feasible(max_pages):
        students = 1
        current_sum = 0
        for pages in arr:
            if pages > max_pages:
                return False  # single book exceeds limit, impossible
            if current_sum + pages > max_pages:
                students += 1
                current_sum = pages
            else:
                current_sum += pages
        return students <= m

    low, high = max(arr), sum(arr)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(mid):
            result = mid  # mid pages is enough, try smaller
            high = mid - 1
        else:
            low = mid + 1  # mid pages not enough, need more
    return result

print(allocate_books([12, 34, 67, 90], 2))  # Output: 113



# 24. Median of Two Sorted Arrays

def find_median_sorted_arrays(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1  # ensure arr1 is smaller

    m, n = len(arr1), len(arr2)
    low, high = 0, m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1

        max_left1 = float('-inf') if partition1 == 0 else arr1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else arr1[partition1]

        max_left2 = float('-inf') if partition2 == 0 else arr2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else arr2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1

print(find_median_sorted_arrays([1, 3], [2]))       # Output: 2
print(find_median_sorted_arrays([1, 2], [3, 4]))    # Output: 2.5




# 25. Find the Closest Element to a Target

def find_closest(arr, target):
    low, high = 0, len(arr) - 1
    if target <= arr[low]:
        return arr[low]
    if target >= arr[high]:
        return arr[high]

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # after loop, high < low; closest is one of arr[high] or arr[low]
    if (arr[low] - target) < (target - arr[high]):
        return arr[low]
    else:
        return arr[high]

print(find_closest([1, 3, 8, 10, 15], 12))  # Output: 10