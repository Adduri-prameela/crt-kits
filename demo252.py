'''
2 4 6 8
2 4 6 8
2 4 6 8
2 4 6 8
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(2, 2 * n + 1, 2):
        print(j, end=" ")
    print()