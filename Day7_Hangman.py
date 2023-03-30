import random
import hangman_art
import hangman_words
import os


os.system('cls')
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.\n')

#Create blanks
display = []
for letter in chosen_word:
  display += "_"
print(f"\n{' '.join(display)}")


#Check guessed letter while there are still blanks and 10a lives
lives = 9
guess_attempts = []

while "_" in display:
  
  guess = input("\nGuess a letter: ").lower()
  os.system('cls')

  i = 0
  correct_guess = False

  if guess in guess_attempts:
      print(hangman_art.logo)
      print(f"\n{' '.join(display)}")
      print(f"\n{' '.join(guess_attempts)}")
      print(hangman_art.stages[lives])
      print(f"\nYou already tried that letter, try again.")

    
  else:
      # check to see if guess is in chosen word
      for letter in chosen_word:
          if letter == guess:
              display[i] = guess
              correct_guess = True
          i += 1

      #add guess attempts to list
      guess_attempts.append(guess)
  
      #if guess is correct
      if (correct_guess == True):
          print(hangman_art.logo)
          print(f"\n{' '.join(display)}")
          print(f"\n{' '.join(guess_attempts)}")
          print(hangman_art.stages[lives])
          print("\nNice!")
        
      #if guess is wrong
      else:
          lives -= 1
          print(hangman_art.logo)
          print(f"\n{' '.join(display)}")
          print(f"\n{' '.join(guess_attempts)}")
          print(hangman_art.stages[lives])
          print(f"\n'{guess}' is not in the word, you lose a life!")
      
      #if lost
      if lives == 0:
          print(f"\nDEAD! You Lose. The word was {chosen_word}.\n")
          break
    
      #if won
      if "_" not in display:
          print("\nGOOD JOB, You Win!!\n")
          break