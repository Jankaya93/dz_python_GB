"""
Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""
n = int(input("Введите число-ограничитель: "))
i = 0
while 2 ** i <= n:
    # выводим число 2 в степени i, прока произведение не превышает ограничения
    print(2 ** i, end=" ")
    i += 1
