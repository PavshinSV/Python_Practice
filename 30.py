# Вычислить число π c заданной точностью d
# Пример: при d = 0.001,π = 3.141.10^(-1)≤d≤10^(-10)

precission=0.001

error=3
pi=0
i=1

while abs(error)>precission/10:
    previos=pi
    pi+=4/i
    if i>0:
        i=(i+2)*(-1)
    else:
        i=(i-2)*(-1)
    error=previos-pi

pi=(pi//precission)*precission
print('При расчете числа Пи с заданной точностью: {0} получено значение: {1}'.format(precission,pi))