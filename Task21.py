# Задача 21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет
def pos_string(a):
    x = a[0] # один
    for i in range(0, len(a)):
        x = a[i] # один 
        for j in range(0, len(a)):
            if a[j] == x and j > i: # один 
                res = j 
            else:
                res = None
        return res
a = ['один', 'два', 'три', 'три', 'пять']
print(pos_string(a))

# a = ['один', 'два', 'три', 'три', 'пять']
# x = a[0]
# for i in range(0, len(a)):
#     # print(a[i])
#     # print(i)
#     for j in range(0, len(a)):
#         if x == a[j] and j > i:
#             print(a[j])
#     print()