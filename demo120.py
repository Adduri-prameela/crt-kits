Godown_A =list(map(str,input('Enter the product codes : ').split()))
Godown_B =list(map(str,input('Enter the product codes : ').split()))
print('Unified Inventory : ',set(Godown_A + Godown_B)) 
print("True count: ",len(Godown_A + Godown_B))