q = int(input('Количество чисел:'))
c = 0
for i in range (q):
    b = int(input('Число:'))
    c = c + b
v = round(c/q, 2)
print(v)