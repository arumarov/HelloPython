def create_set(n):
    a = []
    res = 1
    for i in range(1, n+1):
        res = res*i
        a.append(res)
    return a
print(create_set(5))