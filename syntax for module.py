import array
a=array.array('i',[1,2,3,4,5,4])
a.append(7)
print("After append:", a)
a.insert(2,6)
print("After insert:", a)
a.pop(1)
print("After pop:", a)
b=a.index(4)
print("Index of 4:",b)
a.reverse()
print("After reverse:", a)
c=a.count(4)
print(c)
