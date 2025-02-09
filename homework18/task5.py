# Напишіть декоратор, який логує аргументи та результати функції.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def logger_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Arguments:')
        for arg in args:
            logger.info(arg)
        logger.info(f'Result: {result}')
        return result
    return wrapper

@logger_decor
def add_numbers(a, b):
    return a + b

add_numbers(3, 4)