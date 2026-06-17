'''
2 4 6 8 
10 12 14 16
18 20 22 24 
26 28 30 32 
'''
n = int(input("Enter the number:"))
k = 2
for i in range(n):
    for j in range(n):
        print("{:2d}".format(k), end=" ")
        k += 2
    print()