# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# Рассчитать на какую сумму лежит каждого товара на складе
# TODO здесь ваш код
# list_goods = goods.keys()
for i in goods:
    code = goods[i]
    price = 0
    quantity = 0
    for j in store[code]:
        price += j['price']
        quantity += j['quantity']
    print(f'{i}: кол-во - {quantity}шт; цена - {price}руб')
