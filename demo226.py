'''
22. Check Strong Number
Write a program to check whether a number is a Strong Number. A Strong Number is equal to the sum of the factorials of its digits.
'''
num = input()
total = 0
for digit in num:
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    total += fact
if total == int(num):
    print("Strong Number")
else:
    print("Not a Strong Number")