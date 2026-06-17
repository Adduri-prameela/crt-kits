'''35.
1 1 1 1
4 4 4
9 9
16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(i * i, end=" ")
    print()
'''36.
1 4 9 16
1 4 9
1 4 
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j * j, end=" ")
    print()
'''37.
16 16 16 16
9 9 9 
4 4
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print(i * i, end=" ")
    print()
'''38.
16 9 4 1
16 9 4 
16 9 
16
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j * j, end=" ")
    print()
'''39.
      *
    * *
  * * *
* * * *
'''
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
'''40.
      1
    1 2
  1 2 3
1 2 3 4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''41.
      1
    2 2
  3 3 3
4 4 4 4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(i, end=" ")
    print()
'''42.
       1
     2 3 
   4 5 6
7 8 9 10
'''
n = int(input("Enter the number: "))
k = 1
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()
'''43. 
       1
     1 4
   1 4 9
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j * j, end=" ")
    print()
'''44.
          1 
        4 4 
      9 9 9
16 16 16 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(i * i, end=" ")
    print()
'''45.
          1
       4 9
   16 25 36
49 64 81 100 
'''
n = int(input("Enter the number:"))
k = 1
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(k * k, end=" ")
        k += 1
    print()

'''# equalateral triangle of *'''
n=int(input("Enter a number:"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

'''# equalatral triangle of 1234'''
n=int(input("Enter a number:"))
k=1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()

'''#equalateral triangel of 1 22 333 444'''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end=" ")
        else:
            print(" ",end="")
    print()

'''#equalateral triangle of 1 2 3 4'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    k=1
    for j in range(n,0,-1):
        if j<=i:
            print(k,end=" ")
            k+=1
        else:
            print(" ", end="")
    print()

'''#equalateral triangle of 1 00 111 0000'''
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()

'''#equalateral triangle of 1 10 101 1010'''
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()

'''#equalateral triangle of 1 ** 111 ****'''
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print("*",end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()

'''#equalateral triangle of * 11 *** 1111'''
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print(1,end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ", end="")
    print()

