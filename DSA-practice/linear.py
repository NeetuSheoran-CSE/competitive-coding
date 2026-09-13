#Write a function linear_search(arr, target) that 
# takes an unsorted list and a target value, and 
# returns the index of the target if found, or -1 
# if not found. Don't use Python's built-in in or .index().


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1 #not found
    
# arr = [4,2,7,1,9,3]
# target = 1

# result = linear_search(arr, target)
# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")
    
    
    
    
#2. Find All Occurrences
#Given a list that may contain duplicate 
# values, write a function that returns a list of 
# all indices where the target value occurs, using linear search.

# def occurance(arr, target):
#     indices = []
#     for i in range(len(arr)):
#         if arr[i]==target:
#             indices.append(i)
#     return indices 

# arr = [4,2,7,1,7,9,3,7]
# target = 7

# result = occurance(arr,target)
# if result:
#     print(f"Element found at indices: {result}")
# else:
#     print("element not found")
    
    
    
# 3. Basic Binary Search
#Write a function binary_search(arr, target) 
# that takes a sorted list and returns the index of 
# the target using the binary search algorithm (iterative, 
# not recursive). Return -1 if not found  

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = (low+high)//2
     
        if arr[mid]==target:
         return mid
        elif arr[mid]<target:
         low = mid+1
        else:
         high = mid-1
    
    return -1

arr = [1,3,4,5,6,7,8]
target =9

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")



arr = [10, 25, 7, 45, 32]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element:", largest)



arr = [10, 20, 30, 40, 50]

arr.reverse()

print("Reversed array:", arr)



stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop
element = stack.pop()

print("Deleted element:", element)
print("Stack after pop:", stack)



arr = [10, 20, 30, 40, 50]
key = 30

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
    


arr = [10, 20, 30, 40, 50, 60, 70]
key = 50

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index:", mid)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")