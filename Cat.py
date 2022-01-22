class Cat:
    color = ''
    age = int
    name = ""

    def speak(self):
        print("meow")

    def print_cat(self):
        print(self.color)
        print(self.age)
        print(self.name)

if __name__ == '__main__':
    kitty = Cat()
    kitty.color = 'black'
    kitty.age = 2
    kitty.name = 'Noel'
    kitty.print_cat()
    print(kitty.color)
    kitty.speak()
    print(type(kitty))