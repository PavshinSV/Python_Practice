# Написать программу преобразования десятичного числа в двоичное

def decimal_at_binary(num):
    result = ''
    while num > 1:
        result = str(num % 2)+result
        num = int(num/2)
    if num == 1:
        result = '1'+result
    return result


number = int(input('Введите целое десятичное число: '))

print(
    f'В двоичном формате это число запишется в виде: {decimal_at_binary(number)}')
