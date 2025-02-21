# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

import re

text = '(9999-9999-9999-9999)'
pattern = '\(^\d{4}-\d{4}-\d{4}-\d{4}\)$' #???

result = re.search(pattern, text)

print(f'valid!' if result else 'NOT VALID!')