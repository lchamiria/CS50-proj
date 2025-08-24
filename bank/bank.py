greeting = input("greeting: ").title()
greeting = greeting.count(greeting)
def greetings():
    for char in greeting:
        if greeting.startswith("Hello"):
            print("$0")
        elif greeting.startswith("H"):
            print("$20")
        else:
            print("$100")

greetings()


