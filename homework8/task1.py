# Task 1
# Напишіть програму, яка перевіряє, чи всі елементи в списку є унікальними.

my_list = [1, 2, 3, 4, 5]

set_list = set(my_list)

if len(my_list) == len(set_list):
    print("Унiкальний!")
else:
    print("Не унiкальний!")