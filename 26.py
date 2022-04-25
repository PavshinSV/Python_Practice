# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibonachi(num):
    fibonachi_list=[]
    i=0
    while num>i:
        if i < 2:
            fibonachi_list.append(1)
            i+=1
        else:
            fibonachi_list.append(fibonachi_list[i-2]+fibonachi_list[i-1])
            i+=1
    return fibonachi_list

def nego_fibonachi(num):
    fibonachi_list=[]
    i=0
    while num>i:
        if i==0:
            fibonachi_list.insert(0,1)
            i+=1
        elif i==1:
            fibonachi_list.insert(0,-1)
            i+=1
        else:
            fibonachi_list.insert(0,-(fibonachi_list[0])+fibonachi_list[1])
            i+=1
    return fibonachi_list

number=int(input('Введите число значений в ряду Фибоначчи: '))

result_list=[]
result_list.extend(nego_fibonachi(number))
result_list.extend([0])
result_list.extend(fibonachi(number))
print(result_list)