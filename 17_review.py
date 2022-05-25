# 17.	Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension:
import random

def get_data(number):
    return [x for x in range(-number,number+1)]

def create_positions(number):
    length = number*2+1
    pos=random.sample([x for x in range(0,length)],random.randint(1,number))
    pos.sort()
    with open('17_review.txt', 'w') as file:
        [file.write(f'{x}\n') for x in pos]

def get_positions():
    with open('17_review.txt', 'r') as file:
        return list(map(int,[line for line in file]))

def get_mult(li,pos):
    mult=1
    for x in pos:
        mult*=li[x]
    return mult


n=random.randint(1,10)

num = get_data(n)
print(f'Для N = {n}, имеем список: {num}')

create_positions(n)
mult_positions=get_positions()
print(f'В файле записаны позиции для перемножения: {mult_positions}')
mult = get_mult(num,mult_positions)
print(f'Произведение элементов списка на указанных позициях = {mult}.')