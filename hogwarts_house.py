name = input('What´s your name? ').strip().lower()

match name:
    case 'Harry' | 'Ron' | 'Hermione':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who is that')

