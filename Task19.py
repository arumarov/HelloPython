# Задача 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# Мое решение (хреновое)
def create_random(a):
    import time
    ft = time.time()
    ran = int(ft * a + a)
    random = str(ran)
    rand = random[7:9]
    rando = int(rand)
    if rando < 20 and rando >= 0: res = random[8] + random[9]
    elif rando > 20 and rando < 40: res = random[8] - random[2]
    elif rando > 40 and rando < 60: res = random[8] + random[3]
    elif rando > 60 and rando < 80: res = random[8] - random[4] 
    elif rando > 80 and rando < 100: res = random[8] + random[5] 
    return res
print(create_random(5))

# Решение с вебинара
import datetime

def get_rand():
    return datetime.datetime.now().microsecond%10

print(get_rand())