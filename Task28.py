# Задача 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
#  1. Математикой
#  2. Используя дополнительные библиотеки*

# Математикой
def find_roots(a,b,c):
    import math

    d = b**2 - 4*a*c
    if d < 0:
        x1 = 'корней'
        x2 = 'нет'
    elif d == 0: 
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = ''
    elif d > 0: 
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
    return x1, x2

a, b, c = 121, 169, 22
print(find_roots(a, b, c))