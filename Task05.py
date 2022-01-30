# Задача 05. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
def check(a):
    res = False
    if a%5 == 0 and (a%10 == 0 or a%15 == 0) and a != 30: res = True
    return res
print(check(45))