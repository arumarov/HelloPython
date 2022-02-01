# Задача 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
def create_list(n):
    a = []
    for i in range(1, n+1):
        res = (1+1/i)**i
        a.append(res)
    sum = a[0]
    for j in range(1, n):
        sum = sum + a[j]
    return sum
print(create_list(6))


