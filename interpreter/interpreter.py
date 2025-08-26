x,y,z = input("Expression: ")
x = int(x)
z = int(z)
match y:
    case "-":
        print(x-z)
    case "+":
        print(x+z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)
