import random

game_choices = ["rock","paper","scissors"]
rock = game_choices[0]
paper = game_choices[1]
scissors = game_choices[2]

print('WELCOME TO ROCK, PAPER AND SCISSORS GAME.')
print('-----------------------------------------')
print('*press q to exit*')
while True:
    result = input('rock, paper and scissors? : ')
    print('-----------------------------------------')
    computer_result = random.choice(game_choices)
    if result == rock:
        if computer_result == rock:
            print(f'Equal {result} = {computer_result}')
            print('-----------------------------------------')
        elif computer_result == paper:
            print(f'Game Over! You Lose! {result} < {computer_result}')
            print('-----------------------------------------')
        elif computer_result == scissors:
            print(f'K.O! You WON! {result} > {computer_result}')
            print('-----------------------------------------')
    if result == paper:
        if computer_result == rock:
            print(f'K.O! You WON! {result} > {computer_result}')
            print('-----------------------------------------')
        elif computer_result == paper:
            print(f'Equal {result} = {computer_result}')
            print('-----------------------------------------')
        elif computer_result == scissors:
            print(f'Game Over! You Lose! {result} < {computer_result}')
            print('-----------------------------------------')
    if result == scissors:
        if computer_result == rock:
            print(f'Game Over! You Lose! {result} < {computer_result}')
            print('-----------------------------------------')
        elif computer_result == paper:
            print(f'K.O! You WON! {result} > {computer_result}')
            print('-----------------------------------------')
        elif computer_result == scissors:
            print(f'Equal {result} = {computer_result}')
            print('-----------------------------------------')
    if result == 'q':
        print('exiting..')
        break