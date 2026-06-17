'''
1 9 25 49
1 9 25 49
1 9 25 49
1 9 25 49
'''
n=int(input("Enter a number: "))
for i in range(1,n+1):
    k=1
    for j in range(1,n+1):
        print("{:2d}".format(k*k),end=" ")
        k+=2
    print()