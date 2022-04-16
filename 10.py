# Найти расстояние между двумя точками пространства

def input_coordinates():
    abscissa = int(input('Введите координату Х: '))
    ordinate = int(input('Введите координату Y: '))
    return [abscissa, ordinate]


print('Ввод координат первой точки')
first_coordinates = input_coordinates()
print()
print('Ввод координат второй точки')
second_coordinates = input_coordinates()
print()
distance_between_points = ((first_coordinates[0]-second_coordinates[0])**2+(
    first_coordinates[1]-second_coordinates[1])**2)**0.5
print(f'Расстояние между введеными точками = {distance_between_points:.2f}')
