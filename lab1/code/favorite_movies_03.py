#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def task_3():
    # Есть строка с перечислением фильмов

    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    # Выведите на консоль с помощью индексации строки, последовательно:
    #   первый фильм
    #   последний
    #   второй
    #   второй с конца

    # Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
    # Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
    # как указано в задании!

    # TODO здесь ваш код
    ##print(my_favorite_movies[:10],my_favorite_movies[41:57],my_favorite_movies[11:25],my_favorite_movies[34:40])
    return my_favorite_movies[:10],my_favorite_movies[41:57],my_favorite_movies[11:25],my_favorite_movies[34:40]