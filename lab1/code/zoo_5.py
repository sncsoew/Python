#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def task_5():
    # есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
    # посадите медведя (bear) между львом и кенгуру
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo.insert(1,'bear')
    zoo1=zoo.copy()
    ## print(zoo1)
    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo.extend(birds)
    zoo2=zoo.copy()
    ## print(zoo)
    # уберите слона
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo.remove('elephant')
    zoo3=zoo.copy()
    ## print(zoo)
    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть понятны простому человеку, не программисту.
    # TODO здесь ваш код
    ## print(zoo.index('lion')+1,zoo.index('lark')+1)

    return [zoo1,zoo2,zoo3,zoo.index('lion')+1,zoo.index('lark')+1]


