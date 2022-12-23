import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
n = int(input("Введите число: "))

print(function_file.prime_factors(n))