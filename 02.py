# Найти максимальное из пяти чисел

amount = 5
number = []
for i in range(0,amount):
    number.append((int(input(f'Введите число №{i+1}: '))))
print()
print(f'Вы ввели следующие числа: {number}')
print()
print(f'Максимальным числом является: {max(number)}')
