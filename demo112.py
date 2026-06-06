n=7
Revenue=[]
for i in range(n):
    ele=int(input(f"Enter the revenue for day {i+1} :"))
    Revenue.append(ele)
print(f"Total Revenue :{sum(Revenue)} | best Day :{max(Revenue)} | worst Day :{min(Revenue)}")