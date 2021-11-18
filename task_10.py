num1 = int(input('Enter: '))
num1 = str(num1)
chet = 0
nchet = 0
num3 = 0
for i in num1:
    i = int(i)
    if i % 2 == 0:
        chet += 1
    else:
        nchet += 1
if chet > nchet:
    for i in num1:
        num3 += int(i)
    print(num3)
elif chet < nchet:
    num3 = int(num1[0]) * int(num1[2]) * int(num1[5])
    print(num3)
else:
    print('Кол-во четных и нечетных цифр равно')
