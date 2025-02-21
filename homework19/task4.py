# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.

import re

text = '2345642345'
pattern = '([a-z]|[A-Z]|[0-9]){2,10}'

result = re.search(pattern, text)

print(f'valid!' if result.group() == text else 'NOT VALID!')