import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Негафибоначчи")
n = int(input("Введите число элементов списка: "))

print(function_file.negafibonacci(n))