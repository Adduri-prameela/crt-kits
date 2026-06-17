'''
30. Check if First and Last Digits are Same
Write a program to check whether the first and last digits are equal.
'''
num = int(input("Enter a number: "))
last = num % 10
first = num
while first >= 10:
    first = first // 10
if first==last:
    print("Same")
else:
    print("Not Same")

#sum of cubes
num=input()
print(sum(int(d)**3 for d in num))