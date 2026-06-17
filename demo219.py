# Check Increasing Digits
'''
15.Write a program to check whether the digits of a three-digit number are in increasing order.
'''
num=list(map(int,input()))
n=True
for i in range(len(num)-1):
    if num[i]>=num[i+1]:
        n=False
        break
if n:
    print("Increasing")
else:
    print("Not Increasing")