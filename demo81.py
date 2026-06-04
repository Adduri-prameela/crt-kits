#shallow copy
import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=100
print(original)
print(new)

#deep copy
import copy
original=[1,2,3,4,5]
print(original)
new2=copy.deepcopy(original)
new2[0]=200
print(original)
print(new2)