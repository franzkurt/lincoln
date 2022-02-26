import random

WORD_LIST = ["aardvark", "baboon", "camel"]
MAX_POINTS = 5
chosen_word = random.choice(WORD_LIST)

word = ["".join("_") for i in chosen_word]
print(word)


def game():
    # Initial setup
    initial_points = MAX_POINTS
    print(f"initial_points: {initial_points}")
    
    # store the guess history
    history = set()
    
    while True:
        if "_" not in word:
            print('you WIN!!')
            break
        elif initial_points < 1:
            print('you LOSE!!')
            break

        guess = input("Guess a letter: ").lower()
        # decrement initial points
        if guess not in chosen_word \
            and guess not in history \
            and guess not in word:
            initial_points -= 1

        for i, c in enumerate(chosen_word):
            if guess == c:
                word[i] = guess

        # Not decrement twice
        history.add(guess)
        
        # display
        print(f"Points: {initial_points} - {word}")
        print(f"Guessed letters: {history}")


game()
