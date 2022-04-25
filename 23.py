# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import math


def pair_multiply(array):
    length = len(array)
    result = []
    for i in range(0, math.ceil(length/2)):
        result.append(array[i]*array[length-1-i])
    return result


list_of_numbers = [2, 3, 4, 5, 6]

print('Исходный список: ')
print(f'{list_of_numbers}\n\n')
print('Список полученный произведением пар чисел: ')
print(f'{pair_multiply(list_of_numbers)}\n\n')
