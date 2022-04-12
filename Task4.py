import math
q = int(input('Введите угол A'))
a = math.radians(q)
n = math.sin(a)
g = round(n, 3)
print('Синуc:',g)
m = math.cos(a)
l = round(m, 3)
print('Косинус:',l)
c = g/l
h = round(c, 3)
print('Тангенс:',h)
d = l/g
f = round(d, 3)
print('Котангенс:',f)