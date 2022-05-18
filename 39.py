# 39. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# * Добавьте игру против бота
# * Подумайте как наделить бота "интеллектом"
import random

def get_comp_move():
    if player[2]==1:
        move = random.randint(min_step, max_step)
    else:
        if max_step>=candys: move = candys
        else: move = candys%(max_step+1)
    return move

def get_max_step(max, can):
    return max if max < can else can


def get_input():
    error = True
    while error:
        input_type = input("Введите число 1 или 2: ")
        if input_type.isdigit() and (0 < int(input_type) < 3):
            error = False
            input_type = int(input_type)
        else:
            print("Ошибка ввода")
    return input_type


def get_start(pl):
    print('Добро пожаловать в игру в конфеты.\nВыберите режим игры: 1 - два игрока, 2- игра с компьютером')
    player_type = get_input()
    if player_type == 1:
        pl[0] = "Игрок 1"
        pl[1] = "Игрок 2"
    else:
        pl[0] = "Игрок"
        pl[1] = "Компьютер"
        print(
            "\nВы выбрали игру с компьютером. Задайте уровень интелекта компьютера.\n1 - Тупой. 2 - С претензией на победу")
        pl[2] = get_input()


def get_candys():
    error = True
    while error:
        inp = input()
        if inp.isdigit() and (min_step <= int(inp) <= max_step):
            player_move = int(inp)
            error = False
        else:
            print(f"Введено не корректное значение. Пожалуйста, введите целое число от {min_step} до {max_step}")
    return player_move


player = ['', '', 1]

get_start(player)

candys = random.randint(10, 50)  # число конфет на старте
min_step = 1
max_step = 4
turn = 1

while candys > 0:
    max_step = get_max_step(max_step, candys)
    print(f"\nРаунд {turn}. Конфет осталось {candys}\nХодит {player[0]}.\nВозьмите от {min_step} до {max_step} конфет")

    player_move = get_candys()

    candys -= player_move
    if not candys:
        print(f"{player[0]} победил!! Парам-пам-пам!")
        break

    max_step = get_max_step(max_step, candys)

    print(f"\nКонфет осталось {candys}\nХодит {player[1]}.")
    if player[1]=="Игрок 2":
        max_step = get_max_step(max_step, candys)
        print(f"Возьмите от {min_step} до {max_step} конфет")
        player_move=get_candys()
    else:
        player_move=get_comp_move()
        print(f"{player[1]} взял {player_move} конфет")

    candys -= player_move
    if not candys:
        print(f"{player[1]} победил!! Пиу-пиу-пиу!")
        break

    turn += 1
