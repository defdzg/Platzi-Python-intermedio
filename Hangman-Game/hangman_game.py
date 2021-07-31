"""
REQUISITOS
    Sistema de puntos, dibujo ASCII, mejora interfaz. 
"""
# MODULES
import os
import random
import time
from pyfiglet import Figlet


FILE_TO_READ = "./files/data.txt"

# LOGIC FOR HANGMAN GAME
class Hangman:
    def __init__(self):
        self.score = 0
        self.words_list = read_data()
        ascii_art()
        time.sleep(3)
    def word(self):
        selected_word = random.sample(self.words_list, 1)
        chars = list(selected_word[0])
        #print(chars)
        
        return chars
    
    def letter(self):
        validation  = False
        while validation == False:
            try:
                user_input = input("Choose a letter: ")
                validation = user_input.isalpha()
                if validation == False or len(user_input) != 1:
                    raise ValueError
            except ValueError:
                print("Choose just one letter. Don't numbers or other characters. \n")
                validation = False
                
        return user_input
    
    def guess(self):
        os.system("clear")
        word_to_guess = self.word()
        guessed_letters = list("_"*len(word_to_guess))
        guessed_idx = 0
        missing_letters = len(word_to_guess)
        
        while guessed_idx != len(word_to_guess):
            os.system("clear")
            ascii_art()
            print(" ".join(guessed_letters))
            print(f'You have {missing_letters} letters missing. \n')
            
            letter_as_input = self.letter()
            idx = [i for i, e in enumerate(word_to_guess) if e == letter_as_input]
            
            for i in idx:
                if guessed_letters[i] == "_":
                    guessed_letters[i] = letter_as_input
                    guessed_idx += 1
                    missing_letters = (len(word_to_guess)-guessed_idx)
                else:
                    print('You have already used that letter.')
        
        os.system("clear")
        print(" ".join(guessed_letters))
        print(f"You've guessed the word!\n\n")
        ascii_art ()
        
# ASCII ART FOTNS:
def ascii_art ():
    custom_fig = Figlet(font='isometric2')
    print(custom_fig.renderText('HMG'))
    print("Hangman Game | Daniel Fernández")
    
    
# READING WORD LIST
def read_data():
    words = []
    with open(FILE_TO_READ, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line[:-1])
            
    return words

# MAIN PROGRAM
def main():
    game = Hangman()
    game.guess()

# ENTRY POINT
if __name__ == "__main__":
    main()