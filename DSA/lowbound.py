
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
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.lowerBound(nums,target)
        
s = Solution()

print(s.searchInsert([1,3,4,5,6],4))
print(s.searchInsert([1,3,4,5,6],7))
print(s.searchInsert([1,3,4,5,6],0))


##### UPPER BOUND ########

class Solution:
    def lowerBound(self, nums, target):
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
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.lowerBound(nums,target)
        
s = Solution()

print(s.searchInsert([1,3,4,5,6],4))
print(s.searchInsert([1,3,4,5,6],7))
print(s.searchInsert([1,3,4,5,6],0))