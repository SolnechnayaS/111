import os
clear = lambda: os.system('clear')
clear()

print("Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.")
num = int(input("Введите число: "))

listNum = list()

for i in range (num):
    if i==0:
        listNum.append (1)
    else:
        listNum.insert (i, listNum[i-1]*(i+1))

print(listNum)