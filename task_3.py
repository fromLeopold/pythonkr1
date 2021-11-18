C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
sum1 = 0
sum2 = 0
for i in C_1:
    sum1 += i
for i in C_2:
    sum2 += i
if sum1 > sum2:
    print('Сумма больше в кортеже:', sum2)
elif sum1 < sum2:
    print('Сумма больше в кортеже:', sum1)
print('max in C_1:', max(C_1), 'min in C_1:', min(C_1))
print('max in C_2:', max(C_2), 'min in C_2:', min(C_2))
