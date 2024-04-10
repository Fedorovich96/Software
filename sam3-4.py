predlojenie = input("Введите предложение на английском: ")

print(f"Длина предложения: {len(predlojenie)}")

predlojenie_lower = predlojenie.lower()
print(f"Предложение в нижнем регистре: {predlojenie_lower}")

vowels = 'aeiou'
count_vowels = sum(1 for char in predlojenie_lower if char in vowels)
print(f"Количество гласных в предложении: {count_vowels}")

new_predlojenie = predlojenie.replace("ugly","beauty")
print(f"Предложение с заменой 'ugly' на 'beauty': {new_predlojenie}")

if predlojenie.startswith("The"):
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")

if predlojenie.endswith("end"):
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")
