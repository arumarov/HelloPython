# Задача 02. Найти максимальное из пяти чисел
def find_max (a, b, c, d, e):
    max = a
    if b > max: 
        max = b
    if c > max: 
        max = c
    if d > max: 
        max = d
    if e > max: 
        max = e
    return max
print(find_max(19, 12, 224, 135, 36))