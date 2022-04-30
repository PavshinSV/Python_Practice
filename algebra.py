def deskriminanta(a, b, c):
    return b**2-4*a*c

def square_roots(a, b, c):
    d = deskriminanta(a, b, c)
    if d < 0:
        print(f'D < 0. Система не имеет решений!\n')
    elif d > 0:
        print(
            f'D > 0. Система имеет два корня, х1: {(-b-d**0.5)/(2*a):.2f} и х2: {(-b+d**0.5)/(2*a):.2f}\n')
    else:
        print(f'D = 0. Система имеет один корень, х: {-b/(2*a):.2f}\n')

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

def psevdo():
    psch=[0,0,0,0]
    param=[100,5,2,1]
    try:
        data = open('param_LKM.txt', 'r')
    except FileNotFoundError:
        with open('param_LKM.txt', 'w') as data:
            data.write(f'{param[0]}\n')
            data.write(f'{param[1]}\n')
            data.write(f'{param[2]}\n')
            data.write(f'{param[3]}\n')
    else:
        i=0
        for line in data:
            param[i]=int(line)
            i+=1
    finally:
        data.close()

    for i in range(0,4):
        psch[i]=(param[1]*param[3]+param[2])%param[0]
        param[3]+=param[3]

    with open('param_LKM.txt','w') as data:
        data.write(f'{param[0]}\n')
        for i in range(1,4):
            data.write(f'{psch[i]}\n')
    return psch[1]