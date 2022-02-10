# Задача 27. Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел
def max_min(a): 
    b = list(map(int, a.split()))
    max, min = b[0], b[0]
    for i in range(0, len(b)):
        if b[i] > max: max = b[i]
        elif b[i] < min: min = b[i]
    print('Max = ', max)
    print('Min = ', min)

a = '3 27 6 54 112 9 1'
max_min(a)