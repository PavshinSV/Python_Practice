# Показать первую цифру дробной части числа

variable = float(input("Введите число с дробной частью: "))
devided = int((variable*10)%10)
print(f'Первая цифра дробной части - {devided}')