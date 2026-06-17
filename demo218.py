#Product of First and Last Digit
'''
14.Write a program to find the product of the first and last digit of a three-digit number.
'''
num=input("Enter a number: ")
first=int(num[0])
last=int(num[-1])
print(f"product={first*last}")