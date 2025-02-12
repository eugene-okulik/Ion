pc_number = 64

while True:
    user_input = int(input(" Enter a number: "))
    if user_input != pc_number:
        print("Try again")
    elif user_input == pc_number:
        print("you guess the number!!!")
        break
