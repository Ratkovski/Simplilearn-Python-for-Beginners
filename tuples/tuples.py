# what are tuples?
# tuple is collection of immutable heterogeneous python objects
emp = ()
print(type(emp))
print(emp)
city = "Pune",
print(type(city))
city = ("Pune")
print(city)
city = ("Pune",)
print(city)
city = ("Pune", "Bangalore", "Delhi", "Mumbai")
print(city)
city = "Pune", "Bangalore", "Delhi", "Mumbai"
print(city)

list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
list1.append(5)
print(list1)
# tuple has no attribute 'append'
# differences between tupes and list

# -> list is mutable whereas tuple is immutable
# -> list uses square brackets. Tuples may or may not use parentheses
print(city)
print(city[1])
print(city[-1])

# concatenation
print(city)
num = 1, 2, 3, 4
print(city + num)

# nesting
nest = (city, num)
print(nest)

# repetition
rep = ("Python",) * 5
print(rep)
rep = ("Python",)
print(rep * 10)
print(rep)

# slicing

print(num)
print(num[1:])
print(num[::-1])

# unpacking
print(tuple("simplilearn"))
print(num)
a, b, c, d = num
print(a, b, c, d)
a, *b, c = num
print(a, b, c)

# Deleting a tuple
tuple2 = (1, 2, 3, 3)
print(tuple2)
del tuple2
# print(tuple2)

# Built in functions
num1 = (3, 5, 2, 2, 2, 2, 6, 5, 8)
print(num1.count(2))
print(sum(num1))
print(len(num1))
print(max(num1))
print(min(num1))

# converting list to tuple
lst = [1, 2, 3, 4]
print(type(lst))
tpl = tuple(lst)
print(tpl)
print(type(tpl))

# Nesting tuples in a list

lst = [(1, 2, 3), (4, 5, 6)]
print(lst)
lst.append(("Tuple", "inside", "list"))
print(lst)
lst.remove((1, 2, 3))
print(lst)

# Nesting lists within tuples
tpl = (['a', 'b', 'c'], ['d', 'e', 'f'])
print(tpl)
tpl[0].append('z')
print(tpl)
tpl[0].remove('z')
print(tpl)
# tpl.append(['x','y','z']) # tuple object has no attribute 'append'
# print(tpl)
