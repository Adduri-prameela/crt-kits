#1 35 7911)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=2
    print()
