#print all elements of a list
list1=[10,20,30,40,50]
for i in list1:
    print(i)

#find the sum of elements in a list
list1=[10,20,30,40,50]
total=0
for num in list1:
    total+=num

print("Sum:",total)

#find the largest number in a list
arr=[10,20,30,40,50]
max_num = arr[0]
for num in arr:
    if num<max_num:
        num=max_num
print("largest:",num)

#count even and odd numbers in a list
list=[1,2,3,4,5,6,7,8]
even=0
odd=0
for n in list:
    if n%2==0:
       even+=1
       
    else:
        odd+=1
print("Even:",even)
print("odd",odd)

#Reverse a list(without using reverse function)
arr=[10,20,30,40,50]
reversed_list=[]

for i in range(len(arr)-1,-1,-1):
    reversed_list.append(arr[i])

print("Reversed:",reversed_list)

#find second largest element
arr2=[12,23,43,21,22]
first=second=float('-inf')

for num in arr2:
   if num>first:
       second=first
       first=num
   elif num>second and num!=first:
       second=num

print("Second Largest:",second)

#check if list is sorted
arr=[10,20,30,40,50]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print("Sorted:",is_sorted)

#remove duplicates from list
arr=[1,2,3,3,5,6,7,8,9]
unique=[]
for num in arr:
    if num not in unique:
        unique.append(num)
print("without Duplicates:",unique)

#find frequency of each element.
arr=[1,2,2,3,3,3,4]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print("Frequency:",freq)

#Rotate list by k positions
arr=[1,2,3,4,5]
k=2
n=len(arr)
k=k%n
rotated=arr[-k:]=arr[:-k]
print("Rotated:",rotated)

