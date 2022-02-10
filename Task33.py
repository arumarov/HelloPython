# Задача 33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def polynomial(k):
    import random
    a = random.randint(0,100)
    b = random.randint(0,100)

    with open('file_Task33.txt', 'w') as data:
        data.write(str(a) + '*x^' + str(5) + '+' + str(b) + '*x = 0')

polynomial(5)
