# Task 6
# Реалізуйте просту програму для збереження контактів. Кожен контакт може мати ім'я як ключ та номер телефону як значення. Дозвольте користувачу додавати нові контакти, видаляти існуючі та отримувати номер телефону за ім'ям.

contacts = {}
action = 0
key = 0
value = 0

while True:
    action = 0
    print("==========================")
    print("Ви маете список дiй:")
    print("1 - Додати/замiнити контакт")
    print("2 - Видалити контакт")
    print("3 - Зобачити контакти")
    print("4 - Закiнчити")
    action = int( input("Напишiть дiю (цифру): ") )
    print("-------------------------")
    if action == 1:
        key = input("Напишiть iм`я: ")
        value = input("Напишiть номер телефону: ")
        contacts[key] = value
        print("Данi оновленi!")
    elif action == 2:
        key = input("Напишiть iм`я: ")
        if key in contacts:
            contacts.pop(key)
            print("Данi видаленi!")
        else:
            print("Таких даних не мае!")
    elif action == 3:
        print(contacts)
    elif action == 4:
        print("До побачення!")
        break
    else:
        print("Цiеi дii не iснуе.")