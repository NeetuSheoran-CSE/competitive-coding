# n=8

# for i in range(n):
#     print(i)

# for i in range(n):
#     for j in range(n):
#         print(i,j)

# i=1
# while i<n:
#     i=i*2


# for i in range(n):
#     for j in range(i):
#         print(i,j)

# for i in range(n):
#     print(i)
# for i in range(n):
#     print(j)

#o(n) is faster than o(n^2)

#time complexity of accessing element by index in array
#o(1) Array index access is constant time

#o(log n) Binary Search halves the array each time


#O(n) grows faster than O(log n)

#order(faster=>slowest)
# O(1)=> O(log n)=> O(n)=> O(n log n)=> O(n^2)
# n=20
# for i in range(n):
#     print(i)

# for j in range(5):
#     print(j)

# #O(n)

# for i in range(n):
#     for j in range(10):
#         print(i,j)
# #O(n^2)

# i=1
# while i<n:
#     print(i)
#     i=i+1
#     #O(n)

# i=n
# while i>0:
#  print(i)
#  i=i//2
#  #n=>n/2=>n/4=>n/8....
 

 # Given a number n, check whether it is even or odd.
 #  return true for even and false for odd
# def isEven(n):
#   rem=n%2
#   if rem==0:
#    return True
#   else:
#    return False
  
# if __name__=="__main__":
#  n=15
#  if isEven(n):
#   print("true")
#  else:
#   print("false")
  

# # the last bit of all odd numbers is always 1, while for
# #  even numbers it's 0. so, when performing bitwise AND 
# #operation with 1, odd numbers give 1,and even numbers 
# # give 0
# def isEven(n):
#  #taking bitwise and of n with 1
#  if(n&1)==0:
#   return True
#  else:
#   return False
 
# if __name__=="__main__":
#  n=15
#  if isEven(n):
#   print("true")
#  else:
#   print("false")

# #Given a number n, we need to print its table

# #iterative Approach
# def printTable(n):
#  for i in range(1,11):
#   #multiples from 1 to 10
#   print("%d*%d=%d"%(n,i,n*i))

# if __name__=="__main__":
#  n=5
#  printTable(n)

# #Recurive Approach
# def printTable(n,i=1):
#  if (i==11):
#   return
#  print(n,"*",i,"=",n*i)
#  i+=1
#  printTable(n,i)
# if __name__=="__main__":
#  n=5
#  printTable(n)         
    

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end='')
#     print()

# n=5 
# for i in range(n):
#     for j in range(i,n):
#        print('',end='')

#     for j in range(i+1):
#        print('*',end='')
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#      print('',end='')

#     for j in range(i,n):
#         print('*',end="")
#     print()
# i=2^6
# for (i=1;i<=n;i=2*i){
#     print(i)
# }