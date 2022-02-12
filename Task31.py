# Задача 31. Составить список простых множителей натурального числа N
def list_multi(n,i):
    list = []

    while i <= n:
        if n%i == 0 and i%i == 0:
            list.append(i)
            n = n/i
        else: i = i + 1
    return list

print(list_multi(264, 2))