# Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне). У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****

import math

size = int( input("Веедiть число (не парне): ") )

if size % 2 == 0:
    size -= 1

i = 1
k = 0
divided_size = size // 2
line_squeeze = divided_size
last_symbol_type = ""
symbol = ""

while i <= size:
    k = -divided_size
    while k <= divided_size:
        symbol = "*" if abs(k) <= line_squeeze else " "
        last_symbol_type = "\n" if divided_size == k else " "
        print(symbol, end = last_symbol_type)
        k += 1
    
    if i > divided_size:
        line_squeeze += 1
    else:
        line_squeeze -= 1

    i += 1