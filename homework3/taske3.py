# Task 3
# Попросіть користувача ввести номер місяця (1-12). Виведіть кількість днів у цьому місяці. (Зверніть увагу на високосні роки для лютого.)

month = int(input("Введи мiсяць: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not 1 <= month <= 12:
    print("Мiсяць введено не правильно!")
else:
    print(f"У мiсяцi {days_in_month[month]} днiв.")