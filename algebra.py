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
