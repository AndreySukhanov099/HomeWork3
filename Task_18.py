#Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине 
#элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество 
#элементов в массиве. Последняя строка содержит число X
#*Пример:*
#5
#   1 2 3 4 5
#    6
#    -> 5

n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число x: "))
import random
list_1=[]
list_2=[]
list_1 =[random.randint(0, 1000) for i in range(n)]
for j in list_1:
    list_2.append(abs(x-j))
print(list_1)
ind=(list_2.index(min(list_2)))
print(list_1[ind])
print(x)


