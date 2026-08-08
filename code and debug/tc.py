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

#sc --





