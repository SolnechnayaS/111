import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
n = int(input("Введите число элементов в списке: "))

new_list = function_file.random_list(n)
print(new_list)

list_pair = function_file.pair_multiplication (new_list)
print(list_pair)
