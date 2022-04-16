# По двум заданным числам проверить является ли одно квадратом второго
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
if first_number**2 == second_number or first_number == second_number**2:
    print('Одно из чисел является квадратом другого')
else:
    print('Ни одно из чисел не является квадратом другого!')
