# Задача 18. Реализовать алгоритм перемешивания списка
def mix_list(a):
    n = len(a) # 5
    for i in range(0, n-1):
        a[i], a[i - 1] = a[i - 1], a[i]
    return a
print(mix_list([12, 44, 60, 20, 56, 257, 9, 643]))