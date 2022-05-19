# 41. Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# * Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
#
# Задание было изменено преподавателем. Вместо вычисления арифметического выражения надо реализовать RLE алгоритм.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:
# 12W1B12W3B24W1B14W

def get_coder(source):
    length = len(source)
    code_string = ''
    counter = 1
    for i in range(1, length):
        if source[i - 1] != source[i]:
            code_string += str(counter) + source[i - 1]
            counter = 1
        else:
            counter += 1
        if i == length - 1:
            code_string += str(counter) + source[i]
    return code_string


def get_decoder(source):
    length = len(source)
    decoded_string = ''
    digit = ''
    for i in source:
        if i.isdigit():
            digit += i
        else:
            decoded_string += i * int(digit)
            digit = ''
    return decoded_string

def get_input():
    error = True
    while error:
        input_type = input("Введите число 1 или 2: ")
        if input_type.isdigit() and (0 < int(input_type) < 3):
            error = False
            input_type = int(input_type)
        else:
            print("Ошибка ввода")
    return input_type

source_string_test = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
coded_string_test = "12W1B12W3B24W1B14W"

print("Введите направление кодирования. 1 - Кодирование (Сжатие). 2 - Декодирование (Распаковка)")
if get_input() == 1:
    print('Строка будет введена вами вручную или использовать тестовую строку? 1- Тестовая строка. 2 - Ввод вручную')
    if get_input() == 1:
        print(f'Тестовая строка имеет вид:\n{source_string_test}\n')
        print(f'В результате кодирования получаем строку:\n{get_coder(source_string_test)}')
    else:
        input_string=input('Введите строку символов без чисел:')
        print(f'В результате кодирования получаем строку:\n{get_coder(input_string)}')
else:
    print('Строка будет введена вами вручную или использовать тестовую строку? 1- Тестовая строка. 2 - Ввод вручную')
    if get_input() == 1:
        print(f'Тестовая строка имеет вид:\n{coded_string_test}\n')
        print(f'В результате декодирования получаем строку:\n{get_decoder(coded_string_test)}')
    else:
        input_string=input('Введите кодированную строку, начинающуюся с числа за которым следует символ и т.д.:')
        print(f'В результате декодирования получаем строку:\n{get_decoder(input_string)}')