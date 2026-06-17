'''
1 3 5 7
1 3 5 7
1 3 5 7
1 3 5 7
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(1, 2 * n, 2):
        print(j, end=" ")
    print()
