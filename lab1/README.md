# Python
## Задание 1
Составить словарь словарей расстояний между городами\
Ответ:
![](img/Screenshot_1.png)
## Задание 2
1.Найти площадь круга и вывести.\
2.Если точка point лежит внутри круга ,то вывести на консоль True, Или False, если точка лежит вовне круга.\
3.Если точка point_2 лежит внутри круга , то вывести на консоль True,Или False, если точка лежит вовне круга.\
Ответ:\
![](img/Screenshot_2.png)
## Задание 3
Расставьте знаки операций "плюс", "минус", "умножение" и скобкимежду числами "1 2 3 4 5" так, что бы получилось число "25".\
Решение:
```python
print(1*(2+3)+4*5)
```
## Задание 4
Есть строка с перечислением фильмов
```python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
```
Выведите на консоль с помощью индексации строки, последовательно:первый фильм,последний,второй,второй с конца.\
Решение:
```python
print(my_favorite_movies[:10],my_favorite_movies[41:57],my_favorite_movies[11:25],my_favorite_movies[34:40])
```
## Задание 5
Создать список роста членов моей семьи и вывести рост отца, общий рост семьи.\
Решение:
```python
my_family_height = [
    ['мать',170],
    ['отец',180],
    ['брат',180]
]
print('Рост отца -',my_family_height[1][1],'см')
print('Общий рост моей семьи -',my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1],'см')
```
## Задание 6
Есть список животных в зоопарке
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
```
Посадить медведя (bear) между львом и кенгуру и вывести список на консоль\
Решение:
```python
zoo.insert(1,'bear')
print(zoo)
```
Добавить птиц из списка birds в последние клетки зоопарка
```python
birds = ['rooster', 'ostrich', 'lark', ]
```
Решение:
```python
zoo.extend(birds)
print(zoo)
```
Убрать слона вывести список на консоль\
Решение:
```python
zoo.remove('elephant')
print(zoo)
```
Вывести на консоль в какой клетке сидит лев (lion) и жаворонок (lark).\
Решение:
```python
print(zoo.index('lion')+1,zoo.index('lark')+1)
```
## Задание 7
Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
```
Распечатать общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'\
Решение:
```python
time_1=violator_songs_list[3][1]+violator_songs_list[5][1]+violator_songs_list[8][1]
print('Три песни звучат',round(time_1,2),'минут')
```
Есть словарь песен группы Depeche Mode
```python
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
```
Распечатать общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'\
Решение:
```python
time_2=violator_songs_dict['Sweetest Perfection']+violator_songs_dict['Policy of Truth']+violator_songs_dict['Blue Dress']
print('А другие три песни звучат',round(time_2),'минут')
```
## Задание 8
Есть зашифрованное сообщение
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
```
Нужно его расшифровать и вывести на консоль в удобочитаемом виде.\
Решение:
```python
print(secret_message[0][3:4],
      secret_message[1][9:13],
      secret_message[2][5:15:2],
      secret_message[3][12:6:-1],
      secret_message[4][20:15:-1]
      )
```
## Задание 9
```python
в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
```
Создать множество цветов, произрастающих в саду и на лугу\
Решение:
```python
garden_set={'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза'}
meadow_set ={'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка'}
```
```python
выведите на консоль все виды цветов
print(garden_set.union(meadow_set))

выведите на консоль те, которые растут и там и там
print(garden_set.intersection(meadow_set))

выведите на консоль те, которые растут в саду, но не растут на лугу
print(garden_set.difference(meadow_set))

выведите на консоль те, которые растут на лугу, но не растут в саду
print(meadow_set.difference(garden_set))
```
## Задание 10
Есть словарь магазинов с распродажами.
```python
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
```
Создать словарь цен на продукты\
Решение:
```python
sweets = {
    'печенье': 
    [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    'конфеты':
    [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель':
    [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное':
    [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]
}
```
## Задание 11
Есть словарь кодов товаров
```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
```
Есть словарь списков количества товаров на складе.
```python
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
```
Вывести стоимость каждого вида товара на складе: один раз распечать сколько всего столов и их общая стоимость, один раз распечать сколько всего стульев и их общая стоимость, и т.д. на складе.\
Решение:
```python
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']+store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']+store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']+store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']+store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

lamps_quantity=store[goods['Лампа']][0]['quantity']
table_quantity=store[goods['Стол']][0]['quantity']+store[goods['Стол']][1]['quantity']
sofa_quantity=store[goods['Диван']][0]['quantity']+store[goods['Диван']][1]['quantity']
chair_quantity=store[goods['Стул']][0]['quantity']+store[goods['Стул']][1]['quantity']+store[goods['Стул']][2]['quantity']

print('цена лампы:',store[goods['Лампа']][0]['price'])
print('цена стола:',store[goods['Стол']][0]['price'],',',store[goods['Стол']][1]['price'])
print('цена дивана:',store[goods['Диван']][0]['price'],',',store[goods['Диван']][1]['price'])
print('цена стула:',store[goods['Стул']][0]['price'],',',store[goods['Стул']][1]['price'],',',store[goods['Стул']][2]['price'])

print('лампа -',lamps_quantity,'шт,','стоимость', lamps_cost,'руб')
print('стол -',table_quantity,'шт,','стоимость', table_cost,'руб')
print('диван -',sofa_quantity,'шт,','стоимость', sofa_cost,'руб')
print('стул -',chair_quantity,'шт,','стоимость', chair_cost,'руб')
```
