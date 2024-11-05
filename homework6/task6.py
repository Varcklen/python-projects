# Task 6
# Напишіть програму, яка підраховує частоту кожного слова у рядку.

text = input("Напиши текст: ")

words = text.split()
word_table = []
found = False

for word in words:
    found = False
    for word_line in word_table:
        if word_line[0] == word:
            word_line[1] += 1
            found = True
            break
    else:
        if not found:
            word_table.append([word, 1])

print("У текстi:")
for word_line in word_table:
    print(f"{word_line[0]}: {word_line[1]}")