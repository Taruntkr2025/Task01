#polymorphism

class Animal():
    def sound(self):
        return "Animal sound"

class Dog(Animal):
    def sound(self):
        return "Dog will bark"

class cat(Animal):
    def sound(self):
        return "Cat Says Meow"

class Human(Animal):
    pass

cat_Instance=cat()
print(cat_Instance.sound())