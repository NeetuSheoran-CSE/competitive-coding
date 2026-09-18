# Implement Lower Bound


class Solution:
    def lowerBound(self, arr, target):
        left,right,answer = 0,len(arr)-1,len(arr)
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]>=target:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
                    
                    
                    
#upper bound


class Solution:
    def upperBound(self, arr, target):
        # code here
        left,right,answer = 0,len(arr)-1,len(arr)
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]>target:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
    
    
# class Solution:
#     def firstisBadVersion(self, arr, target)->int:
#         left,right,answer = 0,len(arr)-1,len(arr)
#         while left<=right:
#             mid=left+(right-left)//2
#             if isBadVersion[mid]:
#                 answer=mid
#                 right=mid-1
#             else:
#                 left=mid+1
#         return answer
    
    
    
 #koko eating banana   
    
class Solution:
    def minEatingSpeed(self,piles:list[int],h:int)->int:
      maxSpeed = max(piles)
      for speed in range(1,maxSpeed+1):
          totalHours=0
          for pile in piles:
            hours=(pile+speed-1)//2
            totalHours+=hours
          if totalHours<=h:
           return speed
      return maxSpeed
  


 #m2 by binary search 
  
class Solution:
    def minEatingSpeed(self,piles:list[int],h:int)->int:
        left = 1
        right = max(piles)
        answer=right
        while left<=right:
            mid = (len+right)//2
            totalHours = 0
            speed = mid
            for pile in piles:
                totalHours += (pile+mid-1)/mid
            if totalHours <= h:
                answer = mid
                right = mid-1
            else:
                left = mid+1
        return answer 