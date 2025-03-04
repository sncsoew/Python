def to_str(nested_list):
    result = []
    while nested_list:
        element = nested_list.pop()
        if isinstance(element, list):
            nested_list.extend(element)
        else:
            result.append(str(element))
    return ' -> '.join(reversed(result)) + ' -> None'
    
def to_str_req(nested_list):
    def flatten(nested_list):
        if not nested_list:
            return []
        else:
            first = nested_list[0]
            rest = nested_list[1:]
            if isinstance(first,list):
                return flatten(first)+flatten(rest)
            else:
                return [first]+ flatten(rest)
    return ' -> '.join(map(str,flatten(nested_list)))+ ' -> None'



def calculate_sequence(n):
    if n == 0 or n == 1:
        return 1
    return calculate_sequence(n - 2) + (calculate_sequence(n - 1) / (2 ** (n - 1)))

def calc(n):
    if n == 0 or n == 1:
        return 1
    a1=1
    a2=1
    for i in range(2,n+1):
        current=a1+(a2/(2**(i-1)))
        a1=a2
        a2=current
    return a2


if __name__ == "__main__":
    print(to_str([1, [2, [3, [4, [5]]]]]))
    print(f'a(5) == {calculate_sequence(5)}')
