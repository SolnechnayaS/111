print('4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
quarterNumber = int(input('Введите номер четверти: '))
if quarterNumber==1:
    print ('Координаты x>0 и y>0')
elif quarterNumber==4:
    print ('Координаты x>0 и y<0')
elif quarterNumber==2:
    print('Координаты x<0 и y>0')
elif quarterNumber==3:
    print('Координаты x<0 и y<0')
else:
    print('Четверть с таким номером не существует')