#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': 
    [
        {'quantity': 27, 'price': 42},
    ],
    '23456': 
    [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': 
    [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': 
    [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price


# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']+store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']+store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']+store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']+store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

lamps_quantity=store[goods['Лампа']][0]['quantity']
table_quantity=store[goods['Стол']][0]['quantity']+store[goods['Стол']][1]['quantity']
sofa_quantity=store[goods['Диван']][0]['quantity']+store[goods['Диван']][1]['quantity']
chair_quantity=store[goods['Стул']][0]['quantity']+store[goods['Стул']][1]['quantity']+store[goods['Стул']][2]['quantity']

def task_10_1():
    ##print('цена лампы:',store[goods['Лампа']][0]['price'])
    ##print('цена стола:',store[goods['Стол']][0]['price'],',',store[goods['Стол']][1]['price'])
    ##print('цена дивана:',store[goods['Диван']][0]['price'],',',store[goods['Диван']][1]['price'])
    ##print('цена стула:',store[goods['Стул']][0]['price'],',',store[goods['Стул']][1]['price'],',',store[goods['Стул']][2]['price'])
    return [f"цена лампы: {store[goods['Лампа']][0]['price']}",
            f"цена стола: {store[goods['Стол']][0]['price']}, {store[goods['Стол']][1]['price']}",
            f"цена дивана: {store[goods['Диван']][0]['price']}, {store[goods['Диван']][1]['price']}",
            f"цена стула: {store[goods['Стул']][0]['price']}, {store[goods['Стул']][1]['price']}, {store[goods['Стул']][2]['price']}"]
def task_10_2():
    ##print('лампа -',lamps_quantity,'шт,','стоимость', lamps_cost,'руб')
    ##print('стол -',table_quantity,'шт,','стоимость', table_cost,'руб')
    ##print('диван -',sofa_quantity,'шт,','стоимость', sofa_cost,'руб')
    ##print('стул -',chair_quantity,'шт,','стоимость', chair_cost,'руб')
    return [f"лампа - {lamps_quantity} шт,стоимость {lamps_cost} руб",
            f"стол - {table_quantity} шт,стоимость {table_cost} руб",
            f"диван - {sofa_quantity} шт,стоимость {sofa_cost} руб",
            f"стул - {chair_quantity} шт,стоимость {chair_cost} руб"]