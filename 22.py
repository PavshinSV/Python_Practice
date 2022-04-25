# Найти сумму чисел списка стоящих на нечетной позиции

list_of_numbers=[0,25,135,-32,98,12,-83,2]
summ=0
for i in range(0,len(list_of_numbers)-1,2):
    summ+=list_of_numbers[i]
print(f'В имеющемся массиве {list_of_numbers}')
print(f'Сумма элементов стоящих на нечетных позициях равна: {summ}')