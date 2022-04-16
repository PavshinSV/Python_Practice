# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

list = [1]
count = int(input('Введите количество членов последовательности: '))
print()
for i in range(1, count):
    list.append(list[i-1]*(-3))
print(list)
