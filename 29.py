# Найти НОК двух чисел

def easy(num):
    arr=[]
    n=2
    while num>1:
        if not num%n:
            arr.append(n)
        else:
            n+=1
    return arr

a=17
b=28

print(easy(a))
print(easy(b))