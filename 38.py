# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".
source_string = "абырабввалг Сегодня 1Абв мы strаБвншышпо будем АБВ12 изучать абВser азбуку"
words = source_string.split(' ')

print(f'Первоначально имеем строку:\n{source_string}\n')

sub_string = 'абв'

for word in words:
    if word.lower().find(sub_string) != -1: words.remove(word)

print(f'После удаления слов содержащих искомую подстроку получаем:\n{" ".join(words)}')
