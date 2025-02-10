# Python
## Задание 1
Составить словарь словарей расстояний между городами\
Решение:
```python
distances = {'Moscow':{'London':(((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5),
                       'Paris':(((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5)},
             'Paris':{'London':(((sites['Paris'][0] - sites['London'][0]) ** 2 + (sites['Paris'][1] - sites['London'][1]) ** 2) ** 0.5),
                      'Moscow':(((sites['Paris'][0] - sites['Moscow'][0]) ** 2 + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5)},
             'London':{'Paris':(((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5),
                       'Moscow':(((sites['London'][0] - sites['Moscow'][0]) ** 2 + (sites['London'][1] - sites['Moscow'][1]) ** 2) ** 0.5)}
             }
```
## Задание 2
Найти площадь круга и вывести\
Решение:
```python
print(round(3.1415926*radius**2,4))
```
Если точка point лежит внутри круга ,то вывести на консоль True, Или False, если точка лежит вовне круга.\
Решение:
```python
print((((0 - 23) ** 2 + (0 - 34) ** 2) ** 0.5)<radius)
```
Если точка point_2 лежит внутри круга , то вывести на консоль True,Или False, если точка лежит вовне круга.\
Решение:
```python
print((((0 - 30) ** 2 + (0 - 30) ** 2) ** 0.5)<radius)
```
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







