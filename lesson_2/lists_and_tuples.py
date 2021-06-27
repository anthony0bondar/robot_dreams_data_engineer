l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}


print(l[0])
print(t[0])
#print(s[0]) # не работает

l[0] = "Smith"
print(l)

l.append("Joe")
l.extend(["Barbara", "Robin"])
print(l)

s.add("Bob")
s.add("joe")
print(s)




# Advanced Set operations
print("------")
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local = friends.difference(abroad)
print(local)
local = friends.difference(abroad)

friends = local.union(abroad)
print(friends)


python = {"Bob", "Jen", "Rolf", "Charlie"}
scala = {"Bob", "Jen", "Adam", "Anne"}

both = python.intersection(scala)
print(both)

one = python.symmetric_difference(scala)
print(one)

print("-"*10 + "slice notation" + 10*"-")
# Slice notation
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

l = "1 2 3 4 5 6 7 8 9 10".split(' ')
l = [int(x) for x in l]
#l[start:end:step]
print(l[5:])

