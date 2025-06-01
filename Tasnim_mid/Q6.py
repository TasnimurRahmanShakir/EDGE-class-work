import random

attempts = 3

print('Guess the number in range [0,20]')
rand = random.randint(0, 20)
while attempts > 0:
    val = int(input('Guess: '))
    if val == rand:
        print('You made it')
        break
    attempts -= 1
    print(f'you have {attempts} left')
    
print(f'Correct number was {rand}')