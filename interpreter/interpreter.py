expression = input("Expression: ")
x = str("x")
y = "-", "+", "*", "/"
z = str("z")
x,y,z = expression.split(" ")
expression = float(x,y,z)

print(expression)
