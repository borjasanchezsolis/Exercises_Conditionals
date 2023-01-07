answer = input('What´s the answer to the Question of Life? ').strip().lower()

match answer:
    case 'forty two' | 'forty-two' | '42':
        print('Yes')
    case _:
        print('No')