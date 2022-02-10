# Задача 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т. е. для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# Просто Фибоначчи
def fibonacci(k):
    fibo = []
    for i in range(0, k):
        if i <= 1: fibo.append(1)
        else: fibo.append(fibo[i-1] + fibo[i-2])
    return fibo

print(fibonacci(8))

# НегоФибоначчи
def fibonacci(k):
    fibo = []
    for i in range(0, k):
        if i <= 1: fibo.append(1)
        else: fibo.append(fibo[i-1] + fibo[i-2])

    fibo1 = []
    for i in range(0,k*2+1):
        if i < k and i%2 == 0: fibo1.append(fibo[k-1-i]*-1)
        elif i < k and i%2 != 0: fibo1.append(fibo[k-1-i])
        elif i == k: fibo1.append(0)
        elif i > k: fibo1.append(fibo[i-k-1])
    return fibo1

print(fibonacci(8))