# Реализовать алгоритм перемешивания списка. 

from random import randint


array = [1,2,3,4,5,6,7,8,9,10]
print(f'На входе имеем массив:\n{array}')
for i in range(0,len(array)-1):
    swap=array[i]
    rnd=randint(i+1,len(array)-1)
    array[i]=array[rnd]
    array[rnd]=swap
print(f'После перемешивания имеем массив:\n{array}')