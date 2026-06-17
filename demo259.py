'''
1 
1 4 
1 4 9 
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j * j, end=" ")
    print()