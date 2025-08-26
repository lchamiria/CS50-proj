x,y,z = input("Expression: ")
x = int(x)
z = int(z)
for y in x,y,z:
    if y == "+":
        print(x+z)
    elif y == "-":
        print(x-z)
    elif y == "*":
        print(x*z)
    elif y == "-":
        print(x/z)
    else:
        break

print(x,y,z)

