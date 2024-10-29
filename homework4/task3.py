# Task 3
# Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури координати точки x та y. Написати програму, яка визначить, лежить ця точка всередині кола чи ні.

RADIUS = 4
CENTER = [0,0]

x = float(input("Введiть координату x: "))
y = float(input("Введiть координату y: "))

if (x - CENTER[0]) ** 2 + (y - CENTER[1]) ** 2 <= RADIUS ** 2:
    print("Точка у колi.")
else:
    print("Точка вне кола.")