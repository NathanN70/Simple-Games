import random

class minesweeper:
    def __init__(self, width, height, mines):
        if mines > width * height:
            print("Invalid Parameters, Too Many Mines")
        if width < 1 or height < 1 or mines < 1:
            print("Invalid Parameters: Width, Height, and Mine Count >= 1")
        self.width = width
        self.height = height
        self.mines = mines
        # for grid, -1 represents tile with mines, 0-8 means that many mines in neighboring(adjascent including diagonal) tiles
        self.grid = [[0 for x in range(height)] for x in range(width)]
        # place mines in random spots
        random.seed()
        places = random.sample([x for x in range(width * height)], k = mines)
        for spot in places:
            x = spot % width
            y = spot // width
            self.grid[x][y] = -1

        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == 0:
                    for checkx in range(-1, 2):
                        for checky in range(-1, 2):
                            try:
                                if self.grid[x + checkx][y + checky] == -1:
                                    self.grid[x][y] += 1
                            except:
                                pass

        self.shown = [[-2 for x in range(height)] for x in range(width)]


    def mark_mine(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            print("Invalid Input")
            return
        temp = self.shown[x][y]
        if temp > -2:
            print("Invalid Input")
            return
        if temp == -2:
            self.shown[x][y] = -3
        else:
            self.shown[x][y] = -2
    

    def show_shown(self):
        pass

    def move(self):
        pass
        
        



def play(width = 10, height = 10, mines = 15):
    board = minesweeper(width, height, mines)

resume = True
while resume == True:
    try:
        play(str(input("Board Width? ")), str(input("Board Height?" )), str(input("Mine Count? ")))
        resume = False
    except:
        pass