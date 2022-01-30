#Задача 07. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def check_xyz(x, y, z):
    return (not(x and y and z)) == (not(x or y or z))
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(check_xyz(0,0,0))