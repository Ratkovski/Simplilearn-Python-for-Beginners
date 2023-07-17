# dictionary is an unotdered collection of data stored as a pair os key and value
# creating a dictionary

d1 = {}
print(d1)
print(type(d1))

d2 = {1: {"welcome"}, 2: {"to"}, 3: {"python"}, 4: {"tutorial"}}
print(d2)

d3 = {"name": "Sam", "age": 22, "profession": "student"}
print(d3)

d4 = dict({1: {"welcome"}, 2: {"to"}, 3: {"python"}, 4: {"tutorial"}})
print(d4)

d5 = dict([(1, "welcome"), (2, "to"), (3, "python"), (4, "tutorial")])
print(d5)

d6 = {"name": {"first": "Sam", "last": "creww"}, "age": 22, "profession": "student"}
print(d6)

# adding elements
d = {}
d[0] = "Welcome"
print(d)
d[1] = ("how", "are", "you")
print(d)
d["name"] = "Sam"
print(d)
d["name"] = {"first": "Sam", "last": "creww"}
print(d)

# Accessing elements
print(d)
print(d["name"])
print(d["name"]["first"])
print(d.get(1))

# Deleting elements
print(d)
print(d.pop(0))
print(d)
print(d.popitem())
print(d)

# using built in functions
print(d.values())
keys = {'a', 'b', 'c', 'd'}
value = 1
print(dict.fromkeys(keys, value))
print(d.clear())
print(d)
