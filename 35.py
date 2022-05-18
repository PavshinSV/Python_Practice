# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('35.txt', 'r') as data:
    n = list(map(int,data.readline().split(' ')))

dropdown = 0;
dropdown_flag = False
print(n)
length = len(n)-1
for i in range(0,length):
    if n[i]+1<n[i+1]:
        dropdown=n[i]+1
        dropdown_flag = True

if dropdown_flag:
    print(f'Недостающее число: {dropdown}')
else:
    print(('Нет выпадающих чисел, все идут по порядку'))