# Open Closed principle 준수하지 않는 Animal
class Animal():
    def __init__(self, type) -> None:
        self.type = type

def hey(animal: Animal):
    if animal.type == 'Cat':
        print('meow')
    elif animal.type == 'Dog':
        print('bark')
    
bingo = Animal('Dog')
kitty = Animal('Cat')

# Cow와 Sheep을 추가하기 위해 hey 함수 수정이 필요
hey(bingo)
hey(kitty)


# 상속을 이용한 Animal class. 추가되는 동물에 대해 hey함수의 수정을 필요로 하지 않는다.
class Animal:
    def speak(self): # interface method
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")

class Sheep(Animal):
    def speak(self):
        print("meh")

class Cow(Animal):
    def speak(self):
        print("moo")

def hey(animal: Animal):
    animal.speak();

bingo = Dog()
kitty = Cat()
sheep = Sheep()
cow = Cow()

hey(bingo)
hey(kitty)
hey(sheep)
hey(cow)