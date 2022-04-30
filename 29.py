# Найти НОК двух чисел

def easy(num):
    arr = []
    n = 2
    while num > 1:
        if not num % n:
            arr.append(n)
            num = num/n
        else:
            n += 1
    return arr

nok=1
a = 441
b = 700

easy_a = easy(a)
easy_b = easy(b)

for i in range(0, len(easy_a)):
    if easy_a[i] != easy_a[i-1] or i == 0:
        if easy_a.count(easy_a[i])>easy_b.count(easy_a[i]):
            for j in range(0, easy_a.count(easy_a[i])-easy_b.count(easy_a[i])):
                easy_b.append(easy_a[i])

for element in easy_b:
    nok*=element

print(f'\nДля чисел a: {a} и b: {b} Наименьшее Общее Кратное (НОК) будет равно: {nok}\n')