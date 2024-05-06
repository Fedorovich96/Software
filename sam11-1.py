def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Генерируем числа Фибоначчи от 200 до 250
for number in fib(250):
    if number >= 200:
        print(number)
