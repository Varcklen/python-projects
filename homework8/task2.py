# Task 2
# Напишіть програму, яка приймає список елементів і повертає кількість унікальних елементів.

my_list = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]

set_list = set(my_list)

print(f"Всього елементiв: {len(my_list)}")
print(f"Унiкальних елементiв: {len(set_list)}")