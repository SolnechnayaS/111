import os
clear = lambda: os.system('clear')
clear()

print("Задача 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму")
n = int(input("Введите число: "))

listNum = list()
sum = 0

for n in range (1, n+1):
        listNum.append ((1 + 1/n) ** n)
        sum= sum+listNum[n-1]

print(listNum)
print(sum)