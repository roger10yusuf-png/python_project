import random
def wordscramble(word):
    wordlist = list(word)
    random.shuffle(wordlist)
    return "".join(wordlist)   
words = ["car","electric","water","street","turtle"]
score = 0
print("you only get 3 chances for each word")
while True:
    word = random.choice(words)
    shuffle_word = wordscramble(word)
    print(shuffle_word)
    for i in range (3):
        guess = input("guess the shuffle word :")

        if guess == word:
            score += 1
            print("you have guessed the scrambled word correctly,")
            break
        else:
            if i == 2:
                print("nice try the word was:",word)
            else:
                print("try again")
            
    keep_playing = input("do you want to keep playing?")

    if keep_playing == "no":
        print("your final score is",score)
        break

    
