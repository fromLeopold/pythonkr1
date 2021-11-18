menu = {"торт": ["сладенькое", 15, 9678],
        "пирожное": ["более сладенькое", 56, 5467],
        "маффин": ["пипяу как сладенько", 23, 8979]}
sweet_menu = []
for i in menu:
    print(i)
    sweet_menu.append(i)
while True:
    print('1.посмотреть описание\n2.посмотреть цену\n3.посмотреть количество\n4.посмотреть всю информацию\n5.приступить к покупке\n6.до свидания')
    act = input('Выберите действиее: ')
    cost = 0
    if act == '1':
        for j in sweet_menu:
            print(f'{j}: {menu[j][0]}')
    elif act == '2':
        for j in sweet_menu:
            print(f'{j}: {menu[j][1]}')
    elif act == '3':
        for j in sweet_menu:
            print(f'{j}: {menu[j][2]}')
    elif act == '4':
        for j in sweet_menu:
            print(f'{j}: {menu[j]}')
    elif act == '5':
        cost = 0
        while True:
            try:
                sweet = input('Введите название десерта: ')
                numb = int(input('Введите количество: '))
                if numb >= menu[sweet][2]:
                    cost += menu[sweet][1] / 100 * numb
                    menu[sweet][2] = menu[sweet][2] - numb
                else:
                    cost += menu[sweet][1] / 100 * menu[sweet][2]
                    del menu[sweet]
            except (KeyError):
                print('Такого десерта нет в меню')
            else:
                c = input('Еще? ')
                if c == 'да':
                    continue
                else:
                    break
            break
    elif act == '6':
        print('Хорошего дня')
        break
    print(f'К оплате: {cost}')