'''
1
4 4
9 9 9
16 16 16 16
'''
n =int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(i):
        print(i * i, end=" ")
    print()