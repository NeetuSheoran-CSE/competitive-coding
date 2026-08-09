#time complexity -- rate of increase in time with wrt input size

# for i in range (1,n+1):  #tc O(n)
#     print("Hello World")


#1. calculate tc always in terms of worst case
#2. avoid the constant value 
#3. avoid lower bound

age = int (input("enter the number:"))
if age >= 80:
    print("You are a super senior citizen")   #best case - O(1)
elif age >= 60 and age < 80:                  # worst case - O(5)
    print("You are a senior citizen")
elif age >= 16 and age < 24:
    print("You are a young adult")
else:
    print("Baby")


#best case - O(1) - when the first condition is true
# average case - O(n) - when the element is at the middle
# worst case - O(n) - when the element is at the end or 
#                      jb code ko subse jayda run hona pade 


# tc => O(8N^6 + 3N^2 + 15)
#    =>O(N^6 + 3M^2)  
# suppose you have N=10^5  so 15 and lower terms add hone ka koi effect nhi hoga 
# ignore the constant and lower order terms
#    => O(N^6) 
#
#
#different type od tc 
# big-O(o)-> worst case 
# tneta -> average case 
# omega -> best case

#for i in range (1,n+1):
#  for j in range (1,n+1):   O(n^2)

#example 2
#for i in range (1,n+1):
#  for j in range (1,i+1):
# 
# n(n+1)/2 => (N^2+n)/2= n^2/2+n/2 => O(n^2)
# n/2 is very small compared to n^2 so we ignore it and also 
# ignore the constant 1/2

#list =|7|9|1|3|2|5|6| 
# 1. append one element in last--> this is not depend on the size
#      1 element  directly add to the last O(1)
# 2. copy the above list --> list2=list.copy()
#      O(n) its depend on the length of the list
# 3. pop last element -->it not depend on the length of the list 
#    O(n)
# 4. pop intermediate[2]--> jub 2th element ko remove kare 
#    ga tb next elements aage shift hote jayege O(n)
# 5. insert--> O(n)  logic like pop intermediate 
# 6. get item-->O(1)
# 7. set item--> O(1)
# 8. delete item--> O(n) shifting hogi
# 9. iteration-->O(n) depend on list length
# 10. get slice--> slice like lst[2:5] slice kiye part ko k let 
# karlo O(k)
# 11. extend[1]-->O(k)
# 12. sort-->O(nlogn)

#****************************************************
# extration of digits 
# -count digits
# -reverse a number
# -check palinfrome
# - armstrong number

# n=5873
# while num > o:
#     last_digit = num%10
#     print(last_digit)
#     num=num//10

#how many integers in given value -- n=5873
# num = n 
# count = 0
# while num>0:
#     count +=1
#     num=num//10
#return count 


