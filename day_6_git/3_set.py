# Set is also an iterable (Sequece of elements) in python like and string
#Set element are enclosed in curly braces{}
# set us a mutable datatype but the elements of the set must be immutiable

# Creating set in python
a = set() # empty set

b = {1, 2, 3}
vowels = {"a", "e", "i", "o", "u"}

data = {"a", 1, 2.1}  # set can have mixed datatypes.

c = {1, 2.1, ["a", "b"]}  # Invalid set. It raises error


# Unlike list, set doesn't support indexing and slicing because set is unordered
d = {1, 2}
e = {2, 1}
print(d == e)  # True


#adding and removing set elements
s1 = {1,2,3,4}
s1.add(5)
print(s1)#{1,2,3,4,5}

s1.update([5, 6, 7, 8])
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}


print(set([1, 3, 2, 1, 2, 3]))

# To remove
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s1.remove(5)
print(s1)  # {1, 2, 3, 4, 6, 7, 8}

# s1.remove(10)  # It raises error

s1.discard(10)  # It doesn't raise error
s1.discard(1)  # {2, 3, 4, 6, 7, 8}

s1.pop()
print(s1)  # {2, 3, 4, 6, 7}

s1.clear()
print(s1)  # set()