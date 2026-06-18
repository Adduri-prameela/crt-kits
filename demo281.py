#equalateral traiangle pattern
'''
   a  
  b b
 c c c
d d d d
'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + i), end=" ")
    print()

'''
   a  
  a b
 a b c
a b c d
'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + j), end=" ")
    print()

'''
   d  
  c c
 b b b
a a a a
'''
n = int(input("Enter a number: "))
for i in range(n):
    print(' '*(n-i-1) + (chr(96+n-i)+' ')*(i+1))

'''
    d
   d c
  d c b
 d c b a
'''
n = int(input("Enter a number: "))
for i in range(n):
    print(' '*(n-i-1) + ' '.join(chr(100-j) for j in range(i+1)))

#29.Equalateral triangle of alphabet A BB CCC DDDD
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")
    print()
    
#30.Equalateral triangle of alphabet A A B  A B C  A B C D
n = int(input("Enter a number: "))  
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

#31.Equalateral triangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))  
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()

#32.Equalateral triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()