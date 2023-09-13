import random
import monopolyboard as board_to_use

class monopoly:
    def __init__(self, playercount):
        self.playercount = playercount
        self.players = [player(x + 1) for x in range(playercount)]
        random.seed()
        self.board = []
        for square in board_to_use.board:
            squaretype = square[0][0]
            if squaretype == "X":
                self.board.append(free(square[0], square[1]))
            if squaretype == "Y":
                self.board.append(chest(square[0], square[1]))
            if squaretype == "Z":
                self.board.append(chance(square[0], square[1]))
            if squaretype == "R":
                self.board.append(rail(square[0], square[1], square[2], square[3]))
            if squaretype == "U":
                self.board.append(util(square[0], square[1], square[2], square[3]))
            if squaretype in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                self.board.append(norm(square[0], square[1], square[2], square[3], square[4]))
        # initialize board

    def move(self, currentplayer):
        print("Player " + str(currentplayer.position) + " Turn")
        if currentplayer.jailed >= 0:
            self.jailmove(currentplayer)
            return
        print("Rolling...")
        firstdie, seconddie = d6(), d6()
        doubles = 1
        print(str(firstdie) + ", " + str(seconddie))
        # pass go check. If pass go, add money and set back 40 spaces
        self.checkgopass(currentplayer, firstdie + seconddie)
        currentplayer.location += firstdie + seconddie
        # new location effect
        self.locationeffect(player)

        while firstdie == seconddie:
            print("Doubles! Go Again!")
            print("Rolling...")
            firstdie, seconddie = d6(), d6()
            print(str(firstdie) + ", " + str(seconddie))
            if firstdie == seconddie:
                doubles += 1
                if doubles == 3:
                    break
            self.checkgopass(currentplayer, firstdie + seconddie)
            currentplayer.location += firstdie + seconddie
            self.locationeffect(player)
        if doubles == 3:
            print("Speeding! Go to Jail!")
            currentplayer.location = 10
            currentplayer.jailed = 3
        if input("Any more actions?(houses, mortgages) Type 'Yes' if so. ") == 'Yes':
            action = input("What action would you like to take? Type '1' to manage houses, Type '2' to manage mortgages. ")
            while action != '1' and action != '2':
                if action == '1':
                    self.managehouses(currentplayer)
                if action == '2':
                    self.managemortgages(currentplayer)
                action = input("Any more actions? Type '1' to manage houses, Type '2' to manage mortgages. ")
                
        # prompt actions (build houses, manage mortgages, etc.)
        # next player's turn
        

        
    def checkgopass(self, currentplayer, roll):
        if currentplayer.location + roll >= self.board(len):
            currentplayer.money += 200
            currentplayer.location -= self.board(len)
        
    def buyprop(self, player, prop):
        self.takemoney(player, prop.buy_price)
        player.property.append(prop)
        prop.owner = player

    def locationeffect(self, player):
        newlocation = self.board[player]
        print(newlocation.name)
        if isinstance(newlocation, free):
            return
        if isinstance(newlocation, property):
            self.landprop(player)
            return
        if isinstance(newlocation, chest):
            self.landchest(player)
            return
        if isinstance(newlocation, chance):
            self.landchance(player)

    def landprop(self, player, prop):
        if prop.owner == 0:
            tobuy = input("Do you want to buy it? If so, type '1'")
            if tobuy == 1:
                self.buyprop(player, prop)

    def landchest(self, player):
        pass

    def landchance(self, player):
        pass

        

    def jailmove(self, currentplayer):
        if currentplayer.gooj != 0:
            print(str(currentplayer.jailed) + " Turns remaining in jail.")
            usegooj = input("Do you want to use a Get Out of Jail Free card? If yes, type 'Yes'. If not type anything else. ")
            if usegooj == "Yes":
                if currentplayer.gooj == 3:
                    whichgooj = input("Which one do you want to use? To use the community chest one, type '1'. To use the chance one, type anything else. ")
                    if whichgooj == '1':
                        currentplayer.gooj -= 1
                        #put gooj in chest discard
                    else:
                        currentplayer.gooj -= 2
                        #put gooj in chance discard
                currentplayer.jailed == -1
                self.move(currentplayer)
                return
        if currentplayer.jailed == 0:
            self.takemoney(currentplayer, 50)
            return
        if 'Yes' == input("Player " + str(currentplayer.position) + " buy out of jail for $50? Type 'Yes' to buy out. "):
            self.takemoney(currentplayer, 50)
            return
        print("Rolling...")
        firstdie = random.randint(1, 6)
        seconddie = random.randint(1, 6)
        print(str(firstdie) + ", " + str(seconddie))
        if firstdie == seconddie:
            print("Doubles! Break out of Jail! (No Additional Move)")
        currentplayer.location += firstdie + seconddie
        self.locationeffect(player)
        if input("Any more actions?(houses, mortgages) Type 'Yes' if so. ") == 'Yes':
            action = input("What action would you like to take? Type '1' to manage houses, Type '2' to manage mortgages. ")
            while action != '1' and action != '2':
                if action == '1':
                    self.managehouses(currentplayer)
                if action == '2':
                    self.managemortgages(currentplayer)
                action = input("Any more actions? Type '1' to manage houses, Type '2' to manage mortgages. ")
        # next player's turn
        
            
    
    def takemoney(self, player, amount):
        player.money -= amount
        if player.money >= 0:
            return
        # get more money through selling/mortgaging properties
    
    def managehouses(self, player):
        managing = True
        while managing:
            for prop in player.property:
                print(prop, prop.houses)
            tomanage = input("What property do you want to manage the houses of? ")
            # management
            moremanaging = input("Do you want to manage more houses? If so, type '1'")
            if moremanaging != '1':
                managing = False

    def managemortgages(self, player):
        managing = True
        while managing:
            for prop in player.property:
                print(prop, prop.houses)
            tomanage = input("What property do you want to manage the houses of? ")
            # management
            moremanaging = input("Do you want to manage more houses? If so, type '1'")
            if moremanaging != '1':
                managing = False
        
        
def d6():
    return random.randint(1, 6)


class player:
    def __init__(self, turn_order):
        self.money = 1500
        # get out of jail free cards
        self.gooj = 0
        self.property = []
        self.location = 0
        self.turn_order = turn_order
        self.jailed = -1
# location id based on code system. Letter, then Number. Normal props, Letters A-H each represent a district. The number (1-3) represents different props in the district
# for free spaces, letter X, number system same
# for rails and utility, letters R and U (rails number 1-4)
# for chest and chance, letters Y and Z
class location:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class free(location):
    def __init__(self, id, name):
        super().__init__(id, name)

class chest(location):
    def __init__(self, id, name):
        super().__init__(id, name)

class chance(location):
    def __init__(self, id, name):
        super().__init__(id, name)

class property(location):
    def __init__(self, id, name, buy_price, prices):
        self.buy_price = buy_price
        self.prices = prices
        self.owner = 0
        super().__init__(id, name)

class util(property):
    def __init__(self, id, name, buy_price, prices):
        super().__init__(id, name, buy_price, prices)

class rail(property):
    def __init__(self, id, name, buy_price, prices):
        super().__init__(id, name, buy_price, prices)

class norm(property):
    def __init__(self, id, name, buy_price, prices, house_cost):
        self.house_cost = house_cost
        super().__init__(id, name, buy_price, prices)

class GameOver(Exception):
    pass

resume = True
while resume == True:
    try:
        playercount = int(input("Player Count? "))
        if playercount < 2 or playercount > 8:
            raise TypeError
        monopoly(playercount)
        resume = False
    except TypeError:
        print("Input an Integer from 2-8")
    except GameOver:
        resume = False
    except:
        print("Unexpected Error")

