#!Python

import time
import random

def roll_dice(name):
    dice_one=random.randint(1,6)
    dice_two=random.randint(1,6)
    dice_total=dice_one+dice_two
    print(name+'rolled a' +str(dice_one) + 'and'+str(dice_two)+'for a total of'+str(dice_total)+'.')
    return dice_total

while True:
    answer=input('\n Wouls you like to play dice? type exit to exit and anything else to play :')
    if answer.lower()=='exit':
        break
    print('\n The dice will be rolled for the computer, then you, Heighest total wins!')

    time.sleep(2)
    comp_total=roll_dice('Computer')
    time.sleep(2)
    player_total=roll_dice('User')
    time.sleep(2)

    if comp_total>=player_total:
        print('\nThe Computer wins!')
    else:
        print('\n You Win...! Congratulation..!!')

