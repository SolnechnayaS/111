import os
clear = lambda: os.system('clear')
clear()

print("Задача 4. Напишите программу, которая принимает на вход 2 числа. Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).")
n = int(input("Введите число N: "))
one = int(input("Введите число на 1-ой позиции: ")) - 1
two = int(input("Введите число на 2-ой позиции: ")) - 1

listN = list(range (-n, n+1))
print(listN)

if one in range (n*2+1) and two in range (n*2+1):
    product = listN[one]*listN[two]
    print(product)
else:
    print("Указанные позиции отсутствуют в списке")