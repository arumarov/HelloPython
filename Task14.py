# Задача 14. Подсчитать сумму цифр в вещественном числе
def sum_digits(a):
    b = str(a)
    c = b.replace('.', '')
    sum = 0
    for i in range(0, len(c)):
        sum = int(c[i]) + sum
    return sum
print(sum_digits(697.18755))