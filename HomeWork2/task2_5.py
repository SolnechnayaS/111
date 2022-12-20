import os
clear = lambda: os.system('clear')
clear()

print("Задача 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.")
n = int(input("Введите число элементов в списке: "))
listN = list(range (n))
print(listN)

import random

randomIterations = random.randint(n, n**3)

for i in range (randomIterations):
    randomPositionChangeOne = random.randint(0, n-1)
    randomPositionChangeTwo = random.randint(-n+1, 0)
    temp = listN [randomPositionChangeOne]
    listN [randomPositionChangeOne] = listN [randomPositionChangeTwo]
    listN [randomPositionChangeTwo] = temp

print(listN)