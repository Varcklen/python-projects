# Task 3
# Реалізуйте свій аналог генераторної функції range().

def my_range(end, start = 1):
    while start <= end:
        yield start
        start += 1

for i in my_range(5, 2):
    print(i)