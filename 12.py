# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dictionary={}
count = int(input('Введите число элекментов в последовательности: '))
for i in range(1,count+1):
    dictionary[i]=3*i+1
print()
print(dictionary)