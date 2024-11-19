# Task 4
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

import math

def get_sequence_number(sequence):
    if len(sequence) <= 2:
        Exception("Замало даних.")

    if sequence[1] - sequence[0] == sequence[2] - sequence[1]:
        return sequence[-1] + sequence[1] - sequence[0]

    if sequence[0] != 0 and sequence[1] / sequence[0] == sequence[2] / sequence[1]:
        return sequence[-1] * sequence[1] / sequence[0]

    if math.sqrt(sequence[1]) - math.sqrt(sequence[0]) == math.sqrt(sequence[2]) - math.sqrt(sequence[1]):
        return (math.sqrt(sequence[-1]) + 1) ** (math.sqrt(sequence[1]) - math.sqrt(sequence[0]) + 1)

    return sequence[-1]

sequence_str = input('Введiть послiдовнiсть: ')
sequence = list( map( int, sequence_str.split(',') ) )

result = get_sequence_number(sequence)
print(f'result: {result}')