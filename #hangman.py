#hangman

import random
secret_words = ["cat", "dog", "frog", "grape", "apple", "house", "lemon", "monkey", "orange", "rabbit", "tiger", "zebra", "banana", "jellyfish", "penguin", "umbrella", "xylophone", "elephant", "strawberry" ]

v = []
win = True
g_limit = 5
guesses = 0
s_word = random.choice(secret_words)
len_s_word = len(s_word)
pos = len_s_word

for i in range(len_s_word):
    v.append('_')

n = input(' \n  \n  \n  \n Hi. What is your name?                               ')

print("""Hi """ + n + """. Lets play Hangman, but first we have to explain the game and its instructions so follow me:
      
      • You will have a blanked word. something like this '_ _ _'. And you need to guess the word.    
      • You will have only 5 guesses before you die.
      • Every letter you get right will be shown.
      • You can only type a word that has the same number of letter the blank has. Example:
          ' _ _ _ _ '. You can't type 'brown' but you can type 'bark'.
      
            ➡ Here is you word. Goodluck:
      
""")

print('            _____________ ')
print('            |          |')
print('            |          |')
print('            |         ⚫')
print('            |         /|\ ')
print('            |         / \ ')
print('           _|____________')










print(' \n  ')
print("                                      ", end="")
print(*v, sep=" ")


print(s_word)

try:
    while (win) and guesses != g_limit:
        user_inp = list(input(' \n   \n        ►  '))
        if user_inp == list(s_word):
                print(' \n  \n ')
                print("                                      ", end="")
                print(*v, sep="   ")
                print(' \n  \n  \n ➡  Exellent job. You guessed my word right!')  
                win = False 
        for pos in range(len_s_word):
            if user_inp[pos] == s_word[pos]:
                v[pos]=s_word[pos]
            else:
                print('')
        if (user_inp[pos] == s_word[pos] or user_inp[pos] != s_word[pos]) and user_inp != list(s_word):
                print('             ➡  You just lost a guess.')
                guesses +=1

        print(' \n  \n ')
        print("                                      ", end="")
        print(*v, sep=" ")
        
        if guesses == 1 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /|\ ')
                    print('            |         /  ')
                    print('           _|____________')
        elif guesses == 2 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /|\ ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses ==3 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /| ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses ==4 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |          | ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses == 5 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         😵')
                    print('            |          ')
                    print('            |           ')
                    print('           _|____________')

                    print('   \n  \n                     Unfortunatly you lost the game. My word was '+ s_word)
                    win = False

except IndexError:
        print(' \n  \n  \n                 Type a word with the corresponding amount of letters. \n  \n  \n')
        win = False



