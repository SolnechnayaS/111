# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
clear = lambda: os.system('clear')
clear()

import function_file
from decimal import Decimal, getcontext

print("Вычислить число c заданной точностью d: ")
n = Decimal(input("Введите вещественное число, которое необходимо округлить: "))
m = Decimal(input("Введите точность округления в формате 0.000001: "))

print(function_file.decimal_num (n, m))