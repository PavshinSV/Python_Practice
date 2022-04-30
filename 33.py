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

print(polynom(3))