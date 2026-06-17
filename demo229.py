'''
25. Check if Sum of Digits is Even
Write a program to check whether the sum of all digits is even or odd.
'''
num=int(input("Enter a number: "))
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
if sum%2==0:
    print("Sum is Even")
else:
    print("Sum is not even")