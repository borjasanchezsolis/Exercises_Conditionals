x, y, z = input('arithmetic expression: ').split(' ')

if y == '+':
    solution = (int(x) + int(z))
elif y == '-':
    solution = (int(x) - int(z))
elif y == '*':
    solution = (int(x) * int(z))
elif y == '/':
    solution = (int(x) / int(z))


print(solution)
