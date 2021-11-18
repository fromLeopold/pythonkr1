from random import randint
num1 = int(input('Сколько чисел: '))
for i in range(num1):
    num2 = int(input('Введите цифру: '))
    rand_num = randint(1, 1000)
    print(rand_num)
    num2 = str(num2)
    rand_num = str(rand_num)
    print(f'{rand_num.count(num2)} раз')
