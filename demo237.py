'''
33. Find Second Largest Digit
Write a program to find the second largest digit in a three-digit number.
'''
num=list(map(int,input().split()))
num1=sorted(num)
print("Second largest number is",num1[-2])
