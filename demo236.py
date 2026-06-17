'''
32. Difference Between Sum and Product of Digits
Write a program to calculate the difference between the sum and product of digits.
'''
num=int(input())
digit_sum=0
product=1
while num!=0:
    digit=num%10
    digit_sum+=digit
    product*=digit
    num=num//10
print(digit_sum)
print(product)
print(f"Difference is {digit_sum-product}")
