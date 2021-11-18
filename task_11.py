tekst1 = input('Enter: ')
glas1 = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
sign1 = ['/', '*', '-', '+', ',', '.', ' ']
glas2 = 0
glas3 = ''
sogl = 0
for i in tekst1:
    if i in glas1:
        glas2 += 1
        glas3 += i + ' '
    elif i in sign1:
        continue
    elif i.isdigit():
        continue
    else:
        sogl += 1
if glas2 == sogl:
    print(glas3)
else:
    print(f'Гласные: {glas2}; Согласные: {sogl}')
