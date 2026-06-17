'''
18. Sum of Even Digits
Write a program to calculate the sum of all even digits in a three-digit number.
'''
num=int(input())
sum=0
while num!=0:
    digit=num%10
    if digit%2==0:
        sum+=digit
    num=num//10
print(f"Sum is {sum}")