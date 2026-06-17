'''
1 1 1 1
2 2 2
3 3
4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(i, end=" ")
    print()
'''
1 2 3 4
1 2 3
1 2
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
4 4 4 4
3 3 3
2 2
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
'''
4 3 2 1
4 3 2
4 3
4
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()