class MyCustomException(Exception):
    def __init__(self, message="Это мое собственное исключение!"):
        self.message = message
        super().__init__(self.message)

# Фрагмент кода 1: Где исключение будет создаваться
def divide_numbers(a, b):
    if b == 0:
        raise MyCustomException("Попытка деления на ноль!")
    return a / b

try:
    result = divide_numbers(10, 0)
except MyCustomException as e:
    print(f"Произошло исключение: {e}")

# Фрагмент кода 2: Где исключение будет обработано
try:
    number = int(input("Введите число больше 10: "))
    if number <= 10:
        raise MyCustomException("Введено число меньше или равное 10!")
except MyCustomException as e:
    print(f"Произошло исключение: {e}")
