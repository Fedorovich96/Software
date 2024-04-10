memory = " world"
string = "hello"
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
    counter += 1
    if counter in values:
     print(string + memory)
    if counter not in values:
        print(string)
