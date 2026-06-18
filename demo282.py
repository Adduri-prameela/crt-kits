#right angle triangle pattern of alphabets
'''
A
B B
C C C 
D D D D
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i), end=" ")
    print()

'''
A 
A B 
A B C
A B C D
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print()

'''
D
C C
B B B
A A A A
'''
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(68 - i)  
    for j in range(i + 1):
        print(ch, end=" ")
    print()

'''
D
D C
D C B
D C B A
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()

'''
a
b b
c c c
d d d d
'''
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + i)  
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
    ch = chr(100 - i)  
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
    for j in range(i + 1):
        print(chr(100 - j), end=" ")
    print()

