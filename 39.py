# 39. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# * Добавьте игру против бота
# * Подумайте как наделить бота "интеллектом"
import random

def get_max_step(max, can):
    return max if max<can else can

candys = random.randint(10,50) # число конфет на старте
min_step = 1
max_step = 4
turn = 1
while candys>0:
    max_step = get_max_step(max_step,candys)
    print(f"\nРаунд {turn}. Конфет осталось {candys}\nХод игрока.\nВозьмите от {min_step} до {max_step} конфет")
    error = True
    while error:
        inp = input()
        if inp.isdigit()and(min_step<=int(inp)<=max_step):
            player_move=int(inp)
            error=False
        else: print(f"Введено не корректное значение. Пожалуйста, введите целое число от {min_step} до {max_step}")
    candys-=player_move
    if not candys:
        print("Вы победили!! Парам-пам-пам!")
        break

    max_step = get_max_step(max_step, candys)
    comp_move = random.randint(min_step,max_step)
    print(f"\nКонфет осталось {candys}\nХод Компьютера.\nКомпьютер взял {comp_move}")
    candys-=comp_move
    if not candys:
        print("Компьютер победил!! Пиу-пиу-пиу!")
        break

    turn+=1