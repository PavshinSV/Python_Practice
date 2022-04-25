# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

str='1 234 846 891 78 15 95 7651'

words=str.split(' ')

words[0]=int(words[0])
max=words[0]
min=words[0]

for i in range(1,len(words)):
    words[i]=int(words[i])
    if words[i]<min:
        min=words[i]
    elif words[i]>max:
        max=words[i]

print(f'Имеется строка с набором чисел разделенных пробелом: {str}')
print(f'В указанной строке максималльным является число: {max},\nа минимальным: {min}')