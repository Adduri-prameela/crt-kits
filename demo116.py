price=list(map(int,input('Enter the price :',).split()))
print([i for i in price if i>1000])