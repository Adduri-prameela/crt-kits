#left triangle pattern
'''
      a
    b b
  c c c
d d d d
'''
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()

''' 
      a
    a b
  a b c     
a b c d 
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + j), end=" ")
    print()

'''
      d
    c c
  b b b
a a a a
'''
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + n - i - 1)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()
    
'''
      d   
    d c
  d c b
d c b a
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + n - j - 1), end=" ")
    print()

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