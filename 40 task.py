#40. В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.uniform(-100,100))
    return list

def FindMax (list):
    max = 0
    for i in list:
        if i>max: 
            max = i
    return max

def FindMin (list):
    min = 0
    for i in list:
        if i<min: 
            min= i
    return min


filled_list = Filling(12)
print(filled_list)

min_value = min(filled_list)
print(f'min = {min_value}')

max_value = max(filled_list)
print(f'max = {max_value}')

print(f'{FindMax(filled_list)} - {FindMin(filled_list)} = {FindMax(filled_list)-FindMin(filled_list)}')

