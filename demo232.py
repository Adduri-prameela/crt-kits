'''
28. Find Smallest Among Three Digits
Write a program to find the smallest digit in a three-digit number without using lists.
'''
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
digit=min(hun,tens,ones)
print(digit)