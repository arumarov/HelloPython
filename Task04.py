# Задача 04. Показать первую цифру дробной части числа
def show_one(a):
     b = a - round(a) # ок
     c = b*10 # ок
     f = (b+1)*10 # ок
     e = str(c)
     d = str(f) # 
     if b > 0: res = e[0]
     elif b < 0: res = d[0]
     return res
a = 12.273
print(show_one(a))