'''
20. Move Last Digit to Front
Write a program to move the last digit of a four-digit number to the front.
'''
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
replace=last*100+first*10+middle
print(replace)
