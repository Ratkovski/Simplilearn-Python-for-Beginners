num = 5
print(type(num))
num = 5.4
print(type(num))
num = 2 + 5j
print(type(num))
print(num.real)
print(num.imag)
num = -5647.675
print(num)
num1 = 10
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(10 / 3)
print(10 // 3)
print(num1 ** num2)
print(num1 % num2)
print(10 % 3)

# conversions

x = "192"
print(type(x))
int(x)
x = int(x)
print(type(x))
x = float(x)
print(x)
print(type(x))
x = complex(x)
print(x)
print(complex(2, 6))

# functions

x = -7.5
print(abs(x))
import math

x = 10
print(math.exp(x))
print(math.e)
print(math.pi)
print(math.sqrt(6))
print(max(1, 34, 4986, 3254, 687))
print(min(1, 34, 4986, 3254, 687))

# what are list?
# a list is a collection of data. it can hold values os multiple data types
# creating lists

num = [1, 2, 3, 4]
print(num)
letter = ['a', 'b', 'c', 'd']
print(letter)
stg = ["get", "certificate", "get", "ahead"]
print(stg)
mix = [1, 6, "Simplilearn", "get", "certified"]
print(mix)
mat = [[1, 2], ['a', 'b']]
print(mat)

# Accessing elements in lists
print(mix)
print(mix[3])
print(mix[-2])
print(mix[:3])
print(mix[3:])
print(mix[2:4])
print(mix[::2])
print(mix[::-1])

# operations list

z = [0] * 100
print(z)
print(letter)
print(stg)
conc = letter + stg
print(conc)
var = list("hey there")
print(var)
print(num)
one, *other = num
print(one)
print(other)

# methods in lists
print(num)
num.append(6)
print(num)
num.extend(stg)
print(num)
num.insert(5, "Simplilearn")
print(num)
num.remove("Simplilearn")
print(num)
var1 = ['b', 'f', 'a', 'q', 'r']
var1.sort()
print(var1)

# Built-in functions with lists

x = [9, 17, 14, 4, 9, 55]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sum(x) / len(x))
