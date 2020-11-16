def ito_decimal(nb, base_dst):
    intermediate_nb = 0
    n = 0
    b = nb[::-1]
    for i in b:
        intermediate_nb += int(base_dst.index(i) * len(base_dst) ** n)
        n += 1
    return intermediate_nb


def ito_base_loop(nb, base):
    new_nb = ''
    while nb > 0:
        x = nb // len(base)
        rest = nb % len(base)
        new_nb = base[rest] + new_nb
        nb = x
    return new_nb


def ito_base(nb, base, base_dst=None):
    if base_dst == None:
        return ito_base_loop(nb, base)
    else:
        intermediate_nb = ito_decimal(nb, base_dst)
        return ito_base_loop(intermediate_nb, base)


if __name__ == '__main__':
    choice = input('Введите количество аргументов функции(2 или 3): ')
    try:
        if choice == '3':
            print(ito_base(input('Введите конвентируемое число: '), input('Введите систему исчисления, в которую нужно конвентировать: '), input('Введите систему исчесления конвентируемого числа: ')))
        elif choice == '2':
            print(ito_base(int(input('Введите беззнаковое конвентируемое число: ')), str(input('Введите систему исчисления в виде строки из ее элементов: '))))
        else:
            raise ValueError
    except ValueError:
        print('Введены некоректные данные')

