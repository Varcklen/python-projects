# Task 5
# Написати скрипт, який повертає найбільше число серед трьох, які введені користувачем.

print("Введiть 3 числа:")
number1 = int( input("Введiть перше число: ") )
number2 = int( input("Введiть друге число: ") )
number3 = int( input("Введiть трете число: ") )

# if number1 >= number2:
#     if number1 >= number3:
#         max = number1
#     else:
#         max = number3
# else:
#     if number2 >= number3:
#         max = number2
#     else:
#         max = number3

max = max(number1, number2, number3)

print(max)