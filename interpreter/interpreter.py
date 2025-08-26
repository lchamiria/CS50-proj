x,y,z = input("Expression: ").split()
x = int(x)
z = int(z)
match y:
    case "/":
        print(f"{x/z}")
    case "*":
        print(f"{x*z}")
    case "-":
        print(f"{x-z}")
    case "+":
        print(x+z)
