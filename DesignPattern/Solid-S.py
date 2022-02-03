class Cat:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name

    def eat(self):
        print("eating...")
    
    def walk(self):
        print("walking...")

    def speak(self):
        print("meow~")
    
    # cat doesn't have printing or logging behavior
    # def print(self):
    #     print(f"name:{self.name}, age:{self.age}")

    # def log(self):
    #     logger.log(f"name:{self.name}, age:{self.age}")

    # Instead, use reprent behavior outside the cat
    def repr(self):
        return f"name:{self.name}, age:{self.age}"

kitty = Cat(3, "kitty")
print(kitty.repr())
#Logger.log(kitty.repr())