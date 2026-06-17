'''
24. Product of Last Two Digits
Write a program to find the product of the last two digits of a three-digit number.
'''
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
print(f"Product is {middle*last}")
