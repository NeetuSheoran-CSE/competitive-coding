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




