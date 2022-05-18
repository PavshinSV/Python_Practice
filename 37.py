# 37. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#   [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

n = [5, 2, 3, 4, 6, 1, 7]
result = []
length = len(n)

for j in range(0, (length)):
    new_list = True
    indexes = []
    while new_list:
        r = []
        new_list = False
        for i in range(j, length):
            if i==j:
                r.append(n[i])
            if len(r) == 1:
                if not indexes.count(i) and n[i] > r[-1]:
                    r.append(n[i])
                    indexes.append(i)
                    new_list = True
            elif n[i] > r[-1]:
                r.append(n[i])
        if new_list: result.append(r)

maxi = []

for e in result:
    if len(e) > len(maxi):
        maxi = e.copy()

print(
    f'Из имеющегося списка {n} можно составить следующие возрастающие последовательности: \n{result},\n при этом самой длиной последовательностью явялется {maxi} ')
