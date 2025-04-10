import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'raad het nummer tussen 1 en {x}: '))
        if guess < random_number:
            print(f"te laag a kk homo, het getal {guess} is te laag!")
        elif guess > random_number:
            print(f"te hoog a a zemmeltje, het getal {guess} is te hoog!")
    print(f"je hebt het getal {guess} geraden a niffo!")   



def computer_guess(x):
    laag = 1
    hoog = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(laag, hoog)
        feedback = input(f'is {guess} te hoog (H), te laag (L), of is het correct? ').lower()
        if feedback == 'h':
            hoog = guess - 1
        elif feedback == 'l':
            laag = guess + 1
    print(f"goedzo de computer heeft het getal geraden!")


computer_guess(624)