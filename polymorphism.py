#polymorphism

class Animal():

    def sound(self):
        return "Animal sound"

class Dog(Animal):

    def sound(self):
        return "Dog will bark"
    
    def typeofAnimal(self):
        return "This is a 4 legged Animal"

class Cat(Dog,Animal):

    def sound(self):
        return "Cat Says Meow"


class Human(Animal):

    def sound(self):
        return "Human Speaks"
    pass

"""
cat_Instance=Cat()
print(cat_Instance.sound())
print(cat_Instance.typeofAnimal())
"""
human=Human()
print(human.sound())