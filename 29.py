# Найти НОК двух чисел

def get_easy(num):
    res=[2]
    for i in range(3,num+1):
        is_easy=True
        for j in res:
            #print(f'i={i} j={j} i%j={i%j}')
            if not i%j:
                is_easy=False
        if is_easy:
            res.append(i)
    return res

def get_base(number,li):
    bases=[]
    for element in li:
        grade=1
        i=0
        while element*grade<=number:
            grade*=element
            i+=1
        b=i
        for j in range(i,-1,-1):
            if number%element**b:
                b-=1
        bases.append(b)
        number/=element**b
    return bases

def get_max_base(li):
    length=len(li[0])
    res=[]
    for i in range(0,length):
        max=0
        for j in li:
            if j[i]>max:
                max=j[i]
        res.append(max)
    return res

def nok(e, mb):
    res=1
    for i in range(0,len(e)):
        res*=e[i]**mb[i]
    return res

a=[int(input(f'Введите {x+1}е натуральное число: ')) for x in range(0,2)]
biger=max(a)

limit=int(biger**0.5)

easy=get_easy(limit)
print(easy)
bases=[get_base(el,easy) for el in a]
print(bases)
max_bases=get_max_base(bases)
print(max_bases)
kratnoe=nok(easy,max_bases)
print(f'Наименьшее общее кратное введенных чисел равно: {kratnoe}')