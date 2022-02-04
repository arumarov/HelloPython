# Задача 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
def product_numbers(a):
    b = []
    for i in range(0, len(a)-1):
        if i < (len(a)/2):
            res = (a[i] * a[len(a)-1-i])
            b.append(res)
        elif (i == len(a)/2-0.5):
            res = a[i] * a[i]
            b.append(res)
            break
    return b
a = [2, 3, 4, 5, 6, 6, 4]
print(product_numbers(a))