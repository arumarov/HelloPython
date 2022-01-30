# Задача 09. Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти
def coordinate(a):
    if a == 1: res = 'x > 1; y > 1'
    elif a == 2: res = 'x < 1; y > 1'
    elif a == 3: res = 'x < 1; y < 1'
    elif a == 4: res = 'x > 1; y < 1'
    return res
print(coordinate(4))