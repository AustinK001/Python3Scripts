import os

class playerstats():
 while True :
    def __init__(self, race, level, strength, agility, inteligence, vitality):

         def stats():
            print(players.name)
            print(players.race)
            print("Level: "+ str(players.level) +" Strength: "+ str(players.strength) +" Agility: " + str(players.agility) +" Inteligence: "+ str(players.inteligence) +" Vitality: "+ str(players.vitality))

def racechoice(A):
     #Here race is chosen
    if players.race == "dwarf" or players.race == "Dwarf": #Race starting stats
        players.race = "Dwarf"
        players.level = 1
        players.strength = 12
        players.agility = 6
        players.inteligence = 8
        players.vitality = 14
        print(stats())
    elif players.race == "Orc" or players.race == "orc":
        players.race = "Orc"
        players.level = 1
        players.strength = 14
        players.agility = 10
        players.inteligence = 4
        players.vitality = 12
        print(stats())
    elif players.race == "elf" or player.race == "Elf":
        players.level = 1
        players.race = "Elf"
        players.strength = 8
        players.agility = 13
        players.inteligence = 12
        players.vitality = 7
        print(stats())
    elif players.race == "Human" or player.race == "human":
        players.level = 1
        players.race = "Human"
        players.strength = 10
        players.agility = 10
        players.inteligence = 10
        players.vitality = 10
        print(stats())
    elif players.race == "gnome" or players.race == "Gnome":
        players.race = "Gnome"
        players.strength = 5
        players.agility = 11
        players.intelligence = 17
        players.vitality = 7
        print(stats())
        return
    else:
        print("Not a valid race")
        return racechoice()
A = players.race = input('After you get a chance to think, you choose to be...')
print(A)

        """

There is a problem, you should do:

if players.race == "dwarf" or "players.race == Dwarf":

But even better, change your conditions to:

elif players.race.lower() == "orc":

It is also recommended that you use a class to encapsulate functionality, for example:

class Player(object):
    def __init__(self, race, level, strength, agility, inteligence, vitality):
        self.race = race
        self.level = level
        self.strength = strength
        self.agility = agility
        self.inteligence = inteligence
        self.vitality = vitality

player = Player('Dwarf', 1, 12, 6, 8, 14)

then your racechoice function will look so:

def racechoice():
    race = input('After you get a chance to think, you choose to be...')
    if race.lower() == 'dwarf':
        player = Player('Dwarf', 1, 12, 6, 8, 14)
    elif race.lower() == 'orc':
        player = Player('Orc', 1, 14, 10, 4, 12)
    ...
    return player

"""
