# Task 5
# Реалізуйте генераторну функцію для генерації послідовності дат. Початкова та кінцеві дати мають бути задані параметрами цієї функції.

class Date:
    def __init__(self, day, month, year) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.__update()

    def __update(self):
        to_add_month = (self.day - 1) // 30
        self.day -= to_add_month * 30
        self.month += to_add_month

        to_add_year = (self.month - 1) // 12
        self.month -= to_add_year * 12
        self.year += to_add_year

    def compressed(self):
        return self.year * 30 * 365 + self.month * 30 + self.day

    def __iadd__(self, other:int):
        self.day += other
        self.__update()
        return self

    def __eq__(self, other) -> bool:
        return self.compressed() == other.compressed()

    def __str__(self) -> str:
        return f'{self.day}.{self.month}.{self.year}'


def date_consiquence(date1, date2):
    amount = date2.compressed() - date1.compressed()
    for _ in range(amount):
        yield date1
        date1 += 1

date1 = Date(24, 11, 1990)
date2 = Date(1, 12, 1990)

for date in date_consiquence(date1, date2):
    print(date)