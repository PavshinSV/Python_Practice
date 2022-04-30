# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# Линейно-конгруэнтный метод

psch=[0,0,0,0]
param=[100,5,2,1]
try:
    data = open('param_LKM.txt', 'r')
except FileNotFoundError:
    with open('param_LKM.txt', 'w') as data:
        data.write(f'{param[0]}\n')
        data.write(f'{param[1]}\n')
        data.write(f'{param[2]}\n')
        data.write(f'{param[3]}\n')
else:
    i=0
    for line in data:
        param[i]=int(line)
        i+=1
finally:
    data.close()

for i in range(0,4):
    psch[i]=(param[1]*param[3]+param[2])%param[0]
    param[3]+=param[3]

with open('param_LKM.txt','w') as data:
    data.write(f'{param[0]}\n')
    for i in range(1,4):
        data.write(f'{psch[i]}\n')

print(f'Ваше Псевдо Случайное Число на сегодня: {psch[1]}')