# Task 2
# Створіть клас "Правильна Дріб" і реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.

import math

class CorrectFraction:
    def __compression__(self):
        divider = math.gcd(int(self.numerator), int(self.denominator))
        self.numerator /= divider
        self.denominator /= divider

    def __check_full_value__(self):
        if self.denominator == 0:
            raise ValueError('denominator must be not 0.')

        full_value_to_add = self.numerator // self.denominator

        if full_value_to_add == 0:
            return

        self.numerator -= full_value_to_add * self.denominator
        self.full_value += full_value_to_add

    def __update__(self):
        self.__compression__()
        self.__check_full_value__()

    def __init__(self, numerator, denominator, full_value = 0):
        self.numerator = numerator
        self.denominator = denominator
        self.full_value = full_value

        self.__update__()

    def __error_check__(self, other):
        if not isinstance(other, CorrectFraction):
            raise TypeError('other must be CorrectFraction')

    def __decompression__(self):
        self.numerator += self.full_value * self.denominator
        self.full_value = 0

    #Урівнює знаменатель двох дробів і повертає числитель другої дроби
    def __equality__(self, other):
        other_numerator = (other.full_value * other.denominator + other.numerator) * self.denominator
        other_denominator = other.denominator

        self.__decompression__()
        self.numerator *= other_denominator 
        self.denominator *= other_denominator

        return other_numerator

    #Урiвняння
    def __add__(self, other):
        self.__error_check__(other)

        other_numerator = self.__equality__(other)
        self.numerator += other_numerator

        self.__update__()
        return self

    def __sub__(self, other):
        self.__error_check__(other)

        other_numerator = self.__equality__(other)
        self.numerator -= other_numerator

        self.__update__()
        return self

    def __mul__(self, other):
        self.__error_check__(other)

        self.__decompression__()
        self.numerator *= other.numerator
        self.denominator *= other.denominator

        self.__update__()
        return self

    def __truediv__(self, other):
        self.__error_check__(other)

        self.__decompression__()
        self.numerator *= other.denominator
        self.denominator *= other.numerator

        self.__update__()
        return self

    def __str__(self):
        text = ''
        if self.full_value != 0:
            text += f'{self.full_value:.0f}'
        if self.full_value != 0 and self.numerator != 0:
            text += ' + '
        if self.numerator != 0:
            text += f'{self.numerator:.0f}/{self.denominator:.0f}'
        return text

fraction = CorrectFraction(1, 2, 3)
fraction2 = CorrectFraction(3, 4)

print(f'Перше число: {fraction}')
print(f'Друге число: {fraction2}')

fraction += fraction2
print(f'+: {fraction}')

fraction = CorrectFraction(1, 2, 3)
fraction -= fraction2
print(f'-: {fraction}')

fraction = CorrectFraction(1, 2, 3)
fraction *= fraction2
print(f'*: {fraction}')

fraction = CorrectFraction(1, 2, 3)
fraction /= fraction2
print(f'/: {fraction}')