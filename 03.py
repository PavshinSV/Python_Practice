# Вывести на экран числа от -N до N

n = int(input('Введите число: '))
step = 1
start = -n
stop = n+1
if n < 0:
    step = -1
    stop -= 2
for i in range(start, stop, step):
    print(i, end=' ')
