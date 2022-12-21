import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
n = int(input("Введите число элементов списка: "))

list_float = function_file.random_list_float(n)
print(list_float)

function_file.fractional_part(list_float)