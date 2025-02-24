import itertools
def task_1():

    """
    Выводит количесвто вариации кодов из букв Н А С Т Я

    Должен вернуть
    >>> task_1()
    'Количество допустимых кодов: 6075'
    """

    letters = ['Н','А', 'С', 'Т', 'Я']
    vowels = ['А', 'Я']
    valid_codes_count = 0

    for code in itertools.product(letters, repeat=6):
        if code.count('А') <= 1 and code.count('Я') <= 1:
            valid_codes_count += 1
            
    return(f"Количество допустимых кодов: {valid_codes_count}")

def task_2():

    """
    Выводит количество 3 в записи числа
    >>> task_2()
    'Количество цифр 3 в записи числа: 37'
    """

    value = (16 ** 15) * (4 ** 10) - 46 - 16

    base_4_digits = []
    while value > 0:
        base_4_digits.append(value % 4)
        value = value // 4
    count_3 = base_4_digits.count(3)

    return(f"Количество цифр 3 в записи числа: {count_3}")

def task_3():
    
    """
    Выводит число и сумму его максимального и минимального делителя
    >>> task_3()
    {452025: 150678, 452029: 23810, 452034: 226019, 452048: 226026, 452062: 226033}
    """

    count = 0
    current_number = 452022 
    results = []

    while count < 5:
        divisors = set()
        for i in range(2, int(current_number**0.5) + 1):
            if current_number % i == 0:
                divisors.add(i)
                divisors.add(current_number // i)
        
        if divisors:
            min_div = min(divisors)
            max_div = max(divisors)
            M = min_div + max_div
        else:
            M = 0
        
        if M % 7 == 3:
            results.append((current_number, M))
            count += 1
        
        current_number += 1
    num={}
    for number, M_value in results:
        num[number]=M_value
        
    return(num)



def main():
    print(task_1())
    print(task_2())
    for n, h in task_3().items():
        print(f"{n} {h}")
if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()

