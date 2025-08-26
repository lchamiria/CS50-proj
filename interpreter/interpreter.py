x,y,z = input("Expression: ")
x = int(x)
z = int(z)
for y in x,y,z:
    if y == "+":
        return(x+z)
    elif y == "-":
        return(x-z)
    elif y == "*":
        return(x*z)
    elif y == "-":
        return(x/z)
    else:
        break

print(x,y,z)

