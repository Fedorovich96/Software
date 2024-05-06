class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Гав-гав!"


class Labrador(Dog):
    def speak(self):
        return "Мяу"


class Poodle(Dog):
    def speak(self):
        return "Арррр "


# Функция для демонстрации полиморфизма
def let_dog_speak(dog):
    print(f"{dog.name}: {dog.speak()}")


# Создаем экземпляры разных пород собак
dog1 = Dog("Шарик")
dog2 = Labrador("Бобик")
dog3 = Poodle("Ника")

# Вызываем метод speak на разных экземплярах
let_dog_speak(dog1)
let_dog_speak(dog2)
let_dog_speak(dog3)
