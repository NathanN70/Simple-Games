# two people take turns counting up by 1 or 2. The goal is to say 21.
# different variations can exist based on the values that can be counted up by or the goal number.
# This is the manual 2 player version, will be doing a automatically generated algorithm later.

# play function: first argument is max_interval, the most that can be counted up to by a player in a single turn
# second argument: goal, the number that each player is trying to say and wins upon saying
def play(max_interval:int, goal:int):
    current = 0
    player_turn = 0
    while current < goal:
        print("player " + str(player_turn % 2 + 1) + " turn")
        move = 0
        while move < 1 or move > max_interval:
            try:
                move = int(input('Type a valid number between 1 and ' + str(max_interval) + " "))
                if move < 1 or move > max_interval:
                    print("Invalid input. Choose a number between 1 and " + str(max_interval) + " ")
            except (TypeError, ValueError):
                print("Invalid input. Choose a number between 1 and " + str(max_interval) + " ")
        player_turn += 1
        current += move
        print(str(current))
    player_turn -= 1
    print("Game Over: Player " + str(player_turn % 2 + 1) + " wins")

while True:
    print("Counting Game")
    if (input('Type "1" to play: ')) == "1":
        max_interval = 0
        goal = 0
        while max_interval < 2:
            try:
                max_interval = int(input('What is the maximum interval? '))
                if max_interval < 2:
                    print("Choose a value greater than or equal to 2")
            except (TypeError, ValueError):
                print("Invalid input. Choose a number greater than 1")
        while goal < 2:
            try:
                goal = int(input('What is the goal number(the number you need to say to win)? '))
                if goal < 2:
                    print("Choose a value greater than or equal to 2")
            except (TypeError, ValueError):
                print("Invalid input. Choose a number greater than 2")
        play(max_interval, goal)
    else:
        break