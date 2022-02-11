# Задача 30. Вычислить число П c заданной точностью d
# Пример: при d = 0.001, П = 3.141.10^-1 <= d <= 10^-10

def pi(d):
    import decimal
    b = decimal.Decimal(str(d))
    x = (b.as_tuple().exponent*-1)
    print(x)
    a, i = 4, 1
    for i in range (0,10):
        b, p = 3, 0
        p = p + a/(i+1*i+2*i+3) - a/(i+3*i+4*i+5)
    pi = p + b
    return round(pi, x)

print(pi(0.00000000000000000000000001))