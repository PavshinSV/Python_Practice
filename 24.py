# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

max = 0
min = 1

list_of_numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(f'На входе имеем список чисел:\n{list_of_numbers}')

for element in list_of_numbers:
    swap = str(float(element)).split('.')
    if int(swap[1]):
        fraction = int(swap[1])/(10**len(swap[1]))
        if fraction < min:
            min = fraction
        if fraction > max:
            max = fraction

print(
    f'Максимальное значение дробной части: {max},\nминимальное значение дробной части: {min}\nразница между максимальной и минимальной частями равна: {max-min}')
