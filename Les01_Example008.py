# 2.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3


print('Введите координату X: ')
x = int(input())

while x == 0:
    print('Координата Х не должна быть равна 0, введите её заново:')
    x = int(input())

print('Введите координату Y: ')
y = int(input())

while y == 0:
    print('Координата Y не должна быть равна 0, введите её заново:')
    y = int(input())

if y >0 and x >0:
    print (f'Точка, с координатами ({x},{y}) лежит в 1-й четверти')

if y >0 and x <0:
    print (f'Точка, с координатами ({x},{y}) лежит в 2-й четверти')

if y <0 and x <0:
    print (f'Точка, с координатами ({x},{y}) лежит в 3-й четверти')

if y <0 and x >0:
    print (f'Точка, с координатами ({x},{y}) лежит в 4-й четверти')