# Задача 24. В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def min_max(a):
    max = a[0] - round(a[0])
    for i in range(0, len(a)):
        if (a[i] - round(a[i]) > max):
            max = a[i] - round(a[i])
    min = a[0] - round(a[0])
    for j in range(0, len(a)):
        if(a[j] - round(a[j]) < min and a[j] - round(a[j]) != 0):
            min = a[j] - round(a[j])
    x = float(max-min)
    return x
a = [1.1, 1.4, 3.1, 5, 10.01]
print(min_max(a))