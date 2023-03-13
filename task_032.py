# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_list = [random.randint(-20, 20) for _ in range(int(input("Введите размер массива---> ")))]
print(my_list)
min_it, max_it = int(input("Введите нижнюю границу диапозона----> ")),int(input("Введите верхнюю границу диапозона---> "))
range_list = [my_list.index(i)  for i in my_list if min_it < i < max_it ]
print(range_list)
