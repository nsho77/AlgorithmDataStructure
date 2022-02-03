# low level에 의존
class Cat:
    def speak(self):
        print("meow")

class Dog:
    def speak(self):
        print("bark")


#Zoo depdns on Cat and Dog
class Zoo:
    def __init__(self):
        self.dog = Dog()
        self.cat = Cat()

    def speakAll(self):
        self.cat.speak()
        self.dog.speak()


zoo = Zoo()
zoo.speakAll()

# Dependency Inversion pattern
class Animal: #abstract module
    def speak(self): #interface method
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")


#Zoo depends on Animal.   (Not Cat, Not Dog)
class Zoo:
    def __init__(self):
        self.animals = []

    def addAnimal(self,animal):
        self.animals.append(animal)
  
    def speakAll(self):
        for animal in self.animals:
            animal.speak()

zoo = Zoo()
zoo.addAnimal(Cat())
zoo.addAnimal(Dog())
zoo.speakAll()