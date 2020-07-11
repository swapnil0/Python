import Hashtable as a
import Model as m
#p.add("1","swapnil")
p=a.hashTable(100)
#p.add("1","ingale")
#p.add("1","ingale")

d=m.ApplicationRecord("swapnil","9834329141","1148","Passed")
#hashed = (hash(d) + i) % self.size
print(p.set(d,d))
print("after same key")
print(p.set(d,"swapnil"))
print(p)
print("after set")
print(p.get(d))
print(p.load())
