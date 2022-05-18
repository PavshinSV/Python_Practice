# 40. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
import random

field = [[' ', ' ', ' '],  # - пустое поле, 1 - крестик, 2 - нолик
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# крестики ставит игрок, нолики - компьютер

def visual_field():
    print(' ', '  0,   1,   2 ')
    print(0, field[0])
    print(1, field[1])
    print(2, field[2])


def get_player_move():
    field_error = True
    while field_error:
        print('\nВведите координаты хода (строка столбец) через пробел: ')
        input_error = True
        while input_error:
            move = input().split(' ')
            if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                input_error = False
                move = list(map(int, move))
            else:
                print('Введены не верные значения. Повторите ввод')
        if field[move[0]][move[1]] == ' ':
            field_error = False
            field[move[0]][move[1]] = 'X'
        else:
            print("Указанное вами поле занято. Выберите другие координаты.")


def get_computer_move():
    field_error = True
    move = [0, 0]
    while field_error:
        move[0] = random.randint(0, 2)
        move[1] = random.randint(0, 2)
        if field[move[0]][move[1]] == ' ':
            field_error = False
            field[move[0]][move[1]] = '0'


def check_for_win():
    if (field[0][0] == field[0][1] == field[0][2]) and field[0][2] != ' ' or (
            field[1][0] == field[1][1] == field[1][2]) and field[1][2] != ' ' or (
            field[2][0] == field[2][1] == field[2][2]) and field[2][2] != ' ' or (
            field[0][0] == field[1][0] == field[2][0]) and field[2][0] != ' ' or (
            field[0][1] == field[1][1] == field[2][1]) and field[2][1] != ' ' or (
            field[0][2] == field[1][2] == field[2][2]) and field[2][2] != ' ' or (
            field[0][0] == field[1][1] == field[2][2]) and field[2][2] != ' ' or (
            field[2][0] == field[1][1] == field[0][2]) and field[0][2] != ' ':
        return True
    else:
        return False


game = True
turn = 1

print(
    "Мы начинаем игру в крестики-нолики.\nДля того, чтобы поставить крестик нужно указать номер строки(отображается слева от игрового поля) \n"
    "и номер столбца(отображается сверху над игровым полем) через пробел")
visual_field()

while game:
    print(f'Ход №{turn}\nХодит Игрок.\n')
    get_player_move()
    visual_field()
    if check_for_win():
        print("Игрок победил! Да здравствует величие человеческого разума!")
        break
    if field.count(' ') == -1:
        print('Ходов больше не осталось. Ничья. У человечества еще есть надежда.')
        break
    get_computer_move()
    visual_field()
    if check_for_win():
        print("Компьютер победил! Всем приготовиться! Скайлайн атакует! Т100 уже в пути!")
        break
    turn += 1
