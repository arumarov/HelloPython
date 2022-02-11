# Задача 29. Найти НОК двух чисел
def multiple(a, b):
    list_a = [a*i for i in range(1,10000)]
    list_b = [b*i for i in range(1,10000)]
    result = list(set(list_a) & set(list_b))
    min = result[0]
    for i in range(0,len(result)):
        if result[i] < min: min = result[i]
    return min
print(multiple(667, 85))