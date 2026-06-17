'''
1 4 9 16
25 36 49 64
81 100 121 144
'''
n = int(input("Enter the number:"))
k = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k * k, end=" ")
        k += 1
    print()