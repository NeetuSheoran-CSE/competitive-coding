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