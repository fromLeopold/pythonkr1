while True:
    try:
        cookie = int(input('Сколько печенек ты мне принес? '))
        if cookie < 5:
            raise BaseException("VERY FEW COOKIES")
    except (BaseException):
        print("Я думаю, что надо больше печенек")
    else:
        print('Спасибо за печеньки•~•')
        break
