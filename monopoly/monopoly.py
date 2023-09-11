import random

class monopoly:
    def __init__(self, playercount):
        self.playercount = playercount
        self.players = [player(x + 1) for x in range(playercount)]
        random.seed()
        self.board = []
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
        # pass go check
        self.checkgopass(currentplayer, firstdie + seconddie)

        # new location effect

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
            # new location effect
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
            print("Doubles! Break out of Jail!")
        currentplayer.location += firstdie + seconddie
        # new location effect
        # prompt actions
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
    def __init__(self, position):
        self.money = 1500
        # get out of jail free cards
        self.gooj = 0
        self.property = []
        self.location = 0
        self.position = position
        self.jailed = -1

class location:
    pass

class go(location):
    pass

class chest(location):
    pass

class chance(location):
    pass

class property(location):
    pass

class util(property):
    pass

class rail(property):
    pass

class norm(property):
    pass

class normA(norm):
    pass

class normB(norm):
    pass

class normC(norm):
    pass

class normD(norm):
    pass

class normE(norm):
    pass

class normF(norm):
    pass

class normG(norm):
    pass

class normH(norm):
    pass

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

