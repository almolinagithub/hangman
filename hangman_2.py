
import stages as stages
from logo import logo
from hangman_words import word_list
import random

words = word_list
print(logo)
lives = 6
game_over = False
parola_da_indovinare = random.choice(words)
lunghezza_parola =len(parola_da_indovinare)
print(f"pss , la parola da indovinare e' {parola_da_indovinare}")
display = []
for letter in range (lunghezza_parola):
    display.append("_")

game_over = False

while not game_over:
    tentativo = input("Inserisci una lettera: ").lower()
    for position in range(lunghezza_parola):
        if tentativo == parola_da_indovinare[position]:
            display[position] = tentativo
    if display[position] != tentativo:
        lives -= 1
        print(stages.stages[lives])
        print(f"Sorry, letter '{tentativo}' does not belong to the word.")
        if lives == 0:
            game_over = True
            print("You lost")



    display_stringa = " ".join(display)
    print(display_stringa)

    if "_" not in display:
        game_over = True
        print(f"You won!")
