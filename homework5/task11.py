# Task 11
# Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.

numbers = [7,2,9,4]

i = 0
i_max = len(numbers) 

while i < i_max // 2:
    # print(numbers[i])
    # print(numbers[i_max - i - 1])
    numbers[i], numbers[i_max - i - 1] = numbers[i_max - i - 1], numbers[i]
    i += 1

print(numbers)