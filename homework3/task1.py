# Task 1
# Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі. Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.

number = int( input("Вкажiть номер квартири: ") )

ENTRANCE_AMOUNT = 4
FLOOR_AMOUNT = 9
APARTMENTS_PER_FLOOR = 4

MAX_APARTMENT_PER_ENTRANCE = FLOOR_AMOUNT * APARTMENTS_PER_FLOOR
MAX_APARTMENT_NUMBER = ENTRANCE_AMOUNT * MAX_APARTMENT_PER_ENTRANCE

prev_number = number - 1

entrance = prev_number // (FLOOR_AMOUNT * APARTMENTS_PER_FLOOR) + 1
entrance_counter = (entrance - 1) * MAX_APARTMENT_PER_ENTRANCE # Повертае число, незалежне вiд пiд'їзду (у пiд'їздi 36 квартир). При number 1 => 1, при number 36 => 36, при number 37 => 1.

floor = ( prev_number - entrance_counter ) // APARTMENTS_PER_FLOOR + 1
apartment_number = prev_number - entrance_counter + 1 - (floor - 1) * APARTMENTS_PER_FLOOR

if not 0 < number <= MAX_APARTMENT_NUMBER:
    print(f"Число {number} не может бути номером квартири. Використовивай число вiд 1 до {MAX_APARTMENT_NUMBER}.")
else:
    print(f"Під'їзд: {entrance}, Поверх: {floor}, Номер на поверсi: {apartment_number}.")