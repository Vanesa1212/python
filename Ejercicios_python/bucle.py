#while

'''want_greet = 'S'  # importante dar un valor inicial

while want_greet == 'S':
    print('Hola qué tal!')
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

'''MAX_GREETS = 4

num_greets = 0
want_greet = 'S'

while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

MAX_GREETS = 4

num_greets = 0
want_greet = 'S'

'''while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
else:
    print('Usted no quiere más saludos')
print('Que tenga un buen día')'''

#for

'''word = 'python'

for letter in word:
    print(letter)'''

'''for i in range(0, 3):
    print(i)

for i in range(6):  # No hace falta indicar el inicio si es 0
    print(i)'''

for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f'{num_table} * {mul_factor} = {result}')
        