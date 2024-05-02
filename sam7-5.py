def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        file.writelines(task + '\n' for task in tasks if task.strip())


def display_tasks(tasks):
    if tasks:
        print("Список задач:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
    else:
        print("Список задач пуст.")


def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
            print("Задача удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")


def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\n1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Показать все задачи")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Изменения сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
