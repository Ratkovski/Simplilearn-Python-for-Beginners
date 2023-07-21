# array is  a container that holds multiple values of the same type
from array import array

arr = array('i', [-1, 2, 3, 4, 5])
print(arr)
print(arr.buffer_info())
print(arr[2])

for i in arr:
    print(i)

for pnt in range(4):
    print(pnt, arr[pnt])

arr.reverse()
print(arr)

arr.append(10)
print(arr)

arr1 = array('i', [-1, 2, 2, 3, 4, 5])
arr1.remove(2)
print(arr1)

arr2 = array('i', [-1, 2, 3, 4, 5])
print(arr2[2])
print(arr2.index(2))

arr3 = array("i", [])
x = int(input("enter size of array"))
#print('enter %$d elements' %x)
print(arr3)


for i in range(x):
    n=int(input())
    arr.append(n)
print(arr)