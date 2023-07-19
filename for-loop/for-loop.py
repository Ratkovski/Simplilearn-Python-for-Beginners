# for loop is used to interate over a sequence, which could be a list, tuple, array or string
x = ["Simplilearn"]

for i in x:
    print(i, end="")

sum = 0
for i in range(0, 21):
    if i % 2 == 0:
        sum = sum + i
print(sum)

# 1
# 12
# 123
# 1234
# 12345


n = int(input("enter a number"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

r = int(input("enter a number of rows"))
c = int(input("enter a number of colomns"))
x = []
val = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input("enter the %d * %d element" % (i, j))))
    x.insert(i, val)
    val = []

y = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input("enter the %d * %d element" % (i, j))))
    y.insert(i, val)
    val = []


sum = []

for i in range(0, r):
    for j in range(0, c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i, val)
    val = []
print(sum)