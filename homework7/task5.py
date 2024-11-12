# Task 5
# Реалізуйте простий перекладач, який використовує словник для збереження пар слів. Користувач може вводити слово, а програма повертає його переклад. У цьому випадку, словник може використовуватись для збереження відповідностей між словами у різних мовах.
# Приклад:
# translations = {
#     'hello': 'привіт',
#     'goodbye': 'до побачення',
#     'cat': 'кіт',
#     'dog': 'собака'
# }

text = input('Введи текст зi слiв: hello, goodbye, cat, dog: ')

translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}

for key, translate in translations.items():
    text = text.replace(key, translate)

print(text)