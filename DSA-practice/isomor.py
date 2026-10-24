#205 isomorphic strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        StoT={}
        TtoS={}
        for chs,cht in zip(s,t):
          if chs in StoT and StoT[chs]!=cht:
            return False
          if cht in TtoS and TtoS[cht]!=chs:
            return False
          StoT[chs]=cht
          TtoS[cht]=chs
        return True
    
    
#count words in a string    
class Solution:
    def countWords(self,s:str)->int:
        return len(s.split())
    
    
#count frequency of words in a string
class Solution:
    def countWords(self,s:str)->dict:
        words=s.split()
        freq={}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        return freq
    
#solve character by frequency
class Solution:
    def frequencySort(self,s:str)->str:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=""
        for ch,count in sorted_freq:
            result+=ch*count
        return result
    
    
    
    
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
            
            
            
            
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k