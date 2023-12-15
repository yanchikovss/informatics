'''
1. Дан двумерный массив размером 3x3. Определить максимальное значение
среди элементов третьего столбца массива; максимальное значение среди элементов
второй строки массива. Вывести полученные значения.
'''

n = 3
arr = []
print('Введите элементы массива:')

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print('Массив имеет вид:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '')
    print()

max_third = max(arr[0][2], arr[1][2], arr[2][2])
max_second = max(arr[1][0], arr[1][1], arr[1][2])

print('Максимальное значение в третьем столбце:', max_third)
print('Максимальное значение во второй строке:', max_second)

'''
2. Дан двумерный массив размером mxn.
Сформировать новый массив заменив положительные элементы единицами,
а отрицательные нулями. Вывести оба массива.
'''

m = int(input('Введите количество строк массива:'))
n = int(input('Введите количество столбцов массива:'))
arr = []
print('Введите элементы массива:')

for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)
print('Исходный массив имеет вид:')

for i in range(m):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()

for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            arr[i][j] = 1
        if arr[i][j] < 0:
            arr[i][j] = 0

print('Новый массив имеет вид:')
for i in range(m):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()

'''
3. Дана целая квадратная матрица n-го порядка.
Определить, является ли она магическим квадратом, т. е. такой матрицей,
в которой суммы элементов во всех строках и столбцах одинаковы.
'''

n = int(input("Введите порядок квадратной матрицы: "))
arr = []
print("Введите элементы матрицы:")

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print('Матрица имеет вид:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '  ')
    print()

sum_arr = sum(arr[0])
magic_square = True
col_sum = sum(arr[j])

for i in range(n):
    if sum(arr[i]) != sum_arr:
        magic_square = False
        break

for j in range(n):
    if col_sum != sum_arr:
        magic_square = False
        break

if magic_square:
    print("Это магический квадрат")
else:
    print("Это не магический квадрат")

'''
4. Определить, является ли заданная целая квадратная матрица
n-го порядка симметричной (относительно главной диагонали).
'''

n = int(input("Введите порядок квадратной матрицы: "))
arr = []
print("Введите элементы матрицы:")

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print('Матрица имеет вид:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '  ')
    print()

arr_symmetric = True
for i in range(n):
    for j in range(i, n):
        if arr[i][j] != arr[j][i]:
            arr_symmetric = False
            break

if arr_symmetric:
    print("Матрица симметрична относительно главной диагонали")
else:
    print("Матрица не симметрична относительно главной диагонали")
