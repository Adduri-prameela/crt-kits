n= int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(i):
        print(j % 2 == 0 and 1 or 0, end=" ")
    print()