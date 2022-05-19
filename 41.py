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
import re

source_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
length = len(source_string)
code_string = ''
counter=1
for i in range(1,length):
    if source_string[i-1]!=source_string[i]:
        code_string+=str(counter)+source_string[i-1]
        counter=1
    else:
        counter+=1
    if i==length-1:
        code_string+=str(counter)+source_string[i]

print(code_string)

sss = re.split(r'\W+',code_string)
print(sss)