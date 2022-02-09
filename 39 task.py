#39. Найти произведение пар чисел в одномерном массиве. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

arr = []
def Creatlist(list):
    for i in range(random.randint(1,10)):
        list.append(random.randint(-10,10))
    return list

def multiplication(list):
    res = []
    for i in range(len(list)//2):
        res.append(list[i]*list[len(list)-i-1])
    return res

CreatList = Creatlist(arr)
print(f'Собранный массив{CreatList}')
print(f'Произведенние пар чисел {multiplication(CreatList)}')