#(1 23 456 78910)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=1
    print()
