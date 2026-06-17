'''
1 3 5 7
9 11 13 15
17 19 21 23 
25 27 29 31
'''
n = int(input("Enter the number:"))
k = 1
for i in range(n):
    for j in range(n):
        print(k, end=" ")
        k += 2
    print()