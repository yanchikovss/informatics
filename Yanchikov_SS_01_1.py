'''
Задание 1.
Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R,
который необходимо ввести с клавиатуры в сантиметрах. Результаты должны округляться до сотых.
'''

import math

r = int(input('radius: '))

L = math.pi*r # L - length
S = math.pi*(r**2) # S - square

print('Length: ', round(L, 2,))
print('Square: ', round(S, 2))

'''
Задание 2.
Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных
на экран до и после замены.
'''

import  math

x = 10
y = 55

print('До замены: ', x, y)
x,y = y,x
print('После замены:', x, y)

'''
Задание 3.
Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых. 
Для расчетов использовать формулу T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2).
Значение длины маятника в метрах необходимо ввести с клавиатуры.
'''

import math

L = int(input('Введите длину маятника: '))
g = 9.81
T = 2*math.pi*math.sqrt(L/g)
print('Период колебания: ', round(T, 2))
