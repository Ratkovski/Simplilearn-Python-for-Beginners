# Set is unordered collection of unique elements

# Sets

s = set([1, 2, 3, 4])
print(s)
print(type(s))
s.add('a')
print(s)
fs = frozenset([1, 2, 3, 4])
print(fs)
# fs.add('b')  #AttributeError: 'frozenset' object has no attribute 'add'
s1 = set([1, 2, 3, 4])
s2 = set([5, 6, 7, 8])
print(s1.union(s2))
print(s1.difference(s2))
