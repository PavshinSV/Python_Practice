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

#def get_max_base(li):
    


a=[int(input(f'Введите {x+1}е натуральное число: ')) for x in range(0,3)]
biger=max(a)

limit=int(biger**0.5)

easy=get_easy(limit)
bases=[get_base(el,easy) for el in a]
