'''
    1 2 3 4
    5 6 7 8
    9 10 11 12
    '''
n  = int(input("Enter integer: "))
k = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k), end=" ")
        k += 1
    print()