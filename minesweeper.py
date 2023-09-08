import random

class minesweeper:
    def __init__(self, width, height, mines):
        if mines > width * height:
            print("Invalid Parameters, Too Many Mines")
            raise
        if width < 1 or height < 1 or mines < 1:
            print("Invalid Parameters: Width, Height, and Mine Count >= 1")
            raise
        self.ongoing = True
        self.width = width
        self.height = height
        self.mines = mines
        # for grid, -1 represents tile with mines, 0-8 means that many mines in neighboring(adjascent including diagonal) tiles
        self.grid = [[0 for x in range(width)] for x in range(height)]
        # place mines in random spots
        random.seed()
        places = random.sample([x for x in range(width * height)], k = mines)
        for spot in places:
            x = spot % width
            y = spot // width
            self.grid[y][x] = -1

        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == 0:
                    for checkx in range(-1, 2):
                        if x + checkx < 0:
                            continue
                        for checky in range(-1, 2):
                            if y + checky < 0:
                                continue
                            try:
                                if self.grid[y + checky][x + checkx] == -1:
                                    self.grid[y][x] += 1
                            except:
                                pass

        self.shown = [["?" for x in range(width)] for x in range(height)]
        while self.ongoing:
            self.move()


    def mark_mine(self, x, y):
        temp = self.shown[y][x]
        if temp != "?" and temp != "!":
            print("Invalid Input")
            return
        if temp == "?":
            self.shown[y][x] = "!"
        else:
            self.shown[y][x] = "?"
    
    def show_shown(self):
        print(" X |", end = "")
        for x in range(self.width):
            print(str(x + 1).center(3), end = "")
        print("\n----" + ("---" * self.width))
        for y in range(self.height):
            print(str(y + 1).center(3), end = "|")
            for x in range(self.width):
                print(str(self.shown[y][x]).center(3), end = "")
            print()

    def move(self):
        try:
            x = int(input("X Coordinate From Left? Pick a number from '1' to the width: ")) - 1
            y = int(input("Y Coordinate From Top? Pick a number from '1' to the height: ")) - 1
            ifmark = int(input("Mark or Select? If Mark, type '1'. If Select, Type '2'. "))
            if x < 0 or y < 0 or x >= self.width or y >= self.height or ifmark < 1 or ifmark > 2:
                print("Invalid Input")
                return
        except:
            print("Invalid Input.")
            return
        if ifmark == 1:
            self.mark_mine(x,y)
            self.show_shown()
        if ifmark == 2:
            temp = self.shown[y][x]
            if temp != "?":
                print("Invalid Input")
                return
            temp = self.grid[y][x]
            if temp == -1:
                print("Boom. You Lose!")
                raise GameOver
            self.shown[y][x] = str(temp)
            if temp == 0:
                self.implicit_move(x, y)
            self.show_shown()
            if self.check_win():
                print("You Win!")
                raise GameOver
            
    
    def implicit_move(self, x, y):
        for hor in range(-1, 2):
            if hor + x < 0:
                continue
            for ver in range(-1, 2):
                if y + ver < 0:
                    continue
                try:
                    if self.shown[y + ver][x + hor] == 0:
                        continue
                    self.shown[y + ver][x + hor] = self.grid[y + ver][x + hor]
                    if self.grid[y + ver][x + hor] == 0:
                        self.implicit_move(x + hor, y + ver)
                except:
                    pass
        # if move reveals a 0, then 
        pass

    def check_win(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] >= 0 and self.shown[y][x] in ["!", "?"]:
                    return False
        return True

        
class GameOver(Exception):
    pass

resume = True
while resume == True:
    try:
        minesweeper(int(input("Board Width? ")), int(input("Board Height? ")), int(input("Mine Count? ")))
        resume = False
    except TypeError:
        print("Input an Integer")
    except GameOver:
        if input("Type 'Continue' to play again. ") != "Continue":
            resume = False
    except:
        print("Unexpected Error")
