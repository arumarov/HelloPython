# Задача 08. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
def coordinate(x,y):
    if x > 0 and y > 0: res = 'I четверть'
    elif x < 0 and y > 0: res = 'II четверть'
    elif x < 0 and y < 0: res = 'III четверть'
    elif x > 0 and y < 0: res = 'IV четверть'
    elif x == 0 and y == 0: res = 'центр'
    elif x == 0: res = 'ось X'
    elif y == 0: res = 'ось Y'
    return res
print(coordinate(10,-6))
