# 15.	Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 6, 24]
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:
import math
import random

n=random.randint(2,10)

test = [math.factorial(x) for x in range(1,n+1)]
print(f'Для N = {n} набор произведений чисел от 1 до N:\n{test}')