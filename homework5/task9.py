# Task 9
# Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць. Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

summary = 0
for salary in salaries:
    summary += salary

result = summary / len(salaries)

print(result)