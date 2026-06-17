'''
17. Replace Middle Digit with Zero
Write a program to replace the middle digit of a three-digit number with 0.
'''
num=int(input())
first=num//100
middle=0
last=num%10
replace=first*100+middle*10+last
print(replace)