# Составить список простых множителей натурального числа N

import algebra

try_input = True

while try_input:
    try:
        n = int(input('Введите натуральное положительное число: '))
    except ValueError:
        print(
            'Введенное вами значение не является целым числом больше нуля. Повторите ввод')
    else:
        try_input=False


print(f'Для введеного числа ряд список простых множителей: {algebra.easy(n)}')
