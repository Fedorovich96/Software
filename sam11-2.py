from get_datetime import get_datetime
get_datetime()

def fib(n, filename='fib.txt'):
    a, b = 1, 1
    with open(filename, 'w') as file:
        for _ in range(n):
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b

fib_generator = fib(200)
list(fib_generator)
