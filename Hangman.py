
import random
from hangman_art import stages
word_list=['junaid','saurabh','naushad','parwez']
end_of_game=False
chosen_word=random.choice(word_list)
lives = 6



print(f'press, the solution is {chosen_word}')
display = []
word_length=len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
    guess=input("guess a letter").lower()
    for position in range(word_length):
        letter =chosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -=1
        if lives==0:
            end_of_game=True
            print("you lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game= True
        print("you win.")
    print(stages[lives])
