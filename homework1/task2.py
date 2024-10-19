#Task 2
#Написати Python-скрипт, який для п'яти цілочисельних значень (вводить користувач з клавіатури), знаходить мінімум, максимум та середнє.
#Для пошуку мінімального та максимального значення потрібно використовувати функції min, max:
#https://docs.python.org/3/library/functions.html#max
#https://docs.python.org/3/library/functions.html#min

print("Введiть п'ять чисел:")
number1 = int(input("Число №1: "))
number2 = int(input("Число №2: "))
number3 = int(input("Число №3: "))
number4 = int(input("Число №4: "))
number5 = int(input("Число №5: "))

min = min(number1, number2, number3, number4, number5)
max = max(number1, number2, number3, number4, number5)
avg = (number1 + number2 + number3 + number4 + number5) / 5
print(f"min: {min}, max: {max}, avg: {avg}.")
input()