# why should we use Numpy arrays when we have Python list? fast, convenient, less memory
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a[0])
print(a[1])
import time
import sys

b = range(1000)
print(sys.getsizeof(5) * len(b))

c = np.arange(1000)
print(c.size * c.itemsize)

size = 100000

L1 = range(size)
L2 = range(size)
A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()
result_list = [(x + y) for x, y in zip(L1, L2)]
# print(result)
print("python list took:", (time.time() - start * 1000))

start = time.time()
result_array = A1 + A2
print("python array took:", (time.time() - start * 1000))

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.ndim)
print(a.itemsize)
print(a.shape)
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print(a)
print(a.itemsize)
print(a.shape)
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print(a)

print(np.zeros((3, 4)))
print(np.ones((3, 4)))
l = range(5)
print(l)
print(np.arange(5))
print("covatenation exampel")
print(np.char.add(['hello', 'hi'], ['abc', 'xyz']))
print(np.char.multiply('hello', 3))
print(np.char.center('hello', 20, fillchar='-'))
print(np.char.capitalize('hello world'))
print(np.char.title('how are you?'))
print(np.char.lower(['HELLO', 'HELLO']))
print(np.char.lower('HELLO'))
print(np.char.upper(['python', 'data']))
print(np.char.upper('python is easy'))
print(np.char.split('are you coming to the party'))
print(np.char.splitlines('hello\nhow are you?'))
print(np.char.strip(['nina', 'admin', 'anaita'], 'a'))
print(np.char.join([':', '-'], ['dmy', 'ymd']))
print(np.char.replace('He is a good dancer', 'is', 'was'))
