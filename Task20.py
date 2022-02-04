# Задача 20. Определить, присутствует ли в заданном списке строк, некоторое число
def check_list(a, b):
    x = str(b)
    for i in range(0, len(a)):
        if x in a[i]:
            res = True
            break
        else: res = False
    return res
a = ['один', 'два', 'три', '4четыре']
b = 4
print(check_list(a, b))