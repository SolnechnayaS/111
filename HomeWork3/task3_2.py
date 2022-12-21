import os
clear = lambda: os.system('clear')
clear()

print("Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
n = int(input("Введите число элементов в списке: "))

import function_file

new_list = function_file.random_list(n)
print(new_list)

list_pair = function_file.pair_multiplication (new_list)
print(list_pair)
