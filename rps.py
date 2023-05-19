import random

# rock paper scissors. Player inputs rock, paper, or scissors while the computer randomly picks rock paper or scissors.
# each of the 3 options beats one of the opponent's option, ties with one of the opponent's option, and loses to one of the opponent's options and vice versa.
# rock beats scissors, scissors beats paper, paper beats rock


def play():
    print("Rock, Paper, Scissors, Shoot!")
    player_move = input("Pick, 'Rock', 'Paper', or 'Scissors' ")
    # computer move shows as int 1-3. 1 is rock, 2 is paper, 3 is scissors
    comp_move = random.randint(1,3)
    if (player_move == "Rock" and comp_move == 1) or (player_move == "Paper" and comp_move == 2) or (player_move == "Scissors" and comp_move == 3):
        print("Draw")
    elif (player_move == "Rock" and comp_move == 2) or (player_move == "Paper" and comp_move == 3) or (player_move == "Scissors" and comp_move == 1):
        print("You Lose")
    else:
        print("You Win")
    
play()

while True:
    print("Rock Paper Scissors")
    if (input('Type "1" to play: ')) == "1":
        play()
    else:
        break