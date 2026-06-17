'''
   * i=1,1
  *** i=2,3
 ***** i=3,5
******* i=4,7'''
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    flage=n-i
    stars=(2*i)-1
    print(" "*flage+"*"*stars)