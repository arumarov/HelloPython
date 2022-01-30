# Задача 01. По двум заданным числам проверить является ли одно квадратом второго 
def check (a,b):
    res = False
    if a==b*b: res = True
    return res
print(check(9,3))