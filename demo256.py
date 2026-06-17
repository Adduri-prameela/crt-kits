'''
4 16 36 64
4 16 36 64
4 16 36 64
4 16 36 64
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(2, 2 * n + 1, 2):
        print(j * j, end=" ")
    print()