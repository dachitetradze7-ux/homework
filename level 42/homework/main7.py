user_input = input("type number: ")
try:
    number = int(user_input)
    print("you typed correctly:", number)
except ValueError:
    print("incorrect: type only numbers")