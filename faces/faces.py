def main():
    user_input = input()
    converted = convert(user_input)
    return converted

def convert(user_input):
    converted = user_input.replace(":)", "🙂").replace(":(", "🙁")
    print(converted)


main()

