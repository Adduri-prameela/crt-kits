#downwards equalateral triangle pattern of alphabets

'''
# downward triangle of stars **** *** ** *
'''
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print("*", end=" ")
    print()

'''
d d d d
 c c c
  b b
   a
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(chr(100 - i), end=" ")
    print()

'''
a b c d
 a b c
  a b 
   a
'''
n= int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(chr(97 + j), end=" ")
    print()

'''
a a a a
 b b b 
  c c
   d
'''
n= int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(chr(97 + i), end=" ")
    print()

'''
d c b a
 d c b
  c b
   d
'''
n= int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(chr(100 - j), end=" ")
    print()

#42.downward  equalateral triangle of stars DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(68 - i), end=" ")
    print()

#43.downward  equalateral triangle of stars ABCD ABC AB A
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()

#44.downward  equalateral triangle of stars AAAA BBB CC D
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(65 + i), end=" ")
    print()

#45.downward  equalateral triangle of stars DCBA DCB DC D
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(68 - j), end=" ")
    print()