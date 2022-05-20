# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:
import random

n=random.randint(1,20)
test_list=[x for x in range(-n,n+1)]
print(f'Для N = {n} получаем список:\n{test_list}')