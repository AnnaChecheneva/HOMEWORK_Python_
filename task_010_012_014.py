print("Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть")

n_token = int(input("Enter a count of token---> "))
reshka = 0
orel = 0
for n in range(n_token):
    print(n+1,".")
    value_token = int(input("Enter 0 or 1--->"))
    if value_token == 0:
        reshka +=1
    else: orel +=1
if reshka > orel: print("flip", orel, "gerb coins")
else: print("flip ", reshka, "tails coins")
    
s = input()

print("Задача 12: Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.")

S, P = int(input("Петя дал подсказку, сумма X Y равна --> ")), int(input("Петя дал подсказку, призведение X Y равно --> "))

for i in range(S):
    for j in range(P):
        if S == i + j and P == i * j:
            print(i, j)

s = input()

print("Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
N = int(input("Введите число до какого возводить степень 2--> "))
degree_tw = 1
for i in range(1000):
     if degree_tw*2 > N:
        break
     else:
         degree_tw *= 2
         print(i+1, ")", degree_tw)
    



