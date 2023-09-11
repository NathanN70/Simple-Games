import random

class monopoly:
    def __init__(self, playercount):
        self.playercount = playercount
        self.players = [player(x + 1) for x in range(playercount)]
        random.seed()

    def move(self, currentplayer):
        print("Player " + str(currentplayer.position) + " Turn")
        if currentplayer.jailed >= 0:
            self.jailmove(currentplayer)
            return
        print("Rolling...")
        firstdie = random.randint(1, 6)
        seconddie = random.randint(1, 6)
        doubles = 1
        print(str(firstdie) + ", " + str(seconddie))
        # pass go check
        self.checkgopass(currentplayer, firstdie + seconddie)

        # new location effect

        while firstdie == seconddie:
            print("Doubles! Go Again!")
            print("Rolling...")
            firstdie = random.randint(1, 6)
            seconddie = random.randint(1, 6)
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
        # prompt actions (build houses, manage mortgages, etc.)
        # next player's turn
        

        
    def checkgopass(self, currentplayer, roll):
        if currentplayer.location + roll >= 40:
            currentplayer.money += 200
            currentplayer.location -= 40
        
        
        

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

