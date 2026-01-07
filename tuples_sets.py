alphabet = ("a","b","c","d")
print(alphabet[1])
x,y,d = (1,2,3)
print(x,y,d)

alphabet = {"a","b","c","d","e","e"}
print(alphabet)

for i in alphabet:
    print(i)

alphabet.add("g")
print(alphabet)
alphabet.remove("c")
print(alphabet)

set1 = {"a","b","c","d"}
set2 = {"a","e","f","d"}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
