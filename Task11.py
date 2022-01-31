# Задача 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def create_list(n):
    a = []
    a.append(1)
    res = 1
    for i in range(1, n):
        res = res*(-3) 
        a.append(res) 
    print(a)
create_list(6)


