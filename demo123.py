prices=list(map(int,input('Enter the prices : ').split()))
print(sorted(sorted(prices,reverse=True))[:3])