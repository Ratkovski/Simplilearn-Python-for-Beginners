stg = "Simplilearn"
print(stg)
stg2 = "Tim's birthday"
print(stg2)
stg3 = 'Tim said,"I\'m busy today".'
print(stg3)
stg4 = '''hey there!
Welcome to Simplilearn'''
print(stg4)
print(len(stg))
print(stg[5])
for i in stg:
    print(i, end="")

print(stg[0:5])
print(stg[:5])
print(stg[5:])
print(stg[2:5])

stg5 = "Welcome to Simplilearn"
print(stg5.upper())
print(stg5.lower())
print(stg5.find('S'))
print(stg5.index('S'))
print(stg5.split(" "))
x = stg5.split(" ")
print(x)
print(stg5.replace("Simplilearn", "Python tutorial"))
print(stg5.rpartition(" to "))

stg6 = "good"
stg7 = "morning"
print(stg6 + " " + stg7)
stg8 = "{},{}".format(stg6, stg7)
print(stg8)
