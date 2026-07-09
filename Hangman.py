import random

# List of predefined words
words = ["python", "computer", "program", "hangman", "keyboard"]


def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


def play_game():
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 45)
    print("🎮 Welcome to Hangman Game!")
    print("=" * 45)
    print(f"You have {max_attempts} incorrect guesses.\n")

    while wrong_guesses < max_attempts:

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed Letters:", " ".join(guessed_letters) if guessed_letters else "None")
        print("Remaining Attempts:", max_attempts - wrong_guesses)

        guess = input("\nEnter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct Guess!")

            # Check if player won
            if all(letter in guessed_letters for letter in secret_word):
                print("\n🎉 Congratulations!")
                print("You guessed the word:", secret_word)
                return

        else:
            wrong_guesses += 1
            print("❌ Wrong Guess!")

            stages = [
                """
                 -----
                 |   |
                 O   |
                /|\\  |
                / \\  |
                     |
                =========
                """,
                """
                 -----
                 |   |
                 O   |
                /|\\  |
                /    |
                     |
                =========
                """,
                """
                 -----
                 |   |
                 O   |
                /|\\  |
                     |
                     |
                =========
                """,
                """
                 -----
                 |   |
                 O   |
                /|   |
                     |
                     |
                =========
                """,
                """
                 -----
                 |   |
                 O   |
                 |   |
                     |
                     |
                =========
                """,
                """
                 -----
                 |   |
                 O   |
                     |
                     |
                     |
                =========
                """,
                """
                 -----
                 |   |
                     |
                     |
                     |
                     |
                =========
                """
            ]

            print(stages[max_attempts - wrong_guesses])

    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)


while True:
    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\n👋 Thanks for playing!")
        break