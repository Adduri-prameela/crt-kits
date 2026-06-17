'''
31. Sum of Cubes of Digits
Write a program to find the sum of cubes of all digits in a three-digit number.
'''
num=input()
print(sum(int(d)**3 for d in num))