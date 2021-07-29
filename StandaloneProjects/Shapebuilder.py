def main():

    print('\n Welcome to Square Builder ')
    "sq_dimension = valid_check()"
    make_square(valid_check())


def valid_check():
    dimension = int(input('\n Enter Square Dimension as a single int: '))
    while not (dimension > 0):
        print('\n Not a Valid int')
        dimension = int(input('\n Enter Square Dimension as a single int: '))
    else:
        return dimension


def make_square(int, border_shape='-'):

    top_line = int * (border_shape+'  ')
    print(' ' + top_line)

    spaces = ' ' * ((int * 3) - 4)
    side_length = (' ' + border_shape + spaces + border_shape)

    length = (int - 2)
    while length > 0:
        print(side_length)
        length -= 1

    print(' ' + top_line)


if __name__ == '__main__':
    main()
