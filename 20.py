# Определить, присутствует ли в заданном списке строк, некоторое число 

list_of_words = ['Привет','Анна','вилка','125','Луна','SpaceX','15']
print(f'Список: {list_of_words}')
desired = input('Введите число, присутствие которого в списке необходимо определить: ')

presence = False

for element in list_of_words:
    if element==desired:
        presence=True

if presence:
    print('Введенное число в списке присутствует')
else:
    print('Введенное число в списке отсутствует')