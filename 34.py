# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

with open('poly1.txt','r') as data:
    first_poly=data.readline().split(' = ')

with open('poly2.txt','r') as data:
    second_poly=data.readline().split(' = ')

with open('poly_summ.txt','w') as data:
    data.write(first_poly[0]+' + '+second_poly[0]+' = '+first_poly[1]+' + '+second_poly[1])