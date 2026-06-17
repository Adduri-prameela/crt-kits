'''
26. Check if Product of Digits is Greater Than 100
Write a program to check whether the product of all digits is greater than 100.
'''
num=int(input("Enter a Number: "))
product=1
while num!=0:
    digit=num%10
    product*=digit
    num=num//10
if product>100:
    print("Product is greater than 100")
else:
    print("Product is not greater than+  100")
