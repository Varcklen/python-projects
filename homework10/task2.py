# 2. Скільки грошей витратив кожен член родини?

def to_number(text: str):
    return float( text.replace('$', '') )

family_spendings = {}
words = []

with open('hw_10_test.txt', 'r') as file:
    for line in file:
        words = line.split()
        if len(words) == 5:
            if words[2] in family_spendings:
                family_spendings[words[2]] += to_number(words[-2])
            else:
                family_spendings[words[2]] = to_number(words[-2])

for key, value in family_spendings.items():
    print(f'{key}: {value: .2f}')