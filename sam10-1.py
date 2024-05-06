import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {elapsed_time:.6f} секунд")
        return result
    return wrapper

@timing_decorator
def calculate_sum(n):
    return sum(range(1, n + 1))

print(calculate_sum(1000000))

