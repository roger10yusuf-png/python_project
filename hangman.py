word = "python"
guess = ["_"] * len(word)
print("Try guessing the word:")
print(" ".join(guess))

def hangman(count):
    if count == 1:
        print("|")
    elif count == 2:
        print('''        |
        O''')
    elif count == 3:
                print('''        |
        O
        |''')
    elif count == 4:
         print('''        |
        O
       /|''')
    elif count == 5:
         print('''        |
        O
       /|\\''')
    elif count == 6:
          print('''        |
        O
       /|\\
       /''')
    elif count == 7:
         print('''        |
        O
       /|\\
       / \\''')
         
         
counter = 0

while True:
    letter_guess = input("What letter do you think is in the word? ")

    if letter_guess in word:
        for i in range(len(word)):
            if word[i] == letter_guess:
                guess[i] = letter_guess
        print(" ".join(guess))
    else:
        print("That letter is not in the word. Try again.")
        counter = counter +1
        hangman(counter)
        if counter == 7:
             print("game over.try again")
             break

    if "_" not in guess:
        print("You have guessed it right!")
        break
