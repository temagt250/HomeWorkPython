#        Домашняя работа
#   Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
#   Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#   Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#   Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
#   на i-ом кусте выросло i ягод.
#   В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#   Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#   Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
#   собирает ягоды с этого куста и с двух соседних с ним.
#     Напишите программу для нахождения максимального числа ягод, 
#   которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов: ")) # указывем кол-во кустов
list_with_berries = []
max = 0
temp = 0
for i in range(n):
    list_with_berries.append(int(input("Введите количество ягод на кусте: ")))  # указываем сколько ягод будет на одном кусте
    print(list_with_berries)
temp = list_with_berries[0]
for i in range(len(list_with_berries)):  # узнаем сколько машина собрала с половины кустов и находим максимум
    temp = temp + list_with_berries[i]
    if i % 3 == 0:
        if max < temp:
            max = temp  
        temp = 0
        i = 2
list_with_berries.reverse()    # разварачиваем кусты, чтобы узнать сколько машина соберет с другой половины куста
for i in range(len(list_with_berries)):  # узнаем сколько машина собрала с другой половины куста и находим максимум
    temp = temp + list_with_berries[i]
    if i % 3 == 0:
        if max < temp:
            max = temp
        temp = 0
        i = 2
print(max) # выводим максимальное кол-во, за одну сборку(т.е с 3-х кустов)
