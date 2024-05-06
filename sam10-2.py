def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("файл пустой")
            return content
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(e)

with open('empty_file.txt', 'w') as file:
    pass

with open('non_empty_file.txt', 'w') as file:
    file.write("Привет, мир!")

print(read_file_content('empty_file.txt'))

print(read_file_content('non_empty_file.txt'))
