# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

WORDS = {
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


def get_amount_piece(value, with_float):
    result = ''
    if with_float == False:
        value = int(value)
    value = str(value)
    for number, word in WORDS.items():
        if str(number) in value:
            result += value.replace(str(number), word) + ' '
    return result

str_value = input('Введiть число: ')
value = float(str_value)

text = ''

if value > 100:
    text += get_amount_piece(value // 100, False) + 'hundred '
    value -= 100

text += get_amount_piece(value, True)
#????????
print(text)