# Task 3
# Напишіть програму, яка приймає словник і перевіряє, чи містяться в ньому унікальні значення.

my_dict = {
    1: 'one',
    2: 'two',
    3: 'two',
    4: 'four',
    5: 'one'
}

set_list = set(my_dict.values())

my_dict_length = len(my_dict)
set_list_length = len(set_list)

if my_dict_length - 1 > set_list_length * 2 or set_list_length  == my_dict_length:#???
    print("Мiстить унiкальнi значення.")
else:
    print("Не мiстить унiкальних значень.")
    