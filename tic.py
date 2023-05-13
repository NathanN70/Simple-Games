global grid
global turn
# initial grid, -1 indicates untouched
# 0 indicates player 1(first to move) possession
# 1 indicates player 2 possession
grid = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
turn = 0
# return player number of victor if any, else return 0
# checks for winner based on most recent move
# add more comments as more complete
def check_winner(spot:int):
    if(spot == 0):
        pass
    return 0

# function for one move, called for each turn
# replaces an empty spot on grid
# prints victory announcement if winner is determined
# prints that the move is invalid if spot already claimed
def move(spot:int):
    global turn
    if grid[spot] != -1:
        print("invalid move")
        return
    grid[spot] = turn % 2
    winning_status = check_winner(spot)
    if (winning_status == 1):
        print("Player 1 Wins!")
    elif(winning_status == 2):
        print("Player 2 Wins!")
    else:
        turn += 1
        print("Turn " + str(turn + 1) + str(grid))


move(2)
print(turn)
print(grid)