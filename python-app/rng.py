from random import randint

min_number = int(input('Enter a min number: '))
max_number = int(input('Enter a max number: '))

if (max_number < min_number):
    print('Invalid Input')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)

