"""
Задача 18: 
Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
Если таких элементов несколько, вы вывести один любой. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X
Пример:
5
    7 -2 3 5 1
    6
    -> 7
"""

import random

n = int(input("Введите количество элементов массива: "))
x = int(input("Введите искомое чило: "))

arr = [random.randint(-10, 10) for i in range(n)]
print(arr)


for j in range(100):
    for i in range(0,len(arr)):
        if arr[i] + j == x or arr[i] - j == x:
            print(arr[i])
            break
    else:
        continue
    break
else:
    print("Решения с такими условиями не существует.")
