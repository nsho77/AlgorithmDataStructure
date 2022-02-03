class Cat:
    def speak(self):
        print("meow")

class BlackCat(Cat):
    def speak(self):
        print("black meow")

def speak(cat:Cat):
    cat.speak()


cat = Cat()
speak(cat)

class Fish(Cat):
    def speak(self):
        raise Exception("Fish cannot speak")

cat = Fish()
speak(cat)