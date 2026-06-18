#21.left angletriangle of alphabet A BB CCC DDDD
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(65 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):         
        
        print(ch, end=" ")
    print()

#22.left angletriangle of alphabet A A B  A B C  A B C D
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

#23.left angletriangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(65 + n - i - 1)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()
    
#24.left angletriangle of alphabet D DC DCB DCBA
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + n - j - 1), end=" ")
    print()