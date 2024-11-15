# Task 4
# Припустимо, що у тебе є дані про дружбу між користувачами соціальної мережі:
# friendships = {
#     "user1": {"user2", "user3", "user4"},
#     "user2": {"user1", "user3"},
#     "user3": {"user1", "user2", "user4"},
#     "user4": {"user1", "user3"}
# }
# Напишіть програму для розрахунку спільних друзів у соціальній мережі, імена яких задає користувач.

friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}

while True:
    user1 = 'user' + input("Задай користувача (1-4): ")
    user2 = 'user' + input("Задай другого користувача (1-4): ")

    if user1 == user2:
        print('Не працюемо з однаковим користовачем.')
        continue
    elif user1 not in friendships or user2 not in friendships:
        print('Не валiдна iнформацiя.')
        continue

    list1 = set(friendships[user1])
    list2 = set(friendships[user2])

    same_friends = list1 & list2

    if len(same_friends) == 0:
        print("Користувачi не мають спiльних друзiв.")
    else:
        print(same_friends)
    
    break
