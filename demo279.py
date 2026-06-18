#square pattern of alphabets
'''
A A A A
B B B B
C C C C
D D D D
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i), end=" ")
    print()

'''
D D D D
C C C C
B B B B
A A A A
'''
n=int(input('Enter the value:'))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(64+i), end=" ")
    print()

'''
A B C D
A B C D
A B C D
A B C D
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j), end=" ")
    print()

'''
A B C D
A B C D
A B C D
A B C D
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j), end=" ")
    print()

'''
D C B A
D C B A
D C B A
D C B A
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(chr(64+j), end=" ")
    print()

'''
a a a a
b b b b
c c c c
d d d d
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(96+i), end=" ")
    print()

'''
d d d d
c c c c
b b b b
a a a a
'''
n=int(input('Enter the value:'))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(96+i), end=" ")
    print()

'''
a b c d
a b c d
a b c d
a b c d
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(96+j), end=" ")
    print()

'''
d c b a
d c b a
d c b a
d c b a
'''
n=int(input('Enter the value:'))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(chr(96+j), end=" ")
    print()

