# Task 2
# Напишіть декоратор, який зберігає результати обчислення функції у файл для подальшого використання.

def calculation(file_name):
    def inner(base):
        with open(file_name, 'w') as f:
            f.write(f'Number added to file - {base}\n')
        return base
    return inner

file_write = calculation(2)

for i in range(8):
    print(file_write(i))