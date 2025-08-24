greeting = input("greeting: ")
def greeting():
    for char in greeting:
        if greeting.startswith("Hello"):
            return "$0"
        elif greeting.startswith("H"):
            return "$20"
        else:
            return "$100"

