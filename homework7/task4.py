# Task 4
# Напишіть програму, яка приймає рядок тексту і повертає словник, де ключами є слова, а значеннями - кількість входжень кожного слова в тексті.

text = input("Напиши текст: ")

words = text.split()
res = {}

for word in words:
    if word in res:
        res[word] += 1
    else:
        res[word] = 1

for key, value in res.items():
    print(f"{key}: {value}")