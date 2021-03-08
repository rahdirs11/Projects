#!/usr/bin/env python
'''
I've designed the game such that if either
of the players loose more than three times,
the other defalts as winner of the game, which
will cause this program to terminate!
'''
from nltk.corpus import words
import random, time, os, sys

clearCommand = 'clear' if sys.platform == 'linux' else 'cls'

wordSet = words.words() # list of 236736 words
# print(len(wordSet))
# wordSet = ['aeroplane', 'bark', 'stupid', 'laptop'] -> used these for test example
turn = 1    # 1 - player 1, 2 - player 2
playerLost, playerWon = False, False
head, leftArm, rightArm, body, leftLeg, rightLeg = ' ', ' ', ' ', ' ', ' ', ' '
player1LossCount = player2LossCount = 0


def reset():
    global head, leftArm, rightArm, body, leftLeg, rightLeg
    head, leftArm, rightArm, body, leftLeg, rightLeg = ' ', ' ', ' ', ' ', ' ', ' '


def printHangMan(tries=0):
    global head, leftArm, rightArm, body, leftLeg, rightLeg, playerLost
    print('-' * 15)
    print(f'{"   |":<9}|')
    if tries == 1:
        head = 'O'
    elif tries == 2:
        body = '|'
    elif tries == 3:
        leftArm = '`'
    elif tries == 4:
        rightArm = '`'
    elif tries == 5:
        rightLeg = '`'
    elif tries == 6:
        leftLeg = '`'
        playerLost = True
    print(f'{head:>4}{"|":>6}')
    print(f'{leftArm:>3}{body}{rightArm:>1}{" ":<4}|')
    print(f'{leftLeg:>3}{rightLeg:>2}{" ":<4}|')
    print(f'{"-----":>12}')


def fillTheBlanks(word):
    print(' ' * len(word))
    for i in word:
        print('_ '  if i == ' ' else f'{i} ', end='')
    print('\n\n')


def playGame(turn):
    global playerWon, playerLost, player1LossCount, player2LossCount
    os.system(clearCommand)
    if player1LossCount > 3:
        print('Player 2 WINS!')
        exit()
    elif player2LossCount > 3:
        print('Player 1 WINS!')
        exit()
    reset()
    wordToBeGuessed = list(random.choice(wordSet))
    guessedWord = [' ' for i in range(len(wordToBeGuessed))]
    tries = 0
    while not playerLost:
        if ''.join(guessedWord) in wordSet:
            print('xyz')
            playerWon = True
            break
        # printHangMan()
        letter = input(f'Player {turn} =>\nGuess a letter:\t').lower()
        os.system(clearCommand)
        if letter in wordToBeGuessed:
            while letter in wordToBeGuessed:
                i = wordToBeGuessed.index(letter)
                guessedWord[i] = letter
                wordToBeGuessed[i] = ' '
        else:
            tries += 1
        printHangMan(tries)
        if playerLost:
            if turn == 1:
                player1LossCount += 1
            else:
                player2LossCount += 1
            print('Player {} failed to guess before the man was HANGED xD!\nYou LOST!!'.format(turn))
            print(f'Correct Answer:\t{wordToBeGuessed}')
            time.sleep(3)
            playerLost = False
            break
        fillTheBlanks(guessedWord)
    if playerWon:
        os.system(clearCommand)
        print(f'PLAYER {turn} WON!! CONGRATS!!')
        time.sleep(3)
        playerWon = False
    turn = 1 if turn == 2 else 2
    return turn

while True:
    if turn == 1:   # player 1
        turn = playGame(turn)
    else:           # player 2
        turn = playGame(turn)
