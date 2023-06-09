"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
size = int(input("Введите количество монеток: "))
orel = 0
reshka = 0

for _ in range(size):
    monety = random.randint(0, 1)
    print(monety, end=" ")

    if monety == 0:
        orel += 1
    else:
        reshka += 1

if orel < reshka:
    print (f"\n Минимально нужно превернуть {orel} монет.")
elif orel > reshka:
    print (f"\n Минимально нужно превернуть {reshka} монет.")
else:
    print (f"\n Количество монет лежащих орлом и решкой одинаково.")