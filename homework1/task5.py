# Task 5
# Деякі інвестиційні консультанти вважають, що розумно очікувати 10% прибутку в довгостроковій перспективі на фондовому ринку.
# Припускаючи, що ви починаєте з 1000 доларів і залишаєте свої гроші інвестованими, обчисліть і відобразіть, скільки грошей ви матимете через 10, 20 і 30 років. 
# Використовуйте наступну формулу для визначення цих сум:
# a = p(1 + r)^n
# де p — початкова інвестована сума (тобто основна сума 1000 доларів США),
# r – річна норма прибутку (10%),
# n - кількість років (10, 20 або 30),
# a — сума на депозиті на кінець n-го року.

p = 1000
r = 0.1
n = [10, 20, 30]

a1 = p * (1 + r) ** n[0]
a2 = p * (1 + r) ** n[1]
a3 = p * (1 + r) ** n[2]

print(f"Результат: {n[0]} рокiв: {a1}, {n[1]} рокiв: {a2}, {n[2]} рокiв: {a3}.")
input()