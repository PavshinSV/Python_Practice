# 36. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

n = [1, 5, 2, 3, 4, 6, 1, 7]
result = []
length = len(n)
indexes = []
new_list = True
while new_list:
    r = []
    new_list = False
    for i in range(0, length):
        if not i:
            r.append(n[i])

        if len(r)==1:
            if not indexes.count(i) and n[i]>r[-1]:
                r.append(n[i])
                indexes.append(i)
                new_list = True
        elif n[i] > r[-1]:
            r.append(n[i])
    if new_list: result.append(r)
print(f'Из имеющегося списка {n} можно составить следующие возрастающие последовательности: \n{result}')
