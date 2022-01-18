# This is my first Python assignment
print("Hello user, please enter your information")

name = input("Enter your name: ")

address = input("Enter your address: ")

phone = input("Enter your phone number: ")

print(f"Your name is {name}")

print(f"Your address is {address}")

print(f"Your phone number is {phone}")

def main() -> object:
    while True:
        again = input("Is your information correct? Enter yes or no: ")

        if again == "no":
            print ("Please try again")
            return
        elif again == "yes":
            print ("Thank you for your information")
            exit()
        else:
            print ("You should enter either \"yes\" or \"no\".")


if __name__ == "__main__":
    main()



