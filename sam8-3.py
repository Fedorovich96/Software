class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я животное"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "ГАВ"

    def wag_tail(self):
        return "Виляет хвостом"


animal = Animal("Some animal")
print(animal.speak()) 

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())
print(dog.wag_tail())
