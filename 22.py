# Найти сумму чисел списка стоящих на нечетной позиции

list_of_numbers=[0,25,135,-32,98,12,-83,2,15]
summ=0
for i in range(1,len(list_of_numbers),2):
    summ+=list_of_numbers[i]
print(f'В имеющемся массиве {list_of_numbers}')
print(f'Сумма элементов стоящих на нечетных позициях равна: {summ}')