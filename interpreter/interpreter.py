x,y,z = input("Expression: ")
x = int(x)
z = int(z)
match y:
    case "-":
        print(float(x-z))
    case "+":
        print(float(x+z))
    case "*":
        print(float(x*z))
    case "/":
        print(float(x/z))
