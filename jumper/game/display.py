class Display:

    def display_jumper(self, jumper):
        print("_ _ _ _ _\n")
        for i in jumper:
            print(i)
        print("^^^^^^^\n")

    def display_puzzle(self, letters, word):
        for letter in word:
            if letter in letters:
                print(letter + " ", end = "")
            else:
                print(" _ ", end = "")
        print()

    def user_input(self):
        letter = input("Guess a letter [a-z]: ")
        return letter

    def display_win_message(self):

        print("Congratulations, you guessed the word and won the game!")

    def display_loss_message(self):

        print("Your jumper run out of lives. Better luck next time.")
    