# Task 7
# Написати скрипт, яких тризначне ціле число (вводить користувач з клавіатури) розділяє на окремі цифри. Кожну цифру треба вивести в окремому рядку.
# Наприклад, якщо користувач вводить число 987, скрипт має вивести в термінал
# 9
# 8
# 7

string_value = input("Введiть тризначне ціле число: ")
print(string_value[0], string_value[1], string_value[2], sep="\n")
input()