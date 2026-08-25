
#TWO SUM PROBLEM

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in seen:
                return [seen[needed],i]
        seen[nums[i]]=i  
        
        
        
 #ROTATE ARRAY       
        
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left += 1
                right -= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        
#3005. Count Elements With Maximum Frequency        
        
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        maxFreq = max(freq.values())
        answer = 0

        for count in freq.values():
            if count == maxFreq:
                answer += count
        return answer
    
    
# 16. Find the K-th Smallest Element Using Binary Search (on value range)

# Given an unsorted array, find the K-th smallest element using binary search over the value range (not sorting first).

# python
def kth_smallest(arr, k):
    low, high = min(arr), max(arr)
    while low < high:
        mid = (low + high) // 2
        count = sum(1 for num in arr if num <= mid)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # Output: 7



# 17. Find First Bad Version (Binary Search on Boolean Condition)

# You have n versions [1, 2, ..., n], and at some point they start being "bad." Given a function is_bad(version) that returns True/False, find the first bad version using the fewest calls.

# python
def is_bad(version):  # example implementation for testing
    return version >= 4

def first_bad_version(n):
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if is_bad(mid):
            high = mid  # first bad could be mid or earlier
        else:
            low = mid + 1  # first bad is after mid
    return low

print(first_bad_version(10))  # Output: 4




# 18. Search in an Infinite (Unbounded) Sorted Array

# Given a sorted array of unknown size (you can only check arr[i], and it throws an error or returns None beyond the bounds), find a target efficiently.

# python
def search_unbounded(arr, target):
    # Step 1: find a range where target could exist
    low, high = 0, 1
    while high < len(arr) and arr[high] < target:
        low = high
        high *= 2
    high = min(high, len(arr) - 1)

    # Step 2: standard binary search within [low, high]
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(search_unbounded(arr, 11))  # Output: 5



# 19. Find Fixed Point (Index Equals Value)

# Given a sorted array of distinct integers, find an index i such that arr[i] == i, using binary search. Return -1 if none exists.

# python
def find_fixed_point(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(find_fixed_point([-10, -5, 0, 3, 7]))  # Output: 3 (arr[3] == 3)




# 20. Search a Target in a Sorted Array of Unknown Order (Ascending or Descending)

# Given a sorted array that could be either ascending or descending (you don't know which), find the target using binary search.

# python
def search_unknown_order(arr, target):
    low, high = 0, len(arr) - 1
    ascending = arr[low] <= arr[high]  # detect the order first

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if ascending:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] > target:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_unknown_order([9, 7, 5, 3, 1], 5))  # Output: 2
print(search_unknown_order([1, 3, 5, 7, 9], 5))  # Output: 2