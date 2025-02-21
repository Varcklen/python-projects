# Task 1
# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.

import re

text = 'rbR Rbbbr Rbbr rrrrr rrro'
pattern = 'R+b*r+'

result = re.findall(pattern, text)

for element in result:
    print(element)