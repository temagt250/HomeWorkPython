#    Домашняя работа
#  Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#  Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#  m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите число n: ")) #первое число
m = int(input("Введите число m: ")) #второе число
list_n = [] # список первого числа
list_m = [] # список второго числа
for i in range(n):
    list_n.append(int(input("Введите число для списка n (list_n): "))) # добавление числа
for i in range(m):
    list_m.append(int(input("Теперь, введите число для списка m (list_m): ")))
print(list_n,list_m) # вывод первого и второго списка(для удобства)
print((set(list_n)).intersection(set(list_m))) # перевод в set и слияние(intersection) и вывод

"Если нужно без скобок:"
#set_of_numbers = str()
#for i in ((set(list_n)).intersection(set(list_m))):
#    set_of_numbers += f" {i}"
#print (set_of_numbers)