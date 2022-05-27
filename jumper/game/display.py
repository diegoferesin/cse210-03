"""Display class has the methods to show the different messages of the game and show the update status of parachute"""
class Display:
    
    def display_jumper(self, jumper):
        #print("_ _ _ _ _\n")
        for i in jumper:
            print(i)
        print("^^^^^^^\n")
        """Print the status of the parachute when the player guess or not a letter of the secret word"""

    
    def display_puzzle(self, letters, word):
        for letter in word:
            if letter in letters:
                print(letter + " ", end="")
            else:
                print(" _ ", end="")
        print()
        """print the letters guessed of the secret word"""

    
    def user_input(self):
        correct = True
        while correct:
            letter = input("Guess a letter [a-z]: ").lower()
            if len(letter) > 1:
                print("You can only enter one letter. Please try again 😁")
            elif letter.isspace():
                print("You can't type an empty space. Please try againg 😁")
            else:
                correct = False
                return letter
        """Method to validate the input letter"""
    
    
    """Messages show to the player along the game"""
    
    def display_win_message(self):
        print("Congratulations, you guessed the word and won the game!")

    def display_loss_message(self):
        print("Your jumper run out of lives. Better luck next time.")

    def display_used_letter(self):
        print("You already used this letter. Please try with a different one 😁")

    def display_letters_used(self, letters):
        print(f"Letters used: {letters}")
    
    def display_secret_word(self,word):
        print(f"The secret word is: {word}")
