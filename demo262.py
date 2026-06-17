#2 46 81012
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=2
    print()
