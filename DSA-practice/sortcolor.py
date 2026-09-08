# 75. Sort Colors


from ast import List


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zero = 0
        one = 0
        two = 0
        for num in nums:
            if num==0:
                zero+=1
            elif num == 1:
                one += 1
            else:
                two += 1
        index = 0
        for i in range(zero):
            nums[index]=0
            index+=1
        for i in range(one):
            nums[index]=1
            index+=1
        for i in range(two):
            nums[index]=2
            index+=1
            
            
 #method 2            
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
                
                
                

# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxWater = 0
        for i in range(n):
            for j in range(i+1,n):
                width = j-i
                h = min(height[i],height[j])
                area = width*h
                maxWater = max(maxWater,area)
        return maxWater
    
    
    
#method 2     
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        while left<right:
            width = right - left
            h = min(height[left],height[right])
            area = width*h
            maxWater = max(maxWater,area)
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return maxWater