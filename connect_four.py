# connect 4. 7 columns and 6 rows. Pick a column to add a marker to and the marker is placed on the lowest row of that column
# To win, you need to have four of your markers continuously in a straight line (vertical, horizontal, or diagonal)
# 

global grid
global turn
grid = []
for x in range(7):
    grid.append([])
turn = 0
print(grid)

def move(spot:int):
    if grid[spot].len() == 6:
        print("Column Full")
        return True
    grid[spot].append(turn % 2)
    winning_status = check_winner(spot)
    if (winning_status == 1):
        print("Player 1 Wins!")
        return False
    elif(winning_status == 2):
        print("Player 2 Wins!")
        return False
    else:
        turn += 1
        if turn == 42:
            print("Draw")
            return False
        print("Turn " + str(turn + 1) + str(grid))
        return True
    
def check_winner(spot:int):
    pass
