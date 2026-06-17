'''23. Sum of First Two Digits
Write a program to find the sum of the first two digits of a three-digit number.
'''
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
print(f"sum is {first+middle}")
