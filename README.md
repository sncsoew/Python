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
Выведите на консоль с помощью индексации строки, последовательно:первый фильм,последний,второй,второй с конца
Решение:
```python
print(my_favorite_movies[:10],my_favorite_movies[41:57],my_favorite_movies[11:25],my_favorite_movies[34:40])
```
