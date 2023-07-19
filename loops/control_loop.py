# loop control statements alter the regular flow of a loop
# break: transfers control to the statement right after the loop

# continue: skips the statements following it and returns control to the beginning of the loops

x = "Hey there . how are you?"
for i in x:
    if i == ".":
        break
    print(i, end="")

for i in [1, 13, 56, 4, 6]:
    if i > 10:
        continue
    print(i)
