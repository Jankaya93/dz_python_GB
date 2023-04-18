"""
*Задача 20: 
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
*Пример:*
ноутбук
12
"""
liter_1 = 'AEIOULNSTRАВЕИНОРСТ'
liter_2 = 'DGДКЛМПУ'
liter_3 = 'BCMPБГЁЬЯ'
liter_4 = 'FHVWYЙЫ'
liter_5 = 'KЖЗХЦЧ'
liter_8 = 'JXШЭЮ'
liter_10 = 'QZФЩЪ'

dictionary = dict.fromkeys(liter_1, 1) | dict.fromkeys(liter_2, 2) | dict.fromkeys(liter_3, 3) | dict.fromkeys(
    liter_4, 4) | dict.fromkeys(liter_5, 5) | dict.fromkeys(liter_8, 8) | dict.fromkeys(liter_10, 10)

slovo = input("Введите слово: ").upper()
total = 0

for i in range(len(slovo)):
    for j in dictionary:
        if slovo[i] == j:
            total += dictionary[j]
print("Ваше слово набрало", total, "баллов")