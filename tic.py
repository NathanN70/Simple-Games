# tic-tac-toe. 2 players alternate occupying one space of a 3x3 grid. The first to get 3 of their mark in a line(horizontal, diagonal, or vertical) wins
# Currently only 3x3 with goal being 3 in a row

global grid
global turn
grid = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
turn = 0
# return player number of victor if any, else return 0
# checks for winner based on most recent move
# add more comments as more complete
def check_winner(spot:int):
    if(spot == 0):
        return 0
    return 0

# function for one move, called for each turn
# replaces an empty spot on grid
# prints victory announcement if winner is determined
# prints that the move is invalid if spot already claimed
def move(spot:int):
    global turn
    if grid[spot] != -1:
        print("Occupied. Choose a spot that has not been occupied")
        return True
    grid[spot] = turn % 2
    winning_status = check_winner(spot)
    if (winning_status == 1):
        print("Player 1 Wins!")
        return False
    elif(winning_status == 2):
        print("Player 2 Wins!")
        return False
    else:
        turn += 1
        if turn == 9:
            print("Draw")
            return False
        print("Turn " + str(turn + 1) + str(grid))
        return True

def start():
    turn = 0
    player_turn = (1 + turn) % 2
    game_state = True
    # initial grid, -1 indicates untouched
    grid = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    # 0 indicates player 1(first to move) possession
    # 1 indicates player 2 possession
    while game_state == True:
        while True:
            try:
                spot = int(input("Player " + str(player_turn) + " choose your move: "))
                game_state = move(spot)
                break
            except (TypeError, ValueError, IndexError):
                print("Invalid input. Choose a number between 0-8")
    pass
while True:
    print("Tic-Tac-Toe")
    if (input('Type "1" to play: ')) == "1":
        start()
    else:
        break