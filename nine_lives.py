import words
import random


def nine_lives(lives, secret_word, word):
    
    if len(lives) == 0:# Stop recursion condition
        return 'Game Over!'

    print(secret_word)
    print(f'Lives left: {lives}\n')
    guess = input('Guess a letter or a whole word: ')
    
    for i in range(len(word)):# Check if letter in word
        if word[i] == guess:
            secret_word[i] = guess# Replace '?' with the correct letter
    
    if guess not in word:
        lives = lives[:-1]
        print('Wrong! one life lost.')# Take away life

    if guess == word or secret_word == word:
        return f'You won! The secret word was {"".join(word)}'
        
    return nine_lives(lives, secret_word, word)# Recursively run function until stop


if __name__ == '__main__':
    word_list = list(random.choice(words.words))
    word_joined = ''.join(word_list)
    secret = list(len(word_joined) * '?')
    lives_left = 9 * "♥"

    print(nine_lives(lives_left, secret, word_list))