# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

value = [0, 1]
print(f'X  Y  Z  \tX V Y V Z\t¬X ⋀ ¬Y ⋀ ¬Z\tX V Y V Z = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in value:
    for y in value:
        for z in value:
            first_expression = bool(x or y or z)
            second_expression = (not x) and (not y) and (not z)
            print(
                f'{x}  {y}  {z}  \t{first_expression}\t\t{second_expression}\t\t{first_expression==second_expression}')
