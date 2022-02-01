# Задача 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ] 
def create_set(n):
    a = []
    res = 1
    for i in range(1, n+1):
        res = res*i
        a.append(res)
    return a
print(create_set(5))