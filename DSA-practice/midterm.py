# def majority_element(arr):
#     candidate = None
#     count = 0
#     for num in arr:
#         if count == 0:
#             candidate = num
#         if num == candidate:
#             count += 1
#         else:
#                 count -=1
#         if arr.count(candidate)>len(arr)//2:
#             return candidate 
#         return -1 
# arr = [3, 2, 3]
# print(majority_element(arr))
        
        

# def binary_search(arr):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
        
#         else:
#             if arr[mid] <= target:
#                 low = mid + 1
                
#             else:
#                 high = mid-1
#     return -1 
# arr = [1,2,3,4,5,6,7]
# target = 5
# print(binary_search(arr))
        
    
      
# def min_eating_speed(piles,h):
#     low =0
#     high=max(piles)
#     answer = high
#     while low<=high:
#         mid = (low+high)//2 
#         hours=0
#         for pile in piles:
#             hours += (pile+mid-1)//2
#             if hours<=h:
#                 answer=mid
#                 high = mid-1
#             else:
#                 low = mid + 1
#     return answer
# piles = [3,6,7,11]
# h = 8   
# print(min_eating_speed(piles,h))


# def sort_color(arr):
#     low=0
#     mid=0
#     high=len(arr)-1
#     while mid<=high:
        
#         if arr[mid] == 0:
#             arr[low],arr[mid]=arr[mid],arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high -= 1
#     return arr
# arr = [2,0,2,1,1,0] 
# print(sort_color(arr))


# def sorted_array(arr):
#     low = 0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
        
#         else:
#             if arr[low] <= arr[mid]:
#                 if arr[low]<target<arr[mid]:
#                    high=mid-1
#                 else:
#                     low=mid+1
#             else:
#                 if arr[mid]<target<arr[high]:
#                     low=mid+1
#                 else:
#                     high=mid-1
#     return -1
# arr=[4,5,6,7,0,1,2]
# target=6
# print(sorted_array(arr))

