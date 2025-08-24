greeting = input("greeting: ")
def greetings():
    for char in greeting:
        if greeting.startswith("Hello"):
            print("$0")
        elif greeting.startswith("H"):
            print("$20")
        else:
            print("$100")

print(greetings)


