# 14.	Подсчитать сумму цифр в вещественном числе.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:
import random

number=random.random()
print(number)
numbers=str(number).split('.')
sum=sum(map(int, numbers[0]))+sum(map(int, numbers[1]))
print(f'Для числа {number} сумма его цифр равна {sum}')