# Task 2
# Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.

def fibonacci():
    values = [0, 1]

    def next():
        values[0], values[1] = values[1], values[0] + values[1]
        return values[0]
    return next

func = fibonacci()
for _ in range(15):
    print(func())