# Task 9
# Напишіть програму, яка кодує рядок, замінюючи кожну літеру на її номер в алфавіті (тільки для латинського алфавіту, наприклад, A = 1, B = 2).

codex = "ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz"

text = input("Напиши текст: ")
new_text = ""
i = 0

for symbol in text:
    if symbol not in codex:
        new_text += symbol
        continue

    i = 0
    while i < len(codex):
        if symbol == codex[i]:
            new_text += str(i + (1 if i <= 24 else -24)) + "_"
        i += 1

print(new_text)


