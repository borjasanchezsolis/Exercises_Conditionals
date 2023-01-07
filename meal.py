def main():
    time = input('What time is it? ')
    if time[0] == '7' or time == '8:00':
        print('it´s breakfast time!')
    elif time[0:2] == '12' or time == '13:00':
        print('its lunch time!')
    elif time[0:2] == '18' or time == '19:00':
        print('its dinner time!')
    else:
        print('You cant eat now!')


main()
