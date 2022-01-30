# Задача 10. Найти расстояние между двумя точками пространства
def place(xa,xb,ya,yb):
    import math
    return (math.sqrt((xb-xa)**2 + (yb-ya)**2))
print(place(12,4,-1,-9))