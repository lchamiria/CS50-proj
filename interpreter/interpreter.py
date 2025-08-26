expression = input("Expression: ")
x,y,z = expression.split(" ")
x = str("x")
y = "-", "+", "*", "/"
z = str("z")
expression = float(x,y,z)

print(expression)
