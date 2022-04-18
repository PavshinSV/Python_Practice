# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

collection_of_numbers=[1]
n=int(input('Введите число N, сколько значений должен содержать набор: '))
for i in range(2,n+1):
    collection_of_numbers.append(collection_of_numbers[i-2]*i)
print(collection_of_numbers)