# Задача 18. Реализовать алгоритм перемешивания списка
# Мое решение (хреновое)
def mix_list(a):
    n = len(a)
    for i in range(0, n-1):
        a[i], a[i - 1] = a[i - 1], a[i]
    return a
print(mix_list([12, 44, 60, 20, 56, 257, 9, 643]))

# Решение с вебинара
from random import * # импорт всех функций из random
new_array = [i for i in range(10)]
print(new_array)

def liat1(x):
    for i in range(len(x)-1):
        index = randint(i+1,len(x)-1)
        x[i], x[index] = x[index], x[i]
    return x

print(liat1(new_array))