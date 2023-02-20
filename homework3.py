s1 = {2,3,4,5,6,7,8,9,10}
s1 = list(s1)
s1.remove(9)
s1.remove(10)
s1.remove(3)
s1.remove(5)
s1.insert(0,5)
s1.insert(1,4)
s1.insert(2,6)
s1.insert(3,7)
print(s1)
print(s1[3:6])
s1 = set(s1)
print(s1)
del s1
a1 = "this job is very tough"
s2 = a1.split()
print(s2)
