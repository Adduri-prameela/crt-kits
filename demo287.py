#combinations of numbers and stars of square pattern
'''1 * * *
   2 3 * *
   3 3 3 *
   4 4 4 4
'''
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
             print(i, end=" ")
        else:
             print("*", end=" ")
    print()
print("--------------------------------")

'''
1 * * *
1 2 * * 
1 2 3 *
1 2 3 4
'''
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
             print(j, end=" ")
        else:
             print("*", end=" ")
    print()
print("--------------------------------")


#equalateral triangle pattern of alphabets

'''
     a
    bbb
   ccccc
  ddddddd
'''
n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    print(chr(97 + i) * (2 * i + 1))
print("--------------------------------")


'''
     a
    aba
   abcbc
  abcdcba
'''
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(97 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(97 + j), end="")
    print()
print("----------------------")