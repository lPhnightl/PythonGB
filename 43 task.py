#43.Написать программу преобразования десятичного числа в двоично

num = int(input('Введите число '))

def IntToBin(num):
    str = ''
    while num >=1:
        str = str + f'{num%2}'
        num = num//2
    return str


def reversedi(variable):
    res=''.join(reversed(variable))
    return res 

print(reversedi(IntToBin(num)))







 


