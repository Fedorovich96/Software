
class LoggingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(" Выполняется функция:", self.func.__name__)
        result = self.func(*args, **kwargs)
        print(" Функция выполнена:", self.func.__name__)
        return result


@LoggingDecorator
def add(a, b):
    return a + b


@LoggingDecorator
def subtract(a, b):
    return a - b


result_add = add(5, 3)
print("Результат сложения:", result_add)

result_subtract = subtract(10, 4)
print("Результат вычитания:", result_subtract)
