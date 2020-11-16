import re


def create_pattern(second_str: str):
    pattern = ''
    for symbol in second_str:
        if symbol != '*':
            pattern += symbol
        else:
            pattern += '\w*'
    print(pattern)
    return pattern


while True:
    first_str = str(input()).lower()
    second_str = str(input()).lower()
    if re.fullmatch(str(create_pattern(second_str)), first_str):
        print('ОК')
    else:
        print('KO')
