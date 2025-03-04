from main import to_str,to_str_req, calculate_sequence,calc

def test_to_str_1():
    assert to_str([1, [2, [3, [4, [5]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> None'
def test_to_str_2():
    assert to_str([1,2,3,[4,[5,[6,7]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'
def test_to_str_3():
    assert to_str([[1,2,3],[4,[5,[6,[7,[8,[9]]]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None'
def test_to_str_4():
    assert to_str([1,[2,[3,[4,[5,[6,[7]]]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'
def test_to_str_5():
    assert to_str([1,[2,3,4,[5,6,7]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'

def test_to_str_req_1():
    assert to_str_req([1, [2, [3, [4, [5]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> None'
def test_to_str_req_2():
    assert to_str_req([1,2,3,[4,[5,[6,7]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'
def test_to_str_req_3():
    assert to_str_req([[1,2,3],[4,[5,[6,[7,[8,[9]]]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None'
def test_to_str_req_4():
    assert to_str_req([1,[2,[3,[4,[5,[6,[7]]]]]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'
def test_to_str_req_5():
    assert to_str_req([1,[2,3,4,[5,6,7]]]) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None'

def test_calculate_sequence_1():
    assert calculate_sequence(5) == 1.4794921875
def test_calculate_sequence_2():
    assert calculate_sequence(10) == 1.7328326573181982
def test_calculate_sequence_3():
    assert calculate_sequence(19) == 1.5153493209223141
def test_calculate_sequence_4():
    assert calculate_sequence(12) == 1.7335722995035647
def test_calculate_sequence_5():
    assert calculate_sequence(15) == 1.515316251200754 

def test_calc_1():
    assert calc(5) == 1.4794921875
def test_calc_2():
    assert calc(10) == 1.7328326573181982
def test_calc_3():
    assert calc(19) == 1.5153493209223141
def test_calc_4():
    assert calc(12) == 1.7335722995035647
def test_calc_5():
    assert calc(15) == 1.515316251200754 
