'''
21. Check Armstrong Number (3 Digits)
Write a program to check whether a three-digit number is an Armstrong number.
'''
num=int(input())
c=num
n=len(str(num))
a=0
while c>0:
    digit=c%10
    a=a+digit**n
    c=c//10
if num==a:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
