# 12.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:

import random

n = random.randint(1, 50)
test_list = {x: 3 * x + 1 for x in range(1, n + 1)}
print(f'Для N = {n}, получаем словарь:\n{test_list}')
