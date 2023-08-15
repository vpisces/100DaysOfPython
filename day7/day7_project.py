#Step 1
import random, hangman_words
from hangman_art import logo, stages
print(logo)

lives = 6

chosen_word = random.choice(hangman_words.word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Convert list into string
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")