Revenue=list(map(int,input("Enter the Revenue for 7 days :").split()))
print(f"Total Revenue :{sum(Revenue)} | best Day :{max(Revenue)} | worst Day :{min(Revenue)}")