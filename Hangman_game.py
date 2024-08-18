import random

# List of word categories
categories = {
    "animals": ["cat", "dog", "elephant", "lion", "tiger", "bear", "monkey"],
    "countries": ["usa", "canada", "mexico", "france", "germany", "italy", "spain"],
    "movies": ["starwars", "avengers", "inception", "interstellar", "matrix", "joker", "parasite"]
}

# Hangman graphics
hangman_graphics = [
    """
    +---+
    |   |
            |
            |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
            |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
    |   |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|   |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
            |
    ========="""
]

def get_word(category):
    return random.choice(categories[category])

def play_hangman():
    print("Welcome to Hangman!")
    print("Choose a category:")
    for i, category in enumerate(categories.keys()):
        print(f"{i+1}. {category.capitalize()}")
    category_choice = int(input("Enter the number of your chosen category: "))
    category = list(categories.keys())[category_choice - 1]
    word = get_word(category)  # Store the chosen word in a variable
    word_length = len(word)
    display = ["_"] * word_length
    guessed_letters = []
    tries = 6
    score = 0

    while "_" in display and tries > 0:
        print(" ".join(display))
        print(hangman_graphics[6 - tries])
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please guess a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            tries -= 1
            print("Incorrect guess.")
        else:
            score += 1
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
    if "_" not in display:
        print("Congratulations, you won!")
        print(f"Your score is {score}.")
    else:
        print("Game over. The word was " + word)
        print("Better luck next time!")

if __name__ == "__main__":
    play_hangman()