# Задача 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
def create_list(n, b):
    a = []
    r = range(-n, n)
    for i in r:
        res = -n + i - 1
        a.append(res)
    with open('file.txt', 'r') as data:
        lines = data.readlines()
        x = int(lines[0])
    return a[x]
print(create_list(5, 5))