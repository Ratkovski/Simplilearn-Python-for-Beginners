# python allows loops to be nested in loops. Nested loops could be:
# for in for
# for in while
# while in while
# while in for

# matrix

x = [[1, 2, 3], ["a", "b", "c"]]
for i in x:
    for j in i:
        print(j, end="")
    print()
