# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import algebra

def polynom(ext):
    if not ext:
        return str(algebra.psevdo())+' = 0'
    elif ext==1:
        return str(algebra.psevdo())+'*x'+' + '+polynom(ext-1)
    else:
        return str(algebra.psevdo())+'*x^'+str(ext)+' + '+polynom(ext-1)

try_input = True

while try_input:
    try:
        k = int(input('Введите натуральное положительное число (основание степени): '))
    except ValueError:
        print(
            'Введенное вами значение не является целым числом больше нуля. Повторите ввод')
    else:
        try_input=False

p=polynom(k)

print(f'По введенному Вами основанию степени многочлен представляется в виде: {p}')

with open('polynomes.txt', 'a') as data:
    data.write(f'{p}\n')
