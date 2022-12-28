# ** 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0 
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!

import os
clear = lambda: os.system('clear')
clear()

import function_file

print("Задача 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.")

temp_name_number1 = int(input("Какой файл будем открывать первым? 1 - poly.txt, 2 - poly2.txt, 3 - другой (ввести): "))
name_file1 = function_file.temp_name (temp_name_number1)

temp_name_number2 = int(input("Какой файл будем открывать вторым? 1 - poly.txt, 2 - poly2.txt, 3 - другой (ввести): "))
name_file2 = function_file.temp_name (temp_name_number2)

def read_file (name_file):
    file = open(name_file, 'r')
    list_lines_file1 = file.readlines()
    file.close()
    return list_lines_file1

def count_lines_file (name_file):
    file = open(name_file, 'r')
    lines = 0
    for line in file:
        lines +=1
    file.close()
    return lines

def addition_polynomials (name_file1, name_file2):
    len_file1 = count_lines_file (name_file1)
    len_file2 = count_lines_file (name_file2)
    list_lines_file1 = read_file (name_file1)
    list_lines_file2 = read_file (name_file2)
    list_polynomial_result = []

    name_file3 = str(input('Введите имя результирующего файла в формате "*.txt": '))
    with open (name_file3, "a", encoding="utf-8") as polynomial_result:
        if len_file1 !=len_file2:
                print("Файлы содержат разное количество многочленов, сложению не подлежат")
        else:
            for i in range (len_file1):
                list_polynomial_result.append(list_lines_file1[i].replace("=0\n","+")+list_lines_file2[i])
            polynomial_result.write("".join(list_polynomial_result).replace("+-","-"))
    print(f'\nРезультат выведен в файл {name_file3}\n{"".join(list_polynomial_result).replace("+-","-")}')

addition_polynomials (name_file1, name_file2)