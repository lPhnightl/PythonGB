# 19. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
import time

def Randomaizer ():
    return time.time()%10

print(Randomaizer())