
# Тема 7.Работа с файлами (ввод, вывод)  
Отчет по Теме #7 выполнил:
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

## Самостоятельная работа №7
### 1)Найдите в интернете любую статью (объем статьи не менее 200
слов), скопируйте ее содержимое в файл и напишите программу,
которая считает количество слов в текстовом файле и определит
самое часто встречающееся слово. Результатом выполнения задачи
будет: скриншот файла со статьей, листинг кода, и вывод в консоль,
в котором будет указана вся необходимая информация.


```python
from collections import Counter
import re

def count_words_and_find_most_frequent(file_path):
    with open(file_path, "r") as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        most_common_word, frequency = Counter(words).most_common(1)[0]

        return word_count, most_common_word, frequency

file_path = 'text.txt'
word_count, most_common_word, frequency = count_words_and_find_most_frequent(file_path)
print(f'Всего слов: {word_count}')
print(f'Самое часто встречающееся слово: "{most_common_word}" попадается {frequency} раз')
```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-1-1.png)
![Меню]((https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-1.png)


### 2)У вас появилась потребность в ведении книги расходов, по отрев
все существующие варианты вы пришли к выводу чт
ничего не
устраивает и нужно все делать самому. Напишите рограмму для
учета расходов. Программа должна позволять в ди ь информацию
о расходах, сохранять ее в файл и выводить с ществующие данные в
консоль. Ввод информации происходит чер консоль. Результатом
выполнения задачи будет: скриншот файл с учетом расходов,
листинг кода, и вывод в консоль, с де онстрацией
работоспособности программы.


```python
import json

def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("Введите описание расхода: ")
    amount = float(input("Введите сумму расхода: "))
    expenses.append({"description": description, "amount": amount})


def display_expenses(expenses):
    print("Текущие расходы:")
    for expense in expenses:
        print(f"Описание: {expense['description']}, Сумма: {expense['amount']}")


def main():
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    while True:
        print("\n1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses, filename)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-2.png)

### 3)Имеется файл input.txt с те том на латинице. Напишите программу,
которая выводит следующ
латинского алфавита; число слов; число строк.
Текст в файле:
татистику по тексту: количество букв
•
Beautiful is better th n u ly.
Explicit is better t an mplicit.
Simple is bette than complex.
Complex s etter than complicated.
•
Ожи емый результат:
Input e contains:
1
2
4
0 let ers
0 ords
lines


```python
def analyze_text(filename):
    letters = 0
    words = 0
    lines_count = 0

    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words += len(line.split())
            letters += sum(1 for char in line if char.isalpha())

    print(f"Input file contains:")
    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines_count} lines")

if __name__ == "__main__":
    analyze_text('input.txt')

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-3.png)

### 4)Напишите программу, которая получает на вход предложение,
выводит его в терминал, заменяя все запрещенные слова
звездочками * (количество звездочек равно количеству букв в
слове). Запрещенные слова, разделенные символом пробела,
хранятся в текстовом файле input.txt. Все слова в этом файле
записаны в нижнем регистре. Программа должна заменить
запрещенные слова, где бы они ни встречались, даже в середине
другого слова. Замена производится независимо от регистра: если
 
 
файл input.txt содержит запрещенное слово exam, то слова exam,
Exam, ExaM, EXAM и exAm должны быть заменены на ****.
•
Запрещенные слова:
hello email python the exam wor is
Предложение для проверки:
•
Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!
•
Ожидаемый результат:
*
*
*
****, ***ld! ****** ** *** programming language of *** f
**** **....
***** ** awesome!!!!


```python
from get_datetime import get_datetime
get_datetime()

import re

def load_banned_words(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def censor_text(text, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text

def main():
    banned_words = load_banned_words('input2.txt')
    sentence = ("Hello, world! Python IS the programming language of thE future. My "
                "EMAIL is.... PYTHON is awesome!!!!")
    censored_text = censor_text(sentence, banned_words)
    print(censored_text)

if __name__ == "__main__":
    main()





```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-4.png)

### 5)Самостоятельно придумайте и решите задачу, к тор я будет
взаимодействовать с текстовым файлом.

Создать текстовый файл tasks.txt, который будет хранить задачи.
Напишите скрипт на Python, который позволит пользователю:
Добавлять новые задачи.
Удалять задачи по номеру.
Просматривать все задачи.
Закончить работу с программой и сохранить изменения.


```python
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

```
### Результат.
![Меню](https://github.com/Fedorovich96/Software/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/7-5.png)
