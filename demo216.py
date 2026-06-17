#reverse and difference
'''
12.Write a program to reverse a three-digit number and find the absolute difference between the original and reversed number.
'''
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
reverse=last*100+middle*10+first
print(reverse-num)