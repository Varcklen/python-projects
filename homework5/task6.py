# Task 6
# Напишіть скрипт, який виводить на екран прямокутник із '*'. Висота і ширина прямокутника вводяться з клавіатури.  Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.
# *****
# *   *
# *   *
# *****

width = int( input("Введiть ширину: ") )
height = int( input("Введiть длину: ") )

i = 1
k = 0
last_symbol_type = ""
symbol = ""

while i <= height:
    k = 1
    while k <= width:
        if k == 1 or k == width or i == 1 or i == height:
            symbol = "*"
        else:
            symbol = " "
        last_symbol_type = "\n" if width == k else " "
        print(symbol, end = last_symbol_type)
        k += 1 
    i += 1 