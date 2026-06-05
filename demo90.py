std={
    101:'prams',102:'sandy',103:'kallu',104:'bunny',105:'harsha'
}
print(std)
std[106]='rolly'
print(std)
del std[101]
del std[106]
print(std)
#check 101,104,105
print(101 in std)
print(104 in std)
print(105 in std)
