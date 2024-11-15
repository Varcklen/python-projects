# Task 5
# Напишіть програму, яка повертає найдовше слово, яке міститься одночасно у двох рядках.

text = 'Хитру сороку спіймати морока, а на сорок сорок - сорок морок.'

lines = text.split(',')

print(lines)

words = []
set_line = []

for line in lines:
    set_line = set(line.split())
    words.append(max(set_line))

print(words)