def main():
    answer = input('What time is it? ')
    time = convert(answer)
    if time >=7 and time <=8:
        print('Its breakfast time!')
    elif time >=12 and time <=13:
        print('Its lunch time!')
    elif time >=18 and time <=19:
        print('Its dinner time!')
    else:
        print('You can´t eat now!')


def convert(time):
    hours, minutes = time.split(':')
    new_minute = float(minutes) / 60
    return float(hours) + new_minute


main()