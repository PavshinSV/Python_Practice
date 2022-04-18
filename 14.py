# Подсчитать сумму цифр в вещественном числе.

number_to_acc = float(
    input('Введите вещественное (с дробной частью, через точку) число: '))
two_half = str(number_to_acc).split('.')
one_sting = two_half[0]+two_half[1]
result_str = 0
for i in range(0, len(one_sting)):
    result_str += int(one_sting[i])
print(f'Сумма цифр в числе равна: {result_str}')
