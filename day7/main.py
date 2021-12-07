# Hangman
import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

number_of_guesses = 5
display = ["_" for letter in chosen_word]
while number_of_guesses > -1:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(''.join(display))
    else:
        print(hangman_art.stages[number_of_guesses])
        number_of_guesses -= 1
        print(''.join(display))
        print("you guessed %s, that's not in the word. You lose a life" % guess)
    if ''.join(display) == chosen_word:
        print("You Win")
        print("the word was %s" % chosen_word)
        break
    if number_of_guesses == 0:
        print("You Lose")
        print("the word was %s" % chosen_word)
        break

    

#for letter in chosen_word:
#    if letter == guess:
#        display.append(letter)
#    else:
#        display.append("_")

#while display != chosen_word:
#   guess = input("Guess a letter: ").lower()
