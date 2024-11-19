# Task 2
# Створіть функцію, яка генерує пароль заданої довжини. Функція повинна приймати довжину паролю та булевий параметр, який визначає, чи має пароль містити спеціальні символи (наприклад, @, #, $ тощо).

import random

CODEX = "ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz"
SPECIAL_CODEX = "!@#$%^&*"

def get_password(length, is_special):
    password = ''
    i = 0
    current_codex = CODEX + SPECIAL_CODEX if is_special else CODEX
    while i < length:
        password += random.choice(current_codex)
        i += 1
    return password
    
length = int( input("Задайте довжину: ") )
is_special = input("Чи пароль повинен мати спеціальні символи (Y/N): ") == 'Y'

print( get_password( length, is_special ) )