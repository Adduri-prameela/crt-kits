'''
1 4 9 16
1 4 9 16 
1 4 9 16
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(1, n + 1):
        print(j * j, end=" ")
    print()
