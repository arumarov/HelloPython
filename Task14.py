# Задача 14. Подсчитать сумму цифр в вещественном числе
# Мое решение
def sum_digits(a):
    b = str(a)
    c = b.replace('.', '')
    sum = 0
    for i in range(0, len(c)):
        sum = int(c[i]) + sum
    return sum
print(sum_digits(697.18755))

# Решение с семинара
def sum_of_number(a):
    res = 0
    for i in str(a):
        if i != '.': res += int(i)
    return res
print(sum_of_number(697.18755))