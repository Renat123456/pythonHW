# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first = int(input("Введите первый элемент прогрессии: "))
step = int(input("Введите шаг прогрессии: "))
quantity = int(input("Введите количество элементов прогрессии: "))

progression = [first]

for i in range(0, quantity - 1):
    next_num = progression[i] + step
    progression.append(next_num)

print(*progression)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

n= random.randint(10,20)
list_1 = [random.randint(-10,10) for i in range(n)]
print(list_1)

min_num = int(input("Введите минимум: "))
max_num = int(input("Введите максимум: "))
list_2 = []

for i in range(len(list_1)):
    if list_1[i] >= min_num and list_1[i] <= max_num:
        list_2.append(i)

print(list_2)