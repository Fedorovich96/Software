def add_two_and_user_input():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения  {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two_and_user_input()
add_two_and_user_input()
add_two_and_user_input()
