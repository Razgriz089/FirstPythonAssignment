def excise_one():
    value = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
    print(value)

def first_name_last_name():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")

    print(last_name + " " + first_name)

def display_colors():
    color_list = ["Red", "Green", "White", "Black"]

    #print(color_list[3])
    #print(color_list[0])
    print(color_list[0] + " , " + color_list[3])

def numbers_greater(num1):
    if num1 > 900 and num1 < 1100 or num1 > 1900 and num1 < 2100:
        print("it's all good")
    else:
        print("Wrong!")



if __name__ == '__main__':
    #excise_one()
    #first_name_last_name()
    #display_colors()
    numbers_greater(990)