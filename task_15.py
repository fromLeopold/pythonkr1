word1 = input('Enter: ')
counter_1 = 0
counter_2 = 0
sum = ''
for i in range(len(word1) - 1):
    sum = word1[i] + word1[i + 1]
    if not sum.isalpha():
        continue
    if sum.isupper():
        counter_1 += 1
    elif sum.islower():
        counter_2 += 1
print(f'Пары верхнего: {counter_1};Пары нижнего: {counter_2}')
