a = 60
if a > 50:
    print("This is the if body")
print("This is outside the if block")

# if else statements

i = 20
if i % 2 == 0:
    print("This is the if block")
    print("i is an even number")
else:
    print("This is the else block")
    print("i is an odd number")

# nested if statements

c = 50
if c < 25:
    if c % 2 == 0:
        print("c is a even number lenss than 25")
    else:
        print("c is a odd number lenss than 25")
else:
    print("c is greater than 25")

# if-elif-else ladder

var = "z"
if var == 'a':
    print("This is the vowel a")
elif var == 'e':
    print("This is the vowel e")
elif var == 'i':
    print("This is the vowel i")
elif var == 'o':
    print("This is the vowel o")
elif var == 'u':
    print("This is the vowel u")
else:
    print("This is a consonant")
