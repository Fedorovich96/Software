  def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным!")
        else:
            self._age = age


# Пример использования класса Dog
my_dog = Dog("Шарик", 5)
print(f"Имя собаки: {my_dog.get_name()}, Возраст собаки: {my_dog.get_age()}")

my_dog.set_age(-2)
my_dog.set_age(3)
my_dog.set_name("Бобик")
print(f"Имя собаки: {my_dog.get_name()}, Возраст собаки: {my_dog.get_age()}")
