def main():
    x = int(input('What´s x? '))
    if is_even(x) is True:
        print('Even')
    else:
        print('Odd')


def is_even(n):
    return True if n % 2 == 0 else False   #also return n % 2 == 0 works fine


main()