x,y,z = input("Expression: ")
x = float(int(x))
z = float(int(z))

match y:
    case "/":
        print(x/z)
    case "*":
        print(x*z)
    case "-":
        print(x-z)
    case "+":
        print(x+z)
