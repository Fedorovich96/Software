
# Тема 8.Основы объектно-ориентированного программирования  
Отчет по Теме #8 выполнил:
- Погребняк Кирилл Федорович
- ИНО ОЗБ ПОАС 22-2

| Задание  | Сам_раб |
| ------ | ------ |
| Задание 1 | + | 
| Задание 2 | + | 
| Задание 3 | + | 
| Задание 4 | + | 
| Задание 5 | + | 



знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №8
### 1) Самостоятельно создайте класс и его объект. Они должны
отличаться, от тех, что указаны в теоретическом материале
(методичке) и лабораторных заданиях. Результатом выполнения
задания будет листинг кода и получившийся вывод консоли.


```python
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


```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/8-1.png)

### 2)Самостоятельно создайте атрибуты и методы для ранее созданного
класса. Они должны отличаться, от тех, что указаны в
теоретическом материале (методичке) и лабораторных ада иях.
Результатом выполнения задания будет листинг код
получившийся вывод консоли.


```python
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


```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/8-2.png)

### 3)Самостоятельно реализуйте наследование, прод жая работать с
ранее созданным классом. Оно должно отлич ься, от того, что
указано в теоретическом материале (мет ди ) и лабораторных
заданиях. Результатом выполнения адани будет листинг кода и
получившийся вывод консоли.


```python
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

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/8-3.png)

### 4)Самостоятельно реализуйте инкапсуляцию, продолжая работать с
ранее созданным классом.
а должна отличаться, от того, что
указана в теоретическом м риале (методичке) и лабораторных
заданиях. Результатом выпо нения задания будет листинг кода и
получившийся вывод онсоли


```python
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

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/8-4.png)

### 5)Самостоятельно реализуйте полиморфизм. Он должен отличаться,
от того, что указ н в теоретическом материале (методичке) и
лабораторных аданиях. Результатом выполнения задания будет
листинг о и получившийся вывод консоли.


```python
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

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/8-5.png)

