

# a = random.randint(1,22)
# print(a)
import random
b = random.randint(1,22)
print(b)
a = random.randint(100,999)
print(a)
print(a//10%10)

# #11. Дано число из отрезка [10,99]. Показать наибольшую цифру числа

# a = random.randint(10,100)
# print(f'a = {a}')

#15.Дано число. Проверить кратно ли оно 7 и 23
a = random.randint(1,100)

print(a)
def qratnosti(a):
    return a%7==0 and a%23==0
    
result = qratnosti(a)
print(result)