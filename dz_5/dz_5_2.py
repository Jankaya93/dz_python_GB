"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
Пример:
2 2
4 
"""

a, b = int(input("Введите первое слагаемое: ")), int(
    input("Введите второе слагаемое: "))


def sum(x, y):
    if x != 0 or y != 0:
        if x < y:
            summa = y + 1
            x -= 1
            y += 1
            if x != 0:
                return (sum(x, y))
        if y < x:
            summa = x + 1
            y -= 1
            x += 1
            if y != 0:
                return (sum(x, y))
    print(f"Результат сложения {a} и {b} равен {summa}")
    return


sum(a, b)
