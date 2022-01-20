# This is my first Python assignment
def collect_info():
    print("Hello user, please enter your information")

    name = input("Enter your name: ")

    address = input("Enter your address: ")

    phone = input("Enter your phone number: ")

    print(f"Your name is {name}")

    print(f"Your address is {address}")

    print(f"Your phone number is {phone}")

if __name__ == "__main__":
    loop_control = True
    while loop_control == True:
        collect_info()
        print("Is your information correct?")
        response = input("Type yes to exit")
        if response == 'yes':
            loop_control = False


# if __name__ == "__main__":
#     loop_control_variable = True
#     while loop_control_variable == True:
#         print("I am looping")
#         response = input("Type 1 to exit this loop")
#         if response == '1':
#             loop_control_variable = False
#     # main()