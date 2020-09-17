import pickle
#Loop
menu_active = True
game_active = True
tutorial1 = True
chapter1 = False
#Story Switches
chapter = '0'
part = '1'
tutorComp = False
switch = [True, False, False, False]
tutorialSwitch = [True, True, True, True, True]
#Character Base Stats
class Alder:
    def __init__(self):
        self.name = 'Alder'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStamina = 100
        self.stamina = self.maxStamina
        self.cLvl = 1
        self.cExp = 0
        self.baseAttack = 10
        self.baseDefence = 10
        self.baseSpeed = 5
        self.baseEvasion = 5
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
        self.weapon1 = weapons[0]
        self.weapon2 = 'None'
    property
    def attack(self):
        attack = self.baseAttack
        if (self.weapon1['wpId'] != '0'):
            attack += self.weapon1['attack']
        else:
            attack += 0
        return attack
    property
    def defence(self):
        defence = self.baseDefence
        if (self.head['type'] == 'hat'):
            defence += self.head['defence']
        if (self.body['type'] == 'shirt'):
            defence += self.body['defence']
        if (self.legs['type'] == 'trousers'):
            defence += self.legs['defence']
        return defence
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        return evasion
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nSpeed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2, '\n'
              )
        
#Alder = {'pId' : '1', 'name' : 'Alder', 'combatLvl' : '1', 'combatExp' : 0,
#         'maxHealth': 100, 'baseAttack' : 10, 'baseDefence' : 10, 'baseSpeed' : 5, 'baseEvasion' : 5, 'maxStamina' : 100,
#         'head' : 'None', 'body' : '1', 'legs' : '2', 'weapon1' : 'None', 'weapon2': 'None'
#         }
Florace = {'pId' : '2', 'name' : 'Florace', 'combatLvl' : '1', 'combatExp' : 0,
         'maxHealth': 150, 'attack' : 15, 'defence' : 10, 'speed' : 7, 'evasion' : 2, 'maxStamina' : 100,
         'head' : 'None', 'body' : 'Apprentice Witch Shirt', 'legs' : 'Apprentice Witch Dress', 'weapon1' : 'None', 'weapon2': 'None'
         }
party = [{'pId' : '1', 'name' : 'Alder', 'title' : 'Servant', 'species' : 'Human', 'inParty' : True},
         {'pId' : '2', 'name' : 'Florace', 'title' : 'Gaurdian', 'species' : 'Human', 'inParty' : False},
         {'pId' : '3', 'name' : 'Dean', 'title' : 'Watch Squire', 'species' : 'Water Shrew', 'inParty' : False}
         ]
#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'weapon', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'weapon', 'description' : 'Legendary sword of the Scion.',
            'attack' : 100, 'weight' : 5, 'count' : 0},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'weapon', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0}
           ]

armors = [{'armId' : '1', 'name' : 'None', 'type' : 'hat', 'description' : '',
          'defence' : 0, 'weight' : 0, 'count' : 0},
          {'armId' : '1', 'name' : 'Old Tunic', 'type' : 'shirt', 'description' : 'An old shirt with holes in it.',
          'defence' : 1, 'weight' : 1, 'count' : 0},
          {'armId' : '2', 'name' : 'Travelling Cloak', 'type' : 'shirt', 'description' : 'A too large black cloak. Good for keeping ou of sight but heavy.',
          'defence' : 10, 'weight' : 10, 'count' : 0},
          {'armId' : '1', 'name' : 'Worn Trousers', 'type' : 'trousers', 'description' : 'An old pair of trousers long past their prime',
          'defence' : 1, 'weight' : 1, 'count' : 0}
          ]
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : 'food',
          'recovers' : 5, 'count' : 0},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : 'food',
          'recovers' : 5, 'count' : 0},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : 'food',
          'recovers' : 5, 'count' : 0}
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0}
         ]
#Inventory
shill = 0
inv = []
PKSwitch = [True, True]

#Location
locations = [{"locId" : "1", "name" : "Cottage Kitchen"},
             {"locId" : "2", "name" : "Cottage Living Room"},
             {"locId" : "3", "name" : "Outside Cottage"},
             {"locId" : "4", "name" : "Cottage Shed"},
             {"locId" : "5", "name" : "Alder's Room"},
             {"locId" : "6", "name" : "Forest Clearing"}
             ]
location = '1'
#Interactable characters
actor = {'actorId' : '1', 'name' : 'Florace', 'locationID' : '1', 'room' : '3', 'chapter' : '1', 'part' : '1', 'dialogue' : ''}
#Save and Load Content
PIK = 'demo.dat'
data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, shill, inv, PKSwitch]

#Set Class
alder = Alder()

def cont():
    con = input()
    if (con == 'skip'):
        return
#Increment/Decrement Shillings
def shillings(m):
    global shill
    if (m < 0):
        m == 0
    shill += m
    print('Shillings: ', shill)
#Increment items
#Add a new item to the inventory if is is not already in there
def itemCount(item, amount):
    inInv = False
    for i in inv:
        if (item['type'] == 'weapon' and i['type'] == 'weapon'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'armor' and i['type'] == 'armor'):
            if (i['armId'] == item['armId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'food' and i['type'] == 'food'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'healing' and i['type'] == 'healing'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] += amount
        inv.append(item)

#The item should be equipped
#If the item is not starting clothing then it should be return to the inventory
#Only items of speciec type can be equiped
def equip():
    equiping = True
    while (equiping == True):
        equipable = []
        print('\nEquip what')
        print('1: Head')
        print('2: Body')
        print('3: Legs')
        print('4: Weapon - A')
        print('5: Weapon - B')
        print('e - Exit')
        i = input('Action: ')
        if (i == '1'):
            count = 0
            for i in inv:
                if(i['type'] == 'hat'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.head['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.head['armId'] != '0'):
                            inv.append(alder.head)
                        alder.head = i
                        i['count'] -= 1
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '2'):
            count = 0
            for i in inv:
                if(i['type'] == 'shirt'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.body['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.body['armId'] != '1'):
                            inv.append(alder.body)
                        alder.body = i
                        i['count'] -= 1
                        print(i['count'])
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '3'):
            count = 0
            for i in inv:
                if(i['type'] == 'trousers'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.legs['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.legs['armId'] != '1'):
                            inv.append(alder.legs)
                        alder.legs = i
                        i['count'] -= 1
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '4'):
            count = 0
            for i in inv:
                if(i['type'] == 'weapon'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon1['attack'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.weapon1['wpId'] != '0'):
                            inv.append(alder.weapon1)
                        alder.weapon1 = i
                        i['count'] -= 1
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '5'):
            count = 0
            for i in inv:
                if(i['type'] == 'weapon2'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon2['attack'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.weapon1['wpId'] != '0'):
                            inv.append(alder.weapon2)
                        alder.weapon2 = i
                        i['count'] -= 1
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == 'e'):
            equiping = False

#Examine background object
def examine(location):
    if (location == '1'):
        print('The cottage kitchen contained various pots and pans hanging on the wall. It had a stove where a cauldron was dangled on a chain. There a cupboard and two tables one of which had an empty bowl on it. Alder had been washing dishes in a basin on the other table next to the window.')
        e = input('Examine: ')
        if (e == 'cauldron' or e == 'Cauldron'):
            print("It was a small metal cauldron above the stove suspended by a chain. It was empty right now.")
            cont()
        elif (e == 'cupboard' or e == 'Cupboard'):
            print('The Cupboard was full of plates, bowls and other kitchen and dining utensils.')
            cont()
        elif (e == 'bowl' or e == 'Bowl'):
            print('A large wooden bowl. It'"'"'s empty.')
            cont()
        elif (e == 'basin' or e == 'Basin'):
            print('The basin Alder was washing was full of water and bits of leftover that Alder scraped off. Clean plates were next to it.')
            cont()
        elif (e == 'window' or e == 'Window'):
            print('Florace and Thay were talking on the other side of the window.')
            cont()
            print('Alder:')
            print('"I'"'"'m coming out"')
            cont()
            tutorialSwitch[0] = False
        else:
            print('Alder thought about it, but it was of no intrest to him.')
            cont()
    elif (location == '2'):
        print('The living room was a homely place that was accessible by both the front and back doors. It had two chairs and a table in front of a fireplace as well as a single bookshelf with three shelves full of books.')
        e = input('Examine: ')
        if (e == 'bookshelf' or e == 'Bookshelf'):
            print("The bookshelf contained several books on magic spells, potions and artefacts. There were also a few romantic kinds of literature with male characters completely absent from their pages.")
            cont()
        elif (e == 'fireplace' or e == 'Fireplace'):
            print('The fireplace was unlit. It was used last night and still had ash and soot in it.')
            cont()
            print('Alder:')
            print('"I’ll clean it up later."')
            cont()
        else:
            print('Alder thought about it, but it was of no interest to him.')
            cont()
    elif (location == '3'):
        print('The burrow as the inhabitants called it was hidden from the world in a strange place. The sky rippled like water and several strange plant life and large mushroom sprouted on vacant patches or on top the trees and stones of the forest where there weren’t any when you went left the burrow, revealing a concealed world full of strange beauty. Around the corner of the cottage where Alder lived, there was an old shed with a slanted roof, in front of it was a deep man-size hole and nearby was a large blackberry bush.')
        e = input('Examine: ')
        if (e == 'sky' or e == 'Sky'):
            print('Ripples in the sky were like a flag that told Alder and all others that they were within the boundaries of the burrow.')
            cont()
        elif (e == 'mushroom' or e == 'Mushroom'):
            print('A There was a variety of mushrooms around the cottage, on the trees and in vacant areas of the woodland earth. Some of them were nearly as big as the cottage. Insects would fly straight through them as if they were nothing but an illusion.')
            cont()
        elif (e == 'plants' or e == 'Plants'):
            print('In addition to the various weeds and flowers, there was some strange purple moss that disappeared during the night and yellow flowers that sprayed a sticky fluid at anyone in the burrow who got to close.')
            cont()
        elif (e == 'trees' or e == 'Trees'):
            print('Various trees made up the woodland, the most frequent were birch, rowen and holly.')
            cont()
        elif (e == 'rocks' or e == 'Rocks'):
            print('There were a few boulders in the area. None of them was as big as the cottage.')
            cont()
        elif (e == 'cottage' or e == 'Cottage'):
            print('The cottage was extravagant for only three people. It had two floors and was made from white clay bricks.')
            cont()
        elif (e == 'shed' or e == 'Shed'):
            print('It was made of entirely of splintered wooden planks and had a single door with no windows.')
            cont()
        elif (e == 'hole' or e == 'Hole'):
            print('The ditch in the earth was deep enough for Alder to fit in.')
            cont()
        elif (e == 'bush' or e == 'Bush' or e == 'blackberry' or e == 'Blackberry' or e == 'blackberry bush' or e == 'Blackberry Bush'):
            print('The blackberry bush was a camouflaged into a holly bush by Kyla’s magic. This was so they would not attract unwanted guests to the area. It still had a few blackberries on it.')
            cont()
    elif (location == '4'):
        print('The inside of the shed was illuminated by a window on the left side from the entrance. It was full of gathering, woodwork and gardening tools which were used by Alder, and pots and creates containing ingredients of magic potions. At the other end from the entrance was a table used for crafts.')
        e = input('Examine: ')
        if (e == 'window' or e == 'Window'):
            print('A single window on the left side of the room.')
            cont()
            print('Outside the woods could be seen.')
            cont()
        elif (e == 'tools' or e == 'Tools' or e == 'axe' or e == 'Axe' or e == 'saw' or e == 'Saw' or
              e == 'pick' or e == 'Pick' or e == 'shovel' or e == 'Shovel' or e == 'sickle' or e == 'Sickle' or
              e == 'rod' or e == 'Rod' or e == 'fishing' or e == 'Fishing' or e == 'fishing rod' or e == 'Fishing rod'):
            print('Various tools were hung on the wall and sat on the shelves.')
            cont()
            print('They included an axe, saw, pick, shovel, sickle and fishing rod.')
            cont()
            print('Alder did not need any of them.')
            cont()
        elif (e == 'pots' or e == 'Pots'):
            print('The pots contained ingredients for potions.')
            cont()
            print('They were left in the shed to save space indoors.')
            cont()
            print('One of the pots was full of eyeballs.')
            cont()
        elif (e == 'crates' or e == 'Crates' or e == 'boxes' or e == 'Boxes'):
            print('Kyla had put space magical tools in boxes to keep them from breaking.')
            cont()
        elif (e == 'table' or e == 'Table'):
            if (PKSwitch[1] == True):
                print('On the table was an unlit candle, a mortar and pestle and a hunting knife.')
            else:
                print('On the table was an unlit candle and a mortar and pestle')
            cont()
            if (tutorialSwitch[3] == False):
                if (PKSwitch[1] == True):
                    pickup = input('Do you want to pick up the hunting knife.(y/n)')
                    if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                        print('\nHunting Knife obtained')
                        itemCount(weapons[2], 1)
                        PKSwitch[1] = False
                        cont()
        elif (e == 'candle' or e == 'Candle'):
            print('The candle was placed in a candlestick.')
            cont()
            print('It was unlit.')
            cont()
        elif (e == 'mortar' or e == 'Mortar' or e == 'pestle' or e == 'Pestle'):
            print('A mortar and pestle were on the table.')
            cont()
            print('Florace recently used it to grind ingredients for potions.')
            cont()
        elif (e == 'knife' or e == 'Knife'):
            print('The knife was designed for hunting but it looks like someone has been using it to cut ingredients.')
            cont()
        
#Pick-up item
def pick(location):
    if (location == '1'):
        print('There was nothing to pick up that wouldn'"'"'t be stealing')
        cont()

#Talk to a character
def talk():
    global switch, tutorial1, part
    if (location == '1'):
        print('There was no one to talk to')
    elif (location == '2'):
        print('There was no one to talk to')
    elif (location == '3'):
        if (tutorialSwitch[2] == True):
            print('1: Florace')
            t = input('talk to: ')
            if (t == '1'):
                dialog = [False, False]
                while(dialog[0] == False or dialog[1] == False):
                    print('1: "So what'"'"'s Thay here for?"')
                    print('2: "How does the magic around the cottage work again?"')
                    c = input('Alder: ')
                    if (c == '1'):
                        print('Florace:')
                        print('"Potions probably."')
                        cont()
                        print('Florace:')
                        print('"He usually comes here for sanctuary or phantom cloak potion."')
                        cont()
                        dialog[0] = True
                    if (c == '2'):
                        print('Florace:')
                        print('"Kyla’s spell hides the cottage in the Wyrd while disguising it as a rock in the Wild."')
                        cont()
                        print('Alder:')
                        print('"I still don’t understand what you mean by Wyrd and Wild?"')
                        cont()
                        print('Florace:')
                        print('"Well there are two realms."')
                        cont()
                        print('Florace:')
                        print('"The world of fairies that we called the Wyrd and the world of men, mice and such that the fairies call the Wild."')
                        cont()
                        print('Florace:')
                        print('"The latter is where we are from."')
                        cont()
                        print('Florace:')
                        print('"The former is where we are."')
                        cont()
                        print('Florace:')
                        print('"You can see plants and animals from both so long as you are here."')
                        cont()
                        print('Florace:')
                        print('"It’s not entirely accurate but we tend to call this place the burrow."')
                        cont()
                        dialog[1] = True
                switch[2] = True
                tutorial1 = False
                tutorialSwitch[2] = False
        elif (tutorialSwitch[3] == True):
            print('1: Thay')
            t = input('talk to: ')
            if (t == '1'):
                dialog = [False, False, False]
                dialog2 = [False, False, False, False, False]
                while(dialog[0] == False or dialog[1] == False or dialog2[4] == False):
                    print('1: "How was your journey?"')
                    print('2: "How did it go with Madame Kyla?"')
                    print('3: "What'"'"'s it like outside the burrow?"')
                    if (dialog[2] == True):
                        print('4: What can you tell me about the woods?')
                        print('5: What can you tell me about the the mouse village?')
                        print('6: What can you tell me about the river?')
                        print('7: What can you tell me about the hill?')
                        print('8: Why are humans so hated?')
                    c = input('Alder: ')
                    if (c == '1'):
                        print('Thay:')
                        print('"It was quite lovely."')
                        cont()
                        print('Thay:')
                        print('"The summer has been good to us all."')
                        cont()
                        dialog[0] = True
                    if (c == '2'):
                        print('Thay:')
                        print('"The usual gave her the herbs she wanted and she gave me the potions I needed."')
                        cont()
                        print('Thay takes out a vial of pieces of black liquid it was Phantom Cloak. It was a magic potion that erased a creature’s presence when in darkness. It was one of many potions that brought patrons to the cottage. Alder never asked what they needed them for.')
                        cont()
                        dialog[1] = True
                    if (c == '3'):
                        print('Thay:')
                        print('"Well, to the north, there are mostly deep woodlands, nothing much there."')
                        cont()
                        print('Thay:')
                        print('"But to the south, is the settlement in the valley where mice and other small beasts live."')
                        cont()
                        print('Thay:')
                        print('"In the west, you’ll run into the river and if you climb to the treetops you can see a hare hill in the east."')
                        cont()
                        print('Thay:')
                        print('"Wait?"')
                        cont()
                        print('With sudden realization of who he was speaking to, Thay panicked at the thought of feeding the curiosity of the boy.')
                        cont()
                        print('Thay:')
                        print('"Alder you aren'"'"'t thinking of going to these places are you!?"')
                        cont()
                        print('Alder:')
                        print('"I..."')
                        cont()
                        print('Alder:')
                        print('"think it would be nice."')
                        cont()
                        print('Thay:')
                        print('"No!"')
                        cont()
                        print('Thay:')
                        print('"NO!! Alder!"')
                        cont()
                        print('Thay:')
                        print('"It’s too dangerous!!"')
                        cont()
                        print('Thay:')
                        print('"If anyone sees you will be hunted and killed!!"')
                        cont()
                        print('Thay:')
                        print('"I cannot exaggerate how much humans are hated!!"')
                        cont()
                        print('Alder:')
                        print('"Ok! Ok!"')
                        cont()
                        print('Alder:')
                        print('"I won’t go wandering!!"')
                        cont()
                        print('Alder:')
                        print('"I'"'"'m Sorry!"')
                        cont()
                        print('Thay:')
                        print('"I hope not!"')
                        cont()
                        print('Thay:')
                        print('"I’d never forgive myself if something were to happen to you."')
                        cont()
                        print('Alder realized that the hedgehog was getting agitated and so decided to move on.')
                        cont()
                        dialog[2] = True
                    if (dialog[2] == True):
                        if (c == '4'):
                            print('Alder:')
                            print('"It’s not that I want to go there but I’d like to know."')
                            cont()
                            print('Thay:')
                            print('"Oldwyrm wood is where we are right now."')
                            cont()
                            print('Thay:')
                            print('"It is an ancient wood that goes on for miles."')
                            cont()
                            print('Thay:')
                            print('"Some of the trees are so old and big that creatures have made their homes in its roots and trees."')
                            cont()
                            print('Thay:')
                            print('"But be warned it is also home to birds of prey and bugs big enough to attack travelers."')
                            cont()
                            dialog2[0] = True
                        if (c == '5'):
                            print('Alder:')
                            print('"It’s not that I want to go there but I’d like to know."')
                            cont()
                            print('Thay:')
                            print('"It’s called Fort Town."')
                            cont()
                            print('Thay:')
                            print('"It’s known for its great library, taking in orphans within the region and being the resting place of the hero Agrimus."')
                            cont()
                            print('Thay:')
                            print('"It is also one of the few mouse settlements that is not controlled by the woodland church."')
                            cont()
                            dialog2[1] = True
                        if (c == '6'):
                            print('Alder:')
                            print('"Me and Florace do sometimes go there to get water."')
                            cont()
                            print('Alder:')
                            print('"With caution of course."')
                            cont()
                            print('Alder:')
                            print('"Once we caught a fish in our bucket."')
                            cont()
                            print('Thay:')
                            print('"Hmm."')
                            cont()
                            print('Thay:')
                            print('"You sure that’s safe?"')
                            cont()
                            print('Thay:')
                            print('"There'"'"'s also a lot of creatures drifting on the river as well."')
                            cont()
                            print('Thay:')
                            print('"Swimming in it too."')
                            cont()
                            print('Alder:')
                            print('"It’s alright."')
                            cont()
                            print('Alder:')
                            print('"Florence has always kept up hidden."')
                            cont()
                            print('Thay:')
                            print('"Err, o-ok then."')
                            cont()
                            dialog2[2] = True
                        if (c == '7'):
                            print('Alder:')
                            print('"It’s not that I want to go there but I’d like to know."')
                            cont()
                            print('Thay:')
                            print('"Hare Hill is the largest hill in the region."')
                            cont()
                            print('Thay:')
                            print('"It is home to many hare and rabbit villages."')
                            cont()
                            print('Thay:')
                            print('"At the top is the capital of Breabuck."')
                            cont()
                            print('Thay:')
                            print('"But it is a difficult and exhausting walk and travels need to scramble up rock walls in some places."')
                            cont()
                            print('Thay:')
                            print('"Unless they go through the rabbits tunnels."')
                            cont()
                            print('Thay:')
                            print('"Oh!"')
                            cont()
                            print('Thay:')
                            print('"Nevermind."')
                            cont()
                            print('Alder:')
                            print('"What?"')
                            cont()
                            print('Thay:')
                            print('"Just."')
                            cont()
                            print('Thay:')
                            print('"Nevermind."')
                            cont()
                            dialog2[3] = True
                        if (c == '8'):
                            print('Thay:')
                            print('"Well."')
                            cont()
                            print('Thay:')
                            print('"There was a certain king who did very, very bad things."')
                            cont()
                            print('Alder:')
                            print('"What kinds of things?"')
                            cont()
                            print('Thay:')
                            print('"Things you'"'"'re too young to know."')
                            cont()
                            print('Thay:')
                            print('"But all you need to know is that he was cruel and unforgivable."')
                            cont()
                            print('Thay:')
                            print('"So unforgivable in fact that along with his followers, woodland folk even took vengeance on the humans who were against him."')
                            cont()
                            print('Alder:')
                            print('"But why?"')
                            cont()
                            print('Alder:')
                            print('"In what way were they involved?"')
                            cont()
                            print('Thay:')
                            print('"They weren'"'"'t."')
                            cont()
                            print('Thay:')
                            print('"But that doesn’t matter to those who had lost friends and family in the conflict."')
                            cont()
                            print('Thay:')
                            print('"Best for you to stay within the burrows border young one."')
                            cont()
                            print('Thay:')
                            print('"If you are seen."')
                            cont()
                            print('Thay:')
                            print('"You will be assumed alined with the kings ideals and killed."')
                            cont()
                            print('Alder gave a sad longing look to the deep wood. He’d like to see more than the tiny patch he called home. But alas as Thay said, the danger was too great.')
                            cont()
                            dialog2[4] = True
                switch[3] = True
                part = '3'
                tutorial1 = False
#Move to another location
def move():
    global location, part, tutorial1, tutorialSwitch
    if (location == '1'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            print('Alder moved to the living room of the cottage.')    
            cont()
    elif (location == '2'):
        print('1: Kitchen')
        print('2: Outside')
        m = input('Move to: ')
        if (m == '1'):
            location = '1'
            print('Alder moved to the kitchen.')    
            cont()
        elif (m == '2'):
            location = '3'
            print('Alder moved outside the cottage through the front door.')
            cont()
            if(tutorialSwitch[1] == True):
                part = '2'
                tutorialSwitch[1] = False
                switch[1] = True
                tutorial1 = False
                tutorialSwitch[3] = False
    elif (location == '3'):
        print('1: Living Room')
        print('2: Shed')
        print('3: Leave cottage')
        m = input('Move to: ')
        if (m == '1'):
            if (tutorialSwitch[2] == False):
                print('Alder moved to the living room of the cottage.')    
                cont()
                print('Kyla:')
                print('"Hm!?"')
                cont()
                print('Kyla:')
                print('"What are you doing in here boy!?"')
                cont()
                print('Alder:')
                print('"Um?"')
                cont()
                print('Kyla:')
                print('"Get out there and entertain our guest!"')
                cont()
                print('Alder withdraws from the cottage.')    
                cont()
            else:
                location = '1'
                print('Alder moved to the living room of the cottage.')    
                cont()
        elif (m == '2'):        
            location = '4'
            print('Alder moved to the shed on the side of the cottage.')    
            cont()
        elif (m == '3'):
            if (tutorialSwitch[3] == False):
                location = '6'
                print('Alder left the area of the spell hiding the cottage.')    
                cont()
            else:
                print('Alder once got lost after he strayed too far from the cottage.')
                cont()
                print('He spend hours in the dark until Florace found him crying and scared.')
                cont()
                print('Kyla was indifferent to the situation.')
                cont()

#Save the game
def save(location, chapter, part):
    data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, shill, inv, PKSwitch]
    print (data)
    print (location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, shill, inv, PKSwitch)
    with open(PIK, "wb") as f:
        print(data)
        pickle.dump(data, f)
    print ('Game Saved!')

def inventory():
    bag = True
    while(bag == True):
        #View the items in inventory
        #The same items should be counted to keep the list clear
        print('\nInventory')
        print('Shillings: ', shill)
        count = 1
        for i in inv:
            print(count, ') ', i['name'], ' x', i['count'])
            count += 1
        print('\n1: Appraise')
        print('2: Equip')
        print('e - Exit')
        i = input('Action: ')

        #Appraise items in inventory
        if (i == '1'):
            appraise = input('\nItem number: ')
            count = 1
            for i in inv:
                if (appraise == str(count)):
                    if (i['type'] != 'food'):
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nDescription: ', i['description'])
                    else:
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nStamina Recovered: ', i['recovers'])
                count += 1
        elif (i == '2'):
            equip()
        elif (i == 'e'):
            print()
            bag = False


def freeTutorial(location, chapter, part):
    global game_active, tutorial1
    if(tutorialSwitch[0] == True):
        print('You will need to have a quick look around. Press "a" to interact with the world.')
    elif(tutorialSwitch[1] == True):
        print('Alder needs to go outside. He will have to move through the living room and then outside.')
    elif(tutorialSwitch[2] == True):
        print('While we wait for Thay Let'"'"'s talk to Florace.')
    print('a - Action')
    print('s - Save')
    print('q - Quit')
    action = input('Enter Command: ')
    print(switch[2])
    if (action == 'a'):
        print('e - Examine')
        if(tutorialSwitch[0] == False):
            print('m - Move')
        if(tutorialSwitch[1] == False):
            print('t - Talk')
        action = input('Enter Command: ')
        if (action == 'e'):
            examine(location)
        if(tutorialSwitch[0] == False):
            if (action == 'm'):
                move()
        if(tutorialSwitch[1] == False):
            if (action == 't'):
                talk()
    if (action == 's'):
        save(location, chapter, part)
    if (action == 'q'):
        print ("Are you sure you wan to quit to menu y/n")
        q = input('Enter Command: ')
        if (q == 'y' or q == 'Y' or q == 'yes' or q == 'Yes'):
            tutorial1 = False
            game_active = False
            
def free(location, chapter, part):
    global game_active, tutorial1
    if(tutorialSwitch[0] == True):
        print('You will need to have a quick look around. Press "a" to interact with the world.')
    elif(tutorialSwitch[1] == True):
        print('Alder needs to go outside. He will have to move through the living room and then outside.')
    elif(tutorialSwitch[2] == True):
        print('While we wait for Thay Let'"'"'s talk to Florace.')
    print('a - Action')
    print('o - Options')
    print('s - Save')
    print('q - Quit')
    #r = open("wawPrologue.txt","r")
    action = input('Enter Command: ')
    if (action == 'a'):
        print('e - Examine')
        print('t - Talk')
        print('m - Move')
        action = input('Enter Command: ')
        if (action == 'e'):
            examine(location)
        elif (action == 't'):
            talk()
        elif (action == 'm'):
            move()
    elif (action == 'o'):
        print('z - Status')
        print('o - Objective')
        print('i - Inventory')
        print('e - Equipment')
        action = input('Enter Command: ')
        if (action == 'z'):
            alder.stats()
        elif (action == 'i'):
            inventory()
        elif (action == 'e'):
            equip()
    
    elif (action == 's'):
        save(location, chapter, part)
    elif (action == 'q'):
        print ("Are you sure you wan to quit to menu y/n")
        q = input('Enter Command: ')
        if (q == 'y' or q == 'Y' or q == 'yes' or q == 'Yes'):
            game_active = False

def game(chapter):
    global switch, tutorial1, location
    print('Chapter: ', chapter)
    print('The game will now begin. For then next line to print press enter.')
    print('You may skip the dialoge by typing skip then pressing enter.')
    while (game_active == True):
        if (tutorComp == False):
            tutorial1 = True
        if (chapter == '0'):
            prologue = True
            print('Prolouge')
            print('In the corridors of a Fort within the upper left of a green field of a valley near the edge of the deep woods and at the foot of a great hill, two of its dwellers were discussing plans for the days to come. They were the lord, an old greyish field mouse and a pudgy vole brother both in brown clothing. They were discussing daily matters and had taken their talks to a corridor overseeing the great hall filled with tapestries for the warriors and wise creatures their order worships, cut off from the sunlight of the outside.')
            cont()
            print('It is long into their conversation about their upcoming feast when a young shrew came running from under the archway leading from the nursing chambers. The section of the abbey that served as an orphanage. He was calling for the mouse abbot and panted as he spoke.')
            cont()
            print('Shrew:')
            print('"My Lord!"')
            cont()
            print('Shrew:')
            print('*Pant* "Excuse me!"')
            cont()
            print('Shrew:')
            print('*Pant* *Pant* "Lord Dilecto!"')
            cont()
            print('Dilecto:')
            print('"Hm?"')
            cont()
            print('Dilecto:')
            print('"Yes child?"')
            cont()
            print('Shrew:')
            print('*Ahem* "Hazel is requesting a meeting."')
            cont()
            print('Vole:')
            print('"He has no authority to call a meeting involving the lord."')
            cont()
            print('Vole:')
            print('"What is it for?"')
            cont()
            print('Shrew:')
            print('"The Gowls… they are… conducting patrols of the woodlands north of here."')
            cont()
            print('Vole:')
            print('"And why does that matter!?"')
            cont()
            print('Vole:')
            print('"That may be unusual but it'"'"'s none of our concern."')
            cont()
            print('Vole:')
            print('"We are not their target."')
            cont()
            print('Dilecto:')
            print('"But someone could be."')
            cont()
            print('Dilecto:')
            print('"I approve and will be attending."')
            cont()
            print('Vole:')
            print('"But my lord the Gowls are no doubt looking for slavers, traitors and humans."')
            cont()
            print('Vole:')
            print('"Enemies who’d do us harm!"')
            cont()
            print('Vole:')
            print('"Surely they are justified."')
            cont()
            print('Dilecto:')
            print('"We shall discuss this."')
            cont()
            print('Dilecto:')
            print('"Though I would prefer there to be no violence near our town."')
            cont()
            print('Dilecto:')
            print('"Besides, not all humans are evil, we had human friends during the war."')
            cont()
            print('Dilecto:')
            print('"Times would have been far grimmer without them."')
            cont()
            print('Shrew:')
            print('"They were... friends with Agrimus?"')
            cont()
            print('Vole:')
            print('"Why does every conversation we have with you end up involving the Scion Dean."')
            cont()
            print('Dean')
            print('"I, um."')
            cont()
            print('Dean was embarrassed. He has always been very invested in this topic and often brought it up.')
            cont()
            print('Dilecto:')
            print('"Hahaha."')
            cont()
            print('Dilecto:')
            print('"It'"'"'s alright Dean."')
            cont()
            print('Dilecto:')
            print('"It has been so long since his time."')
            cont()
            print('Vole:')
            print('*Sighs* "About thirty years now."')
            cont()
            print('Dean')
            print('"Um?"')
            cont()
            print('Dean')
            print('"Do you think the next one will appear soon?"')
            cont()
            print('Vole:')
            print('"As great as that would be, the Woodlands are at peace."')
            cont()
            print('Vole:')
            print('"There is no need for a Scion."')
            cont()
            print('Dilecto:')
            print('"Despite the human killings that is."')
            cont()
            print('Vole:')
            print('"Sir Darrunt and his Gowls Knights have every right to deal with those vermin."')
            cont()
            print('Dilecto:')
            print('"Ralph!"')
            cont()
            print('Dilecto:')
            print('"That talk is too far, no one has any right to mass killing of a species!"')
            cont()
            print('Ralph:')
            print('"But my lord!"')
            cont()
            print('Dilecto:')
            print('"Enough!"')
            cont()
            print('Dilecto:')
            print('"We shall discuss this during the meeting."')
            cont()
            print('Dilecto:')
            print('"Hm!?"')
            cont()
            print('Dilecto notices an elderly mole emerging from a nearby room.')
            cont()
            print('Dilecto:')
            print('"Plumm could you spare a moment?"')
            cont()
            print('Plumm:')
            print('"Yes M’lord?"')
            cont()
            print('Dilecto:')
            print('"I need you to let the other officials know that there is to be a meeting tomorrow after noon."')
            cont()
            print('Dilecto:')
            print('"Dean. Be sure to invite Hazel, we will need to have a word with the Gowls."')
            cont()
            print('Plumm:')
            print('"The Gowls!?"')
            cont()
            print('Plumm:')
            print('"Why?"')
            cont()
            print('Ralph:')
            print('"They'"'"'re sending patrols around our town and into Oldwyrm woods."')
            cont()
            print('Plumm:')
            print('"Good heavens!"')
            cont()
            print('Plumm:')
            print('"Well, I’ll be off then."')
            cont()
            print('Ralph:')
            print('"I’ll help spread the word."')
            cont()
            print('Ralph:')
            print('"Off with you Dean."')
            cont()
            print('Dean')
            print('"Yes sir!"')
            cont()
            print('Plumm and Ralph head to the gardens, while Dean runs to the keep. Leaving Dilecto alone in the corridor. He moves to face the tapestry of an armoured mouse with a sword fighting a black demonic human-shaped figure wearing a tawny-furred cloak with blood red eyes. He looks at it with sombre eyes.')
            cont()
            print('Dilecto:')
            print('"Agrimus."')
            cont()
            print('Dilecto:')
            print('"Your successor as Scion."')
            cont()
            print('Dilecto:')
            print('"I wonder what kind of creature you have planned?"')
            cont()
            print('Dilecto:')
            print('"Whoever you pick I shall always trust your judgement."')
            cont()
            prologue = False
            chapter = '1'
        if (chapter == '1'):
            chapter1 = True
            if (switch[0] == True):
                location = '1'
                print('Chapter 1')
                print('Deep in the Oldwyrm woods north of the Fort a lone creature is wandering through the underbrush. It was a hedgehog. His quills sticking out of his jacket, hood and blue scarf. He had a travelling bag with various herbs and seeds. He was whispering into the air.')
                cont()
                print('Hedgehog:')
                print('"The rabbit seeks his burrow."')
                cont()
                print('There was a silence excluding the song of birds and insects of the setting summer. Then there were ripples in the air and a nearby boulder turned into a cottage and a nearby nettle bush turned into one of blackberries.')
                cont()
                print('In front of him a woman appeared. She towered above the hedgehog, his height not even making it to her waist. She had long dark hair that went down her shoulders and fair pale skin.')
                cont()
                print('Woman:')
                print('"Thay! It'"'"'s good to see you!"')
                cont()
                print('Thay:')
                print('"And you too Florace."')
                cont()
                print('Thay:')
                print('"Where’s young Alder?"')
                cont()
                print('Florace:')
                print('"He’s inside."')
                cont()
                print('Florace:')
                print('"He still has to clean the dishes."')
                cont()
                print('Florace:')
                print('"Alder!!"')
                cont()
                print('Florace:')
                print('"Thay'"'"'s" here!')
                cont()
                print('Inside the cottage, a boy with chestnut hair in a similarly light brown tunic that was worn, torn and noticeably small. He was cleaning plates in the kitchen. He was standing on a stool. He knew the hedgehog and enjoyed his company. He hurried to finish his task making sure each plate was spotless so he would not have to repeat the chore. After he had finished drying the last wooden spoon he was rushed to meet him. This Boy is Alder and this is his story.')
                cont()
                switch[0] = False
                print(location, chapter, part)
            elif (switch[1] == True and part == '2'):
                print('Thay and Florace are waiting for Alder in the clearing.')
                cont()
                print('Thay:')
                print('"Haha! How’ve you been Alder?"')
                cont()
                print('Alder:')
                print('"I’ve been great!"')
                cont()
                print('Thay:')
                print('"You’ve gotten bigger too."')
                cont()
                print('Thay:')
                print('"I remember when we were the same size."')
                cont()
                print('Alder:')
                print('"Yes it'"'"'s been a while since then."')
                cont()
                print('Thay smiled warmly at Alder, then turned to look at an elderly woman in one of the top windows of the cottage. She was a short and very wrinkled woman with a bent beak-like nose.')
                cont()
                print('Thay:')
                print('"Well."')
                cont()
                print('Thay:')
                print('"Better I'"'"'ll be meeting with the witch."')
                cont()
                print('Thay:')
                print('"I'"'"'ll chat with you both soon."')
                cont()
                print('Thay went to the cottage and seeing little reason to knock as he was clearly welcome, let himself in.')
                cont()
                switch[1] = False
            elif (switch[2] == True and part == '2'):
                print('As Alder talked with Florace, Thay came back out of the cottage.')
                cont()
                print('Thay:')
                print('"Thank you, Madame Kyla."')
                cont()
                print('Kyla:')
                print('"Yes yes. Come again."')
                cont()
                print('The old witch closed the door behind Thay who approached to speak to Alder and Florace.')
                cont()
                switch[2] = False
            elif (switch[3] == True and part == '3'):
                print('Florace:')
                print('"Alder!"')
                cont()
                print('Florace:')
                print('"I need you!"')
                cont()
                print('Alder looked back at Thay, disappointed that their conversation had to be cut short.')
                cont()
                print('Thay:')
                print('"Don’t worry about it lad."')
                cont()
                print('Thay:')
                print('"I’ll make sure you see me off."')
                cont()
                print('Alder:')
                print('*Sigh*')
                cont()
                print('Alder:')
                print('"Yes Florace?"')
                cont()
                print('Florace:')
                print('"We are out of meat."')
                cont()
                print('Florace:')
                print('"I need you to go to find an insect and bring it back for supper."')
                cont()
                print('Alder:')
                print('"Ok."')
                cont()
                print('Alder:')
                print('"Where do you want me to look?"')
                cont()
                print('Florace:')
                print('"Just outside the burrow."')
                cont()
                print('Florace:')
                print('"There should be a hunting knife on the table in the shed."')
                cont()
                print('Alder:')
                print('"Thank you."')
                cont()
                itemCount(weapons[2], 1)
                switch[3] = False
            free(location, chapter, part)
            #while(tutorial1 == True):
                #freeTutorial(location, chapter, part)
            if (tutorComp != False):
                free(location, chapter, part)

def loadGame():
    global location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, shill, inv, PKSwitch
    with open(PIK, "rb") as f:
        data = pickle.load(f)
        location = data[0]
        chapter = data[1]
        part = data[2]
        tutorial1 = data[3]
        tutorComp = data[4]
        chapter1 = data[5]
        switch = data[6]
        tutorialSwitch = data[7]
        shill = data[8]
        inv = data[9]
        PKSwitch = data[10]

def menu():
    global menu_active, chapter, part, chapter1, tutorComp, game_active, switch, tutorialSwitch, shill, inv, PKSwitch
    while (menu_active == True):
        print('Wild and Wyrd')
        print('n - New Game')
        print('l - Load')
        print('s - Settings')
        print('q - Quit')
        action = input('Enter Command: ')
        if (action == 'n'):
            game_active = True
            tutorial1 = True
            tutorComp = False
            chapter1 = False
            location = '1'
            chapter = '0'
            part = '1'
            #Story Switches
            switch = [True, False, False, False]
            tutorialSwitch = [True, True, True, True]
            game(chapter)
        elif (action == 'l'):
            game_active = True
            loadGame()
            game(chapter)
        elif (action == 'q'):
            menu_active = False
menu()
quit()
