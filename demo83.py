a=[1,2,35,6,8,6,5,8,999,0,66]
print("original list: ", a)

a.append(5)
print("After append ", a)

a.insert(2,85)
print("After insert ", a)

a.remove(2)
print("After removal ", a)

a.pop()
print("After pop ", a)

a.pop(a.index(0))
print("After pop index of 0 ", a)

index_85=a.index(85)
print("index of 85: ", index_85)

count_2=a.count(2)
print("count of 2: ", count_2)

a.sort()
print("After sort: ", a)

a.reverse()
print("after reverse: ", a)

slice_ex=a[:5]
print("sliced firt 5 elements: ", slice_ex)

a.append(sum(a))
print("After appending sum: ", a)

a.append(max(a))
print("After append max value: ", a)

length= len(a)
print("Length of the list: ", length)

