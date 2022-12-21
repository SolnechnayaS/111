import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без использования встроенной функции преобразования, без строк.")
n = int(input("Введите число: "))

new_list = function_file.binary(n)
print(new_list)