# 3. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?

def to_number(text: str):
    return float( text.replace('$', '') )

FAMILY_NAME = 'Simson'
person = input('Впишiть iм`я людини: ')
amount = 0
words = []

with open('hw_10_test.txt', 'r') as file:
    for line in file:
        words = line.split()
        if words[1] == person and words[2] == FAMILY_NAME:
            amount += to_number(words[-2])
            
if amount:
    print(f'{person} з родини {FAMILY_NAME} витратив {amount: .2f} грошей.')
else:
    print('Такоi людини немае у списку.')
    