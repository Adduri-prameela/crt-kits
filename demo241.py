n = int(input("Enter a value: "))

for i in range(1, n + 1):
    if i % 2 == 1:
        print((str(i) + " ") * i)
    else:
        print(("* " ) * i)