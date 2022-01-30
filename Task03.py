# Задача 03. Вывести на экран числа от -N до N
def print_numbers(n):
    r = range(-n,n+1) # -8 8
    for i in r:
        print(i)
print(print_numbers(8))