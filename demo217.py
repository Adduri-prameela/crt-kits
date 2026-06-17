# Sum of Squares of Digits
'''
13.Write a program to calculate the sum of the squares of all digits in a three-digit number.
'''
num=input()
print(sum(int(d)**2 for d in num))