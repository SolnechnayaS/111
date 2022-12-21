import os
clear = lambda: os.system('clear')
clear()

from random import sample

print("Задача 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).")
n = int(input("Введите число элементов в списке: "))

def random_list (len_list):
    new_list = sample (range (1, len_list ** 2), k=len_list)
    return new_list

def sum_odd (new_list, sum=0):
    for i in range (len(new_list)):
        if i%2==0:
            sum += new_list[i]
    return sum

new_list = random_list(n)
print(new_list)
print(sum_odd (new_list))