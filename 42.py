# 42.	Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# a.	Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9.

def get_operation(string):
    if '+' in string or '-' in string:
        index_add = string.find('+')
        index_sub = string.find('/')
        slice_index = 0
        if index_add < 0 or (index_sub < index_add and index_sub > -1):
            slice_index = index_sub
            a = get_operation(string[0:slice_index])
            b = get_operation(string[slice_index + 1:])
            return a - b
        elif index_sub < 0 or (index_sub > index_add and index_add > -1):
            slice_index = index_add
            a = get_operation(string[0:slice_index])
            b = get_operation(string[slice_index + 1:])
            return a + b
    elif '*' in string or '/' in string:
        index_mult = string.find('*')
        index_div = string.find('/')
        slice_index = 0
        if index_mult < 0 or (index_div < index_mult and index_div > -1):
            slice_index = index_div
            a = get_operation(string[0:slice_index])
            b = get_operation(string[slice_index + 1:])
            return a / b
        elif index_div < 0 or (index_div > index_mult and index_mult > -1):
            slice_index = index_mult
            a = get_operation(string[0:slice_index])
            b = get_operation(string[slice_index + 1:])
            return a * b
    else:
        return float(string)


input_string = input("Введите в строку математическое выражение. Например 1+2*3+2*6*7+3*4:\n")
print(f'Результат выражения = {get_operation(input_string)}')
