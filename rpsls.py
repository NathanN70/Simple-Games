import random

# rock paper scissors lizard spock. Player inputs rock, paper, scissors, lizard, or spock while the computer randomly picks the same 5.
# each of the 5 options beats 2 of the opponent's option, ties with 1 of the opponent's option, and loses to 2 of the opponent's options and vice versa.
# rock beats scissors, scissors beats paper, paper beats rock, i'm not listing the rest here.


def play():
    print("Rock, Paper, Scissors, Shoot!")
    player_move = input("Pick, 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ")
    # computer move shows as int 1-5. 1 is rock, 2 is paper, 3 is scissors, 4 is Lizard, 5 is Spock
    comp_move = random.randint(1,5)
    if (player_move == "Rock" and comp_move == 1) or (player_move == "Paper" and comp_move == 2) or (player_move == "Scissors" and comp_move == 3) or (player_move == "Lizard" and comp_move == 4) or (player_move == "Spock" and comp_move == 5):
        print("Draw")
    elif (player_move == "Rock" and comp_move in [2,5]) or (player_move == "Paper" and comp_move in [1,3]) or (player_move == "Scissors" and comp_move in [1,5]) or (player_move == "Lizard" and comp_move in [1,3]) or (player_move == "Spock" and comp_move in [2,4]):
        print("You Lose")
    else:
        print("You Win")
    
play()

while True:
    print("Rock Paper Scissors Lizard Spock")
    if (input('Type "1" to play: ')) == "1":
        play()
    else:
        break