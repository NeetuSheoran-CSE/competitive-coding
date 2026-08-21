
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