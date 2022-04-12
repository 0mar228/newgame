import math
q = int(input('1 катет'))
w = int(input('2 катет'))
e = q**2 + w**2
d = math.sqrt(q**2 + w**2)
v = round(d,3)
print('Гипотенуза:', v)