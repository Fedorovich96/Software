class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} ГАВ"

    def fetch(self, item):
        return f"{self.name} бежит за  {item}! "

# Создаем экземпляр класса Dog
my_dog = Dog("Шарик", 5)

# Вызываем методы экземпляра класса
print(my_dog.bark())
print(my_dog.fetch("кошкой"))
