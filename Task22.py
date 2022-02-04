# Задача 22. Найти сумму чисел списка стоящих на нечетной позиции
def sum_numbers(a):
    sum = 0
    for i in range(0, len(a)):
        if i%2 > 0:
            sum = sum + a[i]
    return sum
a = [9, 12, 6, 41, 192, 1]
print(sum_numbers(a))