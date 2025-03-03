
def to_str(nested_list):
    result = []
    while nested_list:
        element = nested_list.pop()
        if isinstance(element, list):
            nested_list.extend(element)
        else:
            result.append(str(element))
    return ' -> '.join(reversed(result)) + ' -> None'

def calculate_sequence(n):
    if n == 0 or n == 1:
        return 1
    return calculate_sequence(n - 2) + (calculate_sequence(n - 1) / (2 ** (n - 1)))


if __name__ == "__main__":
    print(to_str([1, [2, [3, [4, [5]]]]]))
    print(f'a(5) == {calculate_sequence(5)}')
