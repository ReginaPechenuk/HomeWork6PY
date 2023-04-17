# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
def FillArray (arraySize):
    array = []
    for i in range (arraySize):
        num = randint(1,10)
        array.append(num)
    return array


list_1 = []

def ArrayINDiapazone (array, start, finish):
    for i in range (0,num):
        if start < array[i] < finish:
            list_1.append(i)
    return list_1



num = int(input('Введите количество элементов массива = '))
my_start = int(input('Введите начало диапазона = '))
my_finish = int(input('Введите конец диапазона = '))
array1 = FillArray(num)
list_2 = ArrayINDiapazone(array1,my_start,my_finish)
print(array1)
print('Индексы элементов массива (списка), значения которых принадлежат заданному диапазону :')
print(list_2)