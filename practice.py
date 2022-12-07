# lists : ordered, mutable, allows duplicate elements
list_org = ["banana", "cherry", "apple"]

# tuple : ordered, immutable, allows duplicate elements, often used for objects
# that belong together
myTuple = ('a', 'p', 'p', 'l', 'e')
print(len(myTuple))

# dictionary is key value pairs that is unordered and mutable
mydict = {3: 9, 6: 36, 9: 81}

# set: unordered, mutable, no duplicates
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.isdisjoint(setB))

# string: ordered, immutable, text representation

mystring = """hello \
world"""
print(mystring)

char = mystring[-1]
print(char)

substring = mystring[::-1]

# slicing operator:
#  Lst[start : end : index jump]

greeting = "whassup"

print(greeting.lower())

print(greeting.count("s"))

var = "Tom"
mystring = "the variable is %s" % var
print(mystring)
