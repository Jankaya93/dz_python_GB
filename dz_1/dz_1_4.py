"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

size_n, size_m, quantity = int(input("Введите длинну шоколадки: ")), int(input(
    "Введите ширину шоколадки: ")), int(input("Введите желаемое количество долек: "))

if size_m*size_n >= quantity and (quantity % size_n == 0 or quantity % size_m == 0):
    print("Да, так можно отломить.")
else:
    print("Нет, так нельзя отломить.")