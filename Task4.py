import math
q = int(input('Введите угол A'))
a = math.radians(q)
n = math.sin(a)
print('Синуc:',n)
m = math.cos(a)
print('Косинус:',m)
c = n/m
print('Тангенс:',c)
d = m/n
print('Котангенс:',d)