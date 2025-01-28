hangman_words = ["Lumberjack", "Mystery", "Galaxy", "Crocodile",
"Avalanche", "Nightingale"]

fact=random.choice(hangman_words)

l=7

guesses=""

for i in range(l):
    guesses+="_"


count=0

def print_hangman(wrong_guesses):
    hangman_stages = [
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
         /|\\  |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ========="""
    ]
    if wrong_guesses < len(hangman_stages):
        print(hangman_stages[wrong_guesses])

# Example usage

wrong_guesses = 0

print ("""+---+
      |
      |
      |
      |
========="""
)
print(guesses)

game_play = True

correct_l=[]

while l>0:
    print("You have ", l, "lives left")
    print("This is how you are tracking, ", word)
    iguess=input("guess a letter:")
    word = ""
           
    for i in fact:
        if i == iguess:
            word += iguess
            correct_l.append(iguess)
            print_hangman(wrong_guesses)
            

        
        elif i in correct_l:
            word += i
            print("You already guessed this letter correctly")
            print_hangman(wrong_guesses)
        else:
            word += "_"
            
    if iguess not in fact:
        print("Incorrect guess")
        
        print_hangman(wrong_guesses)
        wrong_guesses += 1
        
    l-=1
    
    
    if "_" not in word:
        print("""You have guessed the word correctly!
              You""")
        break 

if wrong_guesses == 7:
    print_hangman(wrong_guesses)
    print("You have run out of lives, the word was ", fact)
    print("Game Over")
