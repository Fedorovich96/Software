class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} говорит гав"

my_dog = Dog("Шарик", 5, "Дворняга")

# Взаимодействие с объектом
print(f"Кличка собаки {my_dog.name}.")
print(f"{my_dog.name},возраст {my_dog.age} лет.")
print(my_dog.bark())

