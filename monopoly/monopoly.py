import random
import monopolyboard as board_to_use

class monopoly:
    def __init__(self, playercount):
        self.players = []
        for x in range(1, playercount + 1):
            self.players.append(player(input("Player " + str(x) + " Name? ")))
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
        self.losers = []
        self.comchest_discard = []
        self.chan_discard = []
        self.comchest = board_to_use.chest
        self.chan = board_to_use.chance
        random.shuffle(self.chan)
        random.shuffle(self.comchest)
        for x in range(len(self.players)):
            if self.players[x] not in self.losers:
                self.move(self.players[x])
            if len(self.board) - len(self.losers) == 1:
                break
        for x in self.players:
            if x not in self.losers:
                print("Congragulations " + str(x.name))
        print("Congragulations " + str(self.players[0]))

    def move(self, currentplayer):
        print("Player " + str(currentplayer.name) + " Turn")
        if currentplayer.jailed >= 0:
            self.jailmove(currentplayer)
            if currentplayer.jailed > 0:
                currentplayer.jailed -= 1
                return
            if currentplayer.jailed == -2:
                currentplayer.jailed = -1
                return
        print("Rolling...")
        firstdie, seconddie = d6(), d6()
        doubles = 1
        print(str(firstdie) + ", " + str(seconddie))
        # pass go check. If pass go, add money and set back 40 spaces
        self.checkgopass(currentplayer, firstdie + seconddie)
        currentplayer.location += firstdie + seconddie
        # new location effect
        self.locationeffect(currentplayer)
        # check if lost due to location effect
        if currentplayer in self.losers:
            return
        # if landed on go to jail, this triggers, forcing the doubles trigger not to happen
        if currentplayer.jailed == 3:
            firstdie = 0
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
            self.locationeffect(currentplayer)
            if currentplayer in self.losers:
                return
            if currentplayer.jailed == 3:
                break
        if doubles == 3:
            print("Speeding! Go to Jail!")
            currentplayer.location = 0
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
        if currentplayer.location + roll >= len(self.board):
            currentplayer.money += 200
            currentplayer.location -= len(self.board)
        
    def buyprop(self, currentplayer, prop):
        self.takemoney(currentplayer, prop.buy_price)
        currentplayer.property.append(prop)
        prop.owner = currentplayer

    def locationeffect(self, currentplayer):
        print(currentplayer.location)
        newlocation = self.board[currentplayer.location]
        print(newlocation.name)
        if isinstance(newlocation, free):
            return
        if isinstance(newlocation, property_class):
            self.landprop(currentplayer, self.board[currentplayer.location])
            return
        if isinstance(newlocation, chest):
            self.landchest(currentplayer)
            return
        if isinstance(newlocation, chance):
            self.landchance(currentplayer)
            return
        if isinstance(newlocation, tax):
            self.takemoney(currentplayer, newlocation.payment)
            return
        if isinstance(newlocation, gotojail):
            currentplayer.jailed = 3

    def landprop(self, currentplayer, prop):
        if prop.owner == 0:
            tobuy = input("Do you want to buy it? If so, type '1'")
            if tobuy == 1:
                self.buyprop(currentplayer, prop)

    def landchest(self, currentplayer):
        currentlocation = currentplayer.location
        card = self.comchest.pop()
        print(card[0])
        card[1](currentplayer, self.players)
        for x in self.players:
            self.takemoney(x, 0)
        if currentlocation != currentplayer.location:
            self.locationeffect(currentplayer)
        # if comchest deck empty, put discards in main deck, shuffle(not including unused gooj)
        if len(self.comchest) == 0:
            self.comchest, self.comchest_discard = self.comchest_discard, []
            random.shuffle(self.comchest)

    def landchance(self, currentplayer):
        currentlocation = currentplayer.location
        card = self.chan.pop()
        print(card[0])
        card[1](currentplayer, self.players)
        for x in self.players:
            self.takemoney(x, 0)
        if currentlocation != currentplayer.location:
            self.locationeffect(currentplayer)
        if len(self.chan) == 0:
            self.chan, self.chan_discard = self.chan_discard, []
            random.shuffle(self.chan)


        

    def jailmove(self, currentplayer):
        print("Jailed turns remaining: " + str(currentplayer.jailed))
        if currentplayer.jailed == 0:
            self.takemoney(currentplayer, 50)
            currentplayer.jailed = -1
            return
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
                else:
                    currentplayer.gooj = 0
                currentplayer.jailed = -1
                return
        if input("Player " + str(currentplayer.jailed) + " buy out of jail for $50? Type 'Yes' to buy out. ") == 'Yes':
            self.takemoney(currentplayer, 50)
            currentplayer.jailed = -1
            return
        print("Rolling...")
        firstdie, seconddie = d6(), d6()
        print(str(firstdie) + ", " + str(seconddie))
        if firstdie == seconddie:
            print("Doubles! Break out of Jail! (No Additional Move)")
            currentplayer.jailed == -2
            currentplayer.location += firstdie + seconddie
            self.locationeffect(currentplayer)
            if currentplayer in self.losers:
                return
            return
        if input("Any more actions?(houses, mortgages) Type 'Yes' if so. ") == 'Yes':
            action = input("What action would you like to take? Type '1' to manage houses, Type '2' to manage mortgages. ")
            while action == '1' or action == '2':
                if action == '1':
                    self.managehouses(currentplayer)
                if action == '2':
                    self.managemortgages(currentplayer)
                action = input("Any more actions? Type '1' to manage houses, Type '2' to manage mortgages. ")
        # next player's turn
        
            
    
    def takemoney(self, currentplayer, amount):
        currentplayer.money -= amount
        if currentplayer.money >= 0:
            return
        print(currentplayer + " doesn't have enough money on hand!", "Current Balance: " + str(currentplayer.money), sep = "\n")
        tomanage = []
        for prop in currentplayer.property:
            if prop.houses >= 0:
                # print(prop.name + ": " + str(prop.houses))
                tomanage.append(prop)
        while currentplayer.money < 0 and tomanage != []:
            # get more money through selling houses/mortgaging properties
            for x in range(len(tomanage)):
                print(str(x + 1) + ": " + str(tomanage[x].name), str(tomanage[x].houses))
            
            try:
                print("Do you want to manage houses or mortgage properties?")
                whatdo = input("To manage houses, type '1'. To manage mortgages, type '2'")
                if whatdo not in ['1', '2']:
                    raise
                if whatdo == '1':
                    self.managehouses(currentplayer)
                else:
                    self.managemortgages(currentplayer)
            except:
                print("Invalid Input")
        if currentplayer.money < 0:
            print(currentplayer + " is bankrupt!")
            self.losers.append(currentplayer)

        
    
    def managehouses(self, currentplayer):
        managing = True
        while managing:
            for x in range(len(currentplayer.property)):
                print(str(x + 1) + ": " + str(currentplayer.property[x].name), str(currentplayer.property[x].houses))
            try:
                tomanage = int(input("What property do you want to manage the houses of? Type the number corresponding to the property(to the left of the property in the above list) ")) - 1
                if tomanage not in range(len(currentplayer.property)):
                    raise
                tomanage = currentplayer.property[tomanage]
                if not isinstance(tomanage, norm):
                    raise
            
            except:
                print("Invalid Input")
            # management
            moremanaging = input("Do you want to manage more houses? If so, type '1'")
            if moremanaging != '1':
                managing = False

    def managemortgages(self, currentplayer):
        managing = True
        while managing:
            for x in range(len(currentplayer.property)):
                print(str(x + 1) + ": " + str(currentplayer.property[x].name), str(currentplayer.property[x].houses))
            try:
                tomanage = int(input("What property do you want to manage the mortgages of? Type the number corresponding to the property(to the left of the property in the above list) ")) - 1
                if tomanage not in range(len(currentplayer.property)):
                    raise
                tomanage = currentplayer.property[tomanage]
            except:
                print("Invalid Input")
            moremanaging = input("Do you want to manage more mortgages? If so, type '1'")
            if moremanaging != '1':
                managing = False
        
        
def d6():
    return random.randint(1, 6)


class player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        # get out of jail free cards
        self.gooj = 0
        self.property = []
        self.location = 0
        self.jailed = -1
    def __str__(self):
        return self.name
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

class tax(location):
    def __init__(self, id, name, payment):
        self.payment = payment
        super().__init__(id, name)

class gotojail(location):
    def __init__(self, id, name):
        super().__init__(id, name)

class property_class(location):
    def __init__(self, id, name, buy_price, prices):
        self.buy_price = buy_price
        self.prices = prices
        self.owner = None
        super().__init__(id, name)

class util(property_class):
    def __init__(self, id, name, buy_price, prices):
        super().__init__(id, name, buy_price, prices)

class rail(property_class):
    def __init__(self, id, name, buy_price, prices):
        super().__init__(id, name, buy_price, prices)

class norm(property_class):
    def __init__(self, id, name, buy_price, prices, house_cost):
        self.house_cost = house_cost
        self.houses = 0
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

