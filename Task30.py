# Задача 30. Вычислить число П c заданной точностью d
# Пример: при d = 0.001, П = 3.141.10^-1 <= d <= 10^-10

def pi(d):
    import decimal
    b = decimal.Decimal(str(d))
    x = (b.as_tuple().exponent*-1)
    a = 4
    p, l = 0, 0
    for i in range (0,500):
        b = 3
        p = p + a/(l+2*l+3*l+4) - a/(l+4*l+5*l+6)
        l = l + 4
    pi = p + b
    return round(pi, x)

print(pi(0.000000001))