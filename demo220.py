#check decreasing order
'''
16.Write a program to check whether the digits of a three-digit number are in decreasing order.
'''
num=list(map(int,input()))
n=True
for i in range(len(num)-1):
    if num[i]<=num[i+1]:
        n=False
        break
if n:
    print("Decreasing")
else:
    print("Not Decreasing")