# Необхідно підготувати звіт про витрати членів родини на новорічні свята.
# Дані по витратам наведено у файлі hw_10_test.txt у форматі:
# Номер за переліком Прізвище та ім'я (або ім'я) Сума Категорія товару
# Звіт повинен включати наступне:
# 1. Яка загальна сума витрат по кожній категорії товарів?

def to_number(text: str):
    return float( text.replace('$', '') )

spendings = {}
words = []

with open('hw_10_test.txt', 'r') as file:
    for line in file:
        words = line.split()
        if words[-1] in spendings:
            spendings[words[-1]] += to_number(words[-2])
        else:
            spendings[words[-1]] = to_number(words[-2])

for key, value in spendings.items():
    print(f'{key}: {value: .2f}')