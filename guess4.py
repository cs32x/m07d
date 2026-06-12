### m07b/guess4.py
import random

def main():
    secret = random.randint(1, 100)
    print(f"The secret number is {secret}")

    # Grab the player's guess
    try:
        guess = int(input('Please input your guess: '))
    except ValueError:
        print('Guesses must be an integer.')

    # Check guess against the secret
    if guess == secret:
        print('Exactly! You win!')
    elif guess < secret:
        print('Too small!')
    else:
        print('Too big!')

if __name__ == '__main__':
    main()