#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число x: "))
count =0
import random
list_1=[]
list_1 =[random.randint(0,9) for i in range(n)]
for j in list_1:
    if j == x:
        count +=1
print(list_1)
print(x)
print(count)