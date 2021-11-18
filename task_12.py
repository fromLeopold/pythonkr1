from random import randint
counter_1 = 0
numb1 = 0
numb2 = 0
for i in range(7):
    num1 = int(input('Enter: '))
    num2 = int(input('Enter: '))
    num3 = randint(1, 20)
    num4 = randint(1, 20)
    print(num1, num2, '\n', num3, num4)
    if i == 3:
        numb1 = num3
        numb2 = num4
    if num1 + num2 > num3 + num4:
        counter_1 += 1
if counter_1 <= 3:
    print(numb1, numb2)
else:
    print(f'{counter_1} раз')
