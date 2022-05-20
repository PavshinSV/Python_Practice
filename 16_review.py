# 16.	Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:

import random

n=random.randint(1,10)
test_list=[(1+1/x)**x for x in range(1,n+1)]
summ=sum(test_list)
print(f'Для N = {n} список значений {test_list},\nИх сумма равна {summ}')