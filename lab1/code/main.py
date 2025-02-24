from distance_00 import task_0
from circle_01 import task_1
from operations_02 import task_2
from favorite_movies_03 import task_3
from my_family_04 import task_4
from zoo_5 import task_5
from songs_list_06 import task_6
from secret_07 import task_7
from garden_08 import task_8
from shopping_09 import task_9
from store_10 import task_10

def main():
    print('Задание 0:')
    for n,h in task_0().items():
        print(f"\t{n} {h}")
    print('Задание 1:',task_1())
    print('Задание 2:',task_2())
    print('Задание 3:')
    for i in task_3():
        print(f"\t{i}")
    print('Задание 4:',task_4())
    print('Задание 5:')
    for n,h in task_5().items():
        print(f"\t{n}): {h}")
    print('Задание 6:',task_6())
    print('Задание 7:',task_7())
    print('Задание 8:')
    for n,h in task_8().items():
        print(f"\t{n} {h}")
    print('Задание 9:')
    for n,h in task_9().items():
        print(f"\t{n}:")
        for f in h:
            for e,r in f.items():
                print(f"\t\t {r}")
    print('Задание 10:')
    for n,h in task_10().items():
        print(f"\t{n} {h}")
if __name__ == "__main__":
    main()