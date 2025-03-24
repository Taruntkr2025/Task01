from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name,species):
        self.name= name
        self.species= species

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def __init__(self, name,breed):
        super().__init__(name, "Dog")
        self.breed=breed
    
    def get_details(self):
        return f"{self.name} is a {self.species} with {self.breed} as a breed"

    def speak(self):
        return "Dog barks"

Dog_instance=Dog("Tommy","Pomarian")

print(Dog_instance.get_details())