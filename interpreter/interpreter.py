x,y,z = input("Expression: ")
x,y,z = x,y,z.split()
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
        print(f"{x+z}")
