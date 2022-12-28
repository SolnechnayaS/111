import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.")
print("(Последовательность будет сформирована из простых множителей введенного числа)")
n = int(input("Введите число: "))

print("Исходная последовательность - простые множители введенного числа: ")
first_list = function_file.prime_factors(n)
print(first_list)


print("Уникальные элементы введенной последовательности: ")
list_unique_elements = function_file.list_unique_elements(first_list)
print(list_unique_elements)