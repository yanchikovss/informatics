'''
Три точки заданы своими координатами X(x1, x2),
Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты
точки, для которой угол между осью абсцисс и лучом,
соединяющим начало координат с точкой, минимальный.
Вычисления оформить в виде процедуры.
'''

def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)

'''
Найти все простые натуральные числа, не превосходящие n
, двоичная запись которых представляет собой палиндром,
т. е. читается одинаково слева направо и справа налево.
'''
n = 1000
lst = [True for _ in range(n+1)]
i = 1
while 2*i*(i + 1) < n:
    j = i
    while j <= (n - i) / (2*i + 1):
        lst[2*i*j + i + j] = False
        j = j + 1
    i = i + 1
for i in range(1, n+1):
    elem = lst[i]
    if elem:
        prime = 2*i + 1
        if prime > n: break
        a = bin(prime)[2:]
        b = bin(prime)[2:][::-1]
        if a == b:
            print(prime, end=' ')
