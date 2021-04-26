import os
import pickle
import random
#Loop
menu_active = True
game_active = False
tutorial1 = True
chapter1 = False
#Story Switches
chapter = '0'
part = '1'
tutorComp = False
switch = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
tutorialSwitch = [True, True, True, True, True, True, True]
c2Switch = [True, True, True, True, True, True]
c3Switch = [True, True, True, True, True, True, True]
branchSwitch = ['0']
#Character Base Stats
class Alder:
    def __init__(self):
        self.pId = '1'
        self.name = 'Alder'
        self.species = 'Human'
        self.maxHealth = 60
        self.health = self.maxHealth
        self.maxStamina = 60
        self.stamina = self.maxStamina
        self.cLvl = 1
        self.cExp = 0
        self.cNext = 30
        self.skillPoints = 0
        self.baseAttack = 10
        self.baseDefence = 10
        self.baseAccuracy = 5
        self.baseSpeed = 10
        self.baseEvasion = 5
        self.weapons = ['sword', 'bow', 'dagger']
        self.head = armours[0]
        self.body = armours[1]
        self.legs = armours[3]
        self.weapon1 = weapons[0]
        self.weapon2 = weapons[0]
        self.aliment = 'None'
        self.cStatus = 'None'
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                          {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                          {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                          {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                          {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                          {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                          {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                          ]
        self.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Doubles Evasion for five turns.'},
                        {'spId':'2','name':'Master archer', 'cost':10, 'active':False, 'inEffect':0, 'unlocked':False, 'effect':'Grants a critical for the next arrow fired within the next four turns.'}
                        ]
    property
    def attack(self):
        attack = self.baseAttack
        if (self.weapon1['wpId'] != '0'):
            attack += self.weapon1['attack']
        else:
            attack += 0
        return attack
    property
    def attackRanged(self):
        attackRanged = self.baseAttack
        if (self.weapon2['wpId'] != '0' and self.weapon2['type'] == 'bow'):
            attackRanged += self.weapon2['attack']
        else:
            attackRanged += 0
        return attackRanged
    property
    def defence(self):
        defence = self.baseDefence
        if (self.head['type'] == 'hat'):
            defence += self.head['defence']
        if (self.body['type'] == 'shirt'):
            defence += self.body['defence']
        if (self.legs['type'] == 'trousers'):
            defence += self.legs['defence']
        if (self.weapon2['type'] == 'sheild'):
            defence += self.weapon2['defence']
        else:
            defence += 0
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        if (self.special[0]['active'] == True):
            evasion *= 2 
        return evasion
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nAccuracy: ', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2['name'],'\n'
              '\nSkill Points', self.skillPoints,'\n'
              )
#Enemy Units
class Cricket:
    def __init__(self):
        self.enId = '1'
        self.name = 'Cricket'
        self.maxHealth = 20
        self.health = self.maxHealth
        self.Exp = 10
        self.drop = [{'item' : food[4], 'quantity':2}]
        self.baseAttack = 0
        self.baseDefence = 8
        self.baseAccuracy = 90
        self.baseSpeed = 10
        self.baseEvasion = 25
        self.strat = 'Prey'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.desc = 'Big grasshoppers with long antenna. Can jump a fair distance.'
    def attack(self):
        attack = self.baseAttack
        return attack
    property
    def defence(self):
        defence = self.baseDefence
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        return evasion

class Hornet:
    def __init__(self):
        self.enId = '2'
        self.name = 'Hornet'
        self.maxHealth = 10
        self.health = self.maxHealth
        self.Exp = 10
        self.drop = [{'item':food[4], 'quantity':1}]
        self.baseAttack = 5
        self.baseDefence = 5
        self.baseAccuracy = 90
        self.baseSpeed = 40
        self.baseEvasion = 45
        self.strat = 'Attacker'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.desc = 'More hostile than usual this year. In the air they are annoying to hit but they are easy to kill.'
    def attack(self):
        attack = self.baseAttack
        return attack
    property
    def defence(self):
        defence = self.baseDefence
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        return evasion

class Dummy:
    def __init__(self):
        self.enId = '3'
        self.name = 'Dummy'
        self.maxHealth = 24
        self.health = self.maxHealth
        self.Exp = 0
        self.drop = []
        self.baseAttack = 0
        self.baseDefence = 150
        self.baseAccuracy = 0
        self.baseSpeed = 0
        self.baseEvasion = 0
        self.strat = 'Attacker'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.desc = 'Durable but falling apart.'
    property
    def attack(self):
        attack = self.baseAttack
        return attack
    property
    def defence(self):
        defence = self.baseDefence
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        return evasion
class Wall:
    def __init__(self):
        self.enId = '4'
        self.name = 'Wall'
        self.maxHealth = 200
        self.health = self.maxHealth
        self.type = 'Puzzle'
        self.Exp = 5
        self.drop = []
        self.baseAttack = 0
        self.baseDefence = 350
        self.baseAccuracy = 0
        self.baseSpeed = 0
        self.baseEvasion = 0
        self.strat = 'Attacker'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.desc = 'The wall between the living room and the shed.'
    property
    def attack(self):
        attack = self.baseAttack
        return attack
    property
    def defence(self):
        defence = self.baseDefence
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        return evasion
        
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
            'attack' : 0, 'weight' : 0, 'count' : 0, 'priority': 3},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'weapon', 'description' : 'Legendary sword of the Scion.',
            'attack' : 100, 'weight' : 5, 'count' : 0, 'priority': 3},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'weapon', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0, 'priority': 3},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : 'bow', 'description' : 'A large bow made for practise.',
            'attack' : 20, 'weight' : 2, 'count' : 0, 'priority': 4},
           {'wpId' : '1', 'name' : 'Wooden Sheild', 'type' : 'sheild', 'description' : 'A basic round wooden sheild.',
            'defence' : 20, 'weight' : 1, 'count' : 0, 'priority': 4}
           ]

armours = [{'armId' : '1', 'name' : 'None', 'type' : 'hat', 'description' : '',
          'defence' : 0, 'weight' : 0, 'count' : 0, 'priority': 5},
          {'armId' : '1', 'name' : 'Old Tunic', 'type' : 'shirt', 'description' : 'An old shirt with holes in it.',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 6},
          {'armId' : '2', 'name' : 'Travelling Cloak', 'type' : 'shirt', 'description' : 'A too large black cloak. Good for keeping ou of sight but heavy.',
          'defence' : 10, 'weight' : 10, 'count' : 0, 'priority': 6},
          {'armId' : '1', 'name' : 'Worn Trousers', 'type' : 'trousers', 'description' : 'An old pair of trousers long past their prime',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 7}
          ]
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : 'food',
          'recovers' : 2, 'count' : 0, 'priority': 1},
        {'itemId' : '4', 'name' : 'Mushroom', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : 'food',
          'recovers' : 10, 'count' : 0, 'priority': 1},
        {'itemId' : '6', 'name' : 'Brown Bread', 'type' : 'food',
          'recovers' : 50, 'count' : 0, 'priority': 1}
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0, 'priority': 2}
         ]
projec = [{'itemId' : '1', 'name' : 'Primitive Arrow', 'type' : 'projectile',
           'weapon' : 'bow', 'damage' : 10, 'count' : 0, 'priority': 8},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : 'toss',
           'weapon' : 'none', 'damage' : 0, 'count' : 0, 'priority': 9}
          ]
ingre = [{'ingId' : '1', 'name' : 'Bramble leaves', 'type' : 'ingredient', 'description' : 'The leaves of a blackberry bush',
          'count' : 0, 'priority': 10}
         ]
#Inventory
shill = 0
inv = []
PKSwitch = [True, True, True, True, True, True]

#Quests
mQuests = [{'questId':'1','client':'Florace','name':'Bug hunt', 'desc':'Collect two pieces of bug meat', 'reward' : '', 'rewardCount' : 0,
            'type':'collect', 'required':{'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : 'food'}, 'qnt' : 2,
            'accepted':False,'completed':False, 'submitted':False}
           ]
sQuests = [{'questId':'1','client':'Kyla','name':'Servants work', 'desc':['Clean fireplace:', 'Scrub caldron:', 'Grind bramble leaves in mortar:'], 'reward' : 'none', 'rewardCount' : 0,
            'type':'action', 'required':[False, False, False], 'qnt' : 1,
            'accepted':False,'completed':False, 'submitted':False},
           {'questId':'2','client':'Florace','name':'Provisions', 'desc':['Collect food x'], 'reward' : food[5], 'rewardCount' : 1,
            'type':'action', 'required':[False], 'qnt' : 1,
            'accepted':False,'completed':False, 'submitted':False},
           {'questId':'3','client':'Kyla','name':'Packing up', 'desc':['Take books from bookshelf:', 'Break down wall', 'Take pots from the shed:'], 'reward' : 'shillings', 'rewardCount' : 2,
            'type':'action', 'required':[False, False, False], 'qnt' : 1,
            'accepted':False,'completed':False, 'submitted':False}
           ]

#Location
locations = [{"locId" : "1", "name" : "Cottage Kitchen"},
             {"locId" : "2", "name" : "Cottage Living Room"},
             {"locId" : "3", "name" : "Outside Cottage"},
             {"locId" : "4", "name" : "Cottage Shed"},
             {"locId" : "5", "name" : "Alder's Room"},
             {"locId" : "6", "name" : "Forest Clearing"},
             {"locId" : "7", "name" : "???"}
             ]
location = '1'
#Interactable characters
actor = [{'actorId' : '1', 'name' : 'Florace', 'species' : 'human', 'title' : 'Witches apprentis'},
         {'actorId' : '2', 'name' : 'Kyla', 'species' : 'human', 'title' : 'Woodland witch'},
         {'actorId' : '3', 'name' : 'Thay', 'species' : 'hedgehog', 'title' : 'Wandering herbalist'},
         {'actorId' : '4', 'name' : 'Trissie', 'species' : 'squirrel', 'title' : 'Path finder'},
         {'actorId' : '5', 'name' : 'Jeb', 'species' : 'weasel', 'title' : 'Merchant'},
         {'actorId' : '6', 'name' : '???', 'species' : 'mouse', 'title' : '???'}
         ]
#Save and Load Content
PIK = 'demo.dat'
data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, shill, inv, PKSwitch]

#Set Class
alder = Alder()

def cont():
    con = input()
    if (con == 'skip'):
        return
#Level up character
def levelUP(p):
    #print(p.cNext, ' ', p.cExp)
    if(p.cExp >= p.cNext):
        while(p.cExp >= p.cNext and p.cLvl < 60):
            if(p.cLvl < 60):
                p.cLvl += 1
                p.maxHealth += 5
                p.maxStamina += 5
                p.health += 5
                p.stamina += 5
                p.baseAttack += 2
                p.baseDefence += 2
                p.baseAccuracy += 2
                p.baseSpeed += 2
                p.baseEvasion += 2
                p.skillPoints += 1
                print(p.name,' leveled up!')
                if(p.cLvl == 60):
                    print('Max Level')
                else:
                    if(p.cLvl < 5):
                        p.cNext = round(p.cNext*1.65)
                    elif(p.cLvl < 20):
                        p.cNext = round(p.cNext*1.55)
                    elif(p.cLvl < 30):
                        p.cNext = round(p.cNext*1.45)
                    elif(p.cLvl < 40):
                        p.cNext = round(p.cNext*1.35)
                    elif(p.cLvl < 50):
                        p.cNext = round(p.cNext*1.25)
                    elif(p.cLvl < 60):
                        p.cNext = round(p.cNext*1.15)
                    print(p.cNext)

class Null:
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'
#Boost Stats
def stBoost(p, sb):
    if(sb['stat'] == 'h' and sb['active']):
        p.maxHealth += sb['boost']
        p.health += sb['boost']
    elif(sb['stat'] == 's' and sb['active']):
        p.maxStamina += sb['boost']
        p.stamina += sb['boost']
    elif(sb['stat'] == 'at' and sb['active']):
        p.baseAttack += sb['boost']
    elif(sb['stat'] == 'df' and sb['active']):
        p.baseDefence += sb['boost']
    elif(sb['stat'] == 'ac' and sb['active']):
        p.baseAccuracy += sb['boost']
    elif(sb['stat'] == 'sp' and sb['active']):
        p.baseSpeed += sb['boost']
    elif(sb['stat'] == 'ev' and sb['active']):
        p.baseEvasion += sb['boost']
#Print Skill Tree
def skillTree(p):
    print('\nSkills')
    print('Skill Points: ', p.skillPoints)
    print('You can spend skill points on a stat boost or a character skill.')
    print('1: Stat Boosts')
    print('2: Special Skills')
    skill = input('Skill Type: ')
    if (skill == '1'):
        print('\nStat Boosts')
        print('Skill Points: ', p.skillPoints)
        count = 1
        temp = False
        for i in p.statBoost:
            if (i['No'] == '1' and i['active'] == False):
                print(count,': ', i['name'], ' + ', i['boost'])
                count += 1
            elif (i['No'] == '2' and i['active'] == False and temp == True):
                print(count,': ', i['name'], ' + ', i['boost'])
                count += 1
            elif (i['No'] == '3' and i['active'] == False and temp == True):
                print(count,': ', i['name'], ' + ', i['boost'])
                count += 1
            if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                temp = True
            else:
                temp = False
        sb = input('Boost: ')
        count = 1
        for i in p.statBoost:
            if (i['No'] == '1' and i['active'] == False):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            elif (i['No'] == '2' and i['active'] == False and temp == True):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            elif (i['No'] == '3' and i['active'] == False and temp == True):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                temp = True
            else:
                temp = False
    elif (skill == '2'):
        print('\nSpecial Skills')
        print('Skill Points: ', p.skillPoints)
        count = 1
        for i in p.special:
            if (i['unlocked'] == False):   
                print(count,': ', i['name'], ' - ', i['effect'])
                count += 1
        sa = input('Boost: ')
        count = 1
        for i in p.special:
            if (i['unlocked'] == False):
                if(sa == str(count)):
                    if (p.skillPoints > 0):
                        i['unlocked'] = True
                        print(i['name'], 'has been unlocked')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1

#Increment/Decrement Shillings
def shillings(m):
    global shill
    if (m < 0):
        m == 0
    shill += m
    if (shill < 0):
        shill = 0
    print('Shillings: ', shill)
#Recover health and stamina
def bed():
    alder.health = alder.maxHealth
    alder.stamina = alder.maxStamina
#Inventory order
def itemLister(e):
    return e['priority']
#Increment items
#Add a new item to the inventory if is is not already in there
def itemCount(item, amount):
    inInv = False
    for i in inv:
        if (item['type'] == 'weapon' and i['type'] == 'weapon'):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'sheild' and i['type'] == 'sheild'):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'bow' and i['type'] == 'bow'):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'armour' and i['type'] == 'armour'):
            if (i['armId'] == item['armId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'food' and i['type'] == 'food'):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'healing' and i['type'] == 'healing'):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'projectile' and i['type'] == 'projectile'):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'toss' and i['type'] == 'toss'):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == 'ingredient' and i['type'] == 'ingredient'):
            if (i['ingId'] == item['ingId']):
                i['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] = amount
        inv.append(item)
    inv.sort(key=itemLister, reverse=False)

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
        print('4: Main Weapon')
        print('5: Secondary Weapon')
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
                        if (tutorialSwitch[4] == True and i['wpId'] == '2'):
                            tutorialSwitch[4] = False
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '5'):
            count = 0
            for i in inv:
                if(i['type'] == 'bow' or i['type'] == 'sheild'):
                    count +=1
                    equipable.append(i)
                    if(i['type'] == 'bow'):
                        if (alder.weapon2['type'] == 'bow'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'sheild'):
                        if (alder.weapon2['type'] == 'sheild'):
                            print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.weapon2['defence'])
                        else:
                            print(count, ': ', i['name'], '- Defence: +', i['defence'])                            
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(alder.weapon2['wpId'] != '0'):
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
#Quest Rewards
def qComp(q):
    global shill
    print(q['name'], 'Completed!')
    if(q['reward'] != 'none' and q['rewardCount'] > 0):
        if q['reward'] == 'shillings':
            shill += q['rewardCount']
        elif q['reward'] == 0:
            shill += q['rewardCount']
        else:
            itemCount(q['reward'], q['rewardCount'])
#The user should buy items from shop
def shop(seller):
    shopping = True
    while(shopping == True):
        if(seller == 'Jeb'):
            print('\nFeel free to brouse my wares.')
            print('1: Bandage ', 'Remaining: ', '5 Cost: 5')
            print('2: Dried Fruit' , 'Remaining: ', '5 Cost: 1')
            print('3: Hazel Nuts ', 'Remaining: ', '5 Cost: 1')
            print('e - Exit')
            p = input('Purchise: ')
            if (p == '1'):
                cost = 5
                if (shill >= cost):
                    print('\nYou bought a Bandage')
                    shillings(-cost)
                    itemCount(items[0], 1)
                else:
                    print('\nYou don'"'"'t have enough shillings')
            elif (p == '2'):
                cost = 1
                if (shill >= cost):
                    print('\nYou bought a Dried Fruit')
                    shillings(-cost)
                    itemCount(food[1], 1)
                else:
                    print('\nYou don'"'"'t have enough shillings')
            elif (p == '3'):
                cost = 1
                if (shill >= cost):
                    print('\nYou bought a Hazelnut')
                    shillings(-cost)
                    itemCount(food[2], 1)
                else:
                    print('\nYou don'"'"'t have enough shillings')
            elif (p == 'e'):
                print()
                shopping = False
            
#Win battle
def win(e):
    ex = 0
    rewards = []
    count = 0
    print('\n')
    for i in e:
        ex += i.Exp
        count += 1
    alder.cExp += ex
    print('Alder gained ', ex, ' experience.')
    levelUP(alder)
    for i in e:
        if (len(i.drop) > 0):
            print(i.name,' dropped ', i.drop[0]['item']['name'], ' x', i.drop[0]['quantity'])
            itemCount(i.drop[0]['item'], i.drop[0]['quantity'])
    cont()
#If character dies
def death():
    global game_active
    loss = shill / 10
    if (round(loss) <= 0):
        loss = 1
    shillings(-loss)
    print('\nAlder was slain.')
    cont()
    game_active = False
#Hunder
def hunger(inCombat):
    if(alder.stamina <= 0):
        alder.health -= 1
        if (alder.health <= 0):
            if(inCombat != True):
                death()
        else:
            print('You need to eat!')    
    if(alder.stamina < 0):
        alder.stamina = 0
#Enemy attack
def enemyAttack(e, p, b):
    if (e.attack() != 0):
        target = e.accuracy() + 100 - p.evasion()
        hit = random.randrange(0,100)
        critical = random.randrange(0,100)
        if (hit < target):
            impact = random.randrange(e.attack() - 5, e.attack() + 5)
            if (critical >= 90):
                impact += 10
            impact = round(impact * (100/(100 + p.defence())))
            if (p.cStatus == 'Blocking'):
                impact = round(impact/10)
            if (impact <= 0):
                impact = 1
            p.health -= impact
            print('\n',e.name,' attacked!')
            if(critical >= 90):
                print('Critical Hit!')
            print(p.name, ' took ', impact, ' damage!')
            return b
        else:
            print('\n',e.name,' Missed')
    else:
        print('\n',e.name, 'did not attack!')

#Attack Enemy
def attack(p, e):
    target = p.accuracy() + 100 - e.evasion()
    hit = random.randrange(0,100)
    critical = random.randrange(0,100)
    alder.stamina -= 5
    if (p.ammo['loaded'] == True):
        if (hit < target):
            impact = random.randrange(p.attackRanged() - 3, p.attackRanged() + 3)
            impact += p.ammo['damage']
            if (critical >= 90):
                impact += 10
            impact = round(impact * (100/(100 + e.defence())))
            if (impact <= 0):
                impact = 1
            e.health -= impact
            print('\n',p.name,' fired a', p.ammo['name'], '!')
            if(critical >= 90):
                print('Critical Hit!')
            print(e.name, ' took ', impact, ' damage!')
            p.ammo['loaded'] = False
        else:
            print('\n',p.name,' Missed')
    else:
        if (hit < target):
            impact = random.randrange(p.attack() - 5, p.attack() + 5)
            if(p.weapon1['wpId'] != '0'):
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + e.defence())))
                if (impact <= 0):
                    impact = 1
                e.health -= impact
                print('\n',p.name,' attacked!')
                if(critical >= 90):
                    print('Critical Hit!')
            else:
                impact = 0
                print('\nBut',p.name, ' was unarmed')
            if(critical >= 90):
                print('Critical Hit!')
            print(e.name, ' took ', impact, ' damage!')
        else:
            print('\n',p.name,' Missed')
    if(e.health <= 0):
        print(e.name, ' defeated.')
    if (p.ammo['loaded'] == False):
        p.ammo['name'] = ''
        p.ammo['damage'] = 0

#Block incoming attack
def block(barrier, incoming):
    print(barrier, temp)
    return incoming

#Check if special effect are still active and deactivate them it they are not.
def inEffect():
    for i in alder.special:
        if(i['active'] == True):
            i['inEffect'] -= 1
            if (i['inEffect'] <= 0):
                i['active'] = False
                print(alder.name,"'s ", i['name'], ' has worn off.')

def special(p):
    print('\nSpecial Ability')
    count = 0
    for i in p.special:
        if (i['unlocked'] == True):
            print(i['spId'], ') ',i['name'], ' - ', i['cost'], ' stamina')
            count += 1
    if (count == 0):
        print('None')
    sp = input('Use: ')
    for i in p.special:
        if (i['unlocked'] == True):
            if (sp == i['spId']):
               i['active'] = True
               if (i['spId'] == '1'):
                   p.stamina -= i['cost']
                   i['inEffect'] = 6
               elif (i['spId'] == '2'):
                   p.stamina -= i['cost']
                   i['inEffect'] = 5
               print('\n', p.name, ' uses ', i['name'],'.')

#Use Item
def item(p, e):
    use = []
    using = True
    y = ''
    while(using == True):
        print('\nBag Items')
        count = 1
        if (y == '' or y == 'healing' or y == 'Healing' or
            y == 'health' or y == 'Health'):
            print('Healing')
            for i in inv:
                if(i['type'] == 'healing'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'food' or y == 'Food' or
            y == 'consumables' or y == 'Consumables'):
            print('Food')
            for i in inv:
                if(i['type'] == 'food'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'projectiles' or y == 'Projectiles'):
            print('Projectiles')
            for i in inv:
                if(i['type'] == 'projectile' or i['type'] == 'toss'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        print('e - exit')
        if(count != 0):
            count = 1
            u = input('use item: ')
            if (u == '' or u == 'food' or u == 'Food' or u == 'consumables' or u == 'Consumables' or u == 'healing' or u == 'Healing' or
                u == 'health' or u == 'Health' or u == 'projectiles' or u == 'Projectiles' or u == 'e'):
                y = u
            for i in use:
                if (u == str(count)):
                    if (i['type'] == 'healing'):
                        p.health += i['heals']
                        print(p.name, ' recoved ', i['heals'], ' health')
                        if (p.health > p.maxHealth):
                            p.health = p.maxHealth
                            alder.cStatus = 'Using'
                        using = False
                    elif (i['type'] == 'food'):
                        p.stamina += i['recovers']
                        print(p.name, ' recoved ', i['recovers'], ' stamina')
                        if (p.stamina > p.maxStamina):
                            p.stamina = p.maxStamina
                            alder.cStatus = 'Using'
                        using = False
                    elif (i['type'] == 'projectile'):
                        if (i['weapon'] == 'bow'):
                            if(p.weapon2['type'] == 'bow'):
                                print('\nArrow loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                alder.cStatus = 'Using'
                                using = False
                            else:
                                print('Bow required!')
                                using = False
                    elif (i['type'] == 'toss'):
                        count = 1
                        for j in e:
                            print(count, ': ', j.name)
                            count += 1
                        count = 1
                        target = input('Throw at: ')
                        for j in e:
                            if (target == str(count)):
                                print('\n',p.name,'threw ', i['name'])
                                j.aliment = 'Caught' 
                                alder.cStatus = 'Using'
                                using = False
                            count += 1
                    i['count'] -= 1
                    if(i['count'] <= 0):
                        inv.remove(i)
                elif u == 'e':
                    using = False
                count +=1
            use.clear()

#Combat interface
def battle(e):
    os.system('clear')
    global alder
    enemys = []
    for i in e:
        if i.enId != '0':
            enemys.append(i)
    fighting = True
    winner = False
    count = 1
    bck = 0
    while(fighting == True):
        hunger(fighting)
        #Win condition
        if (enemys[0].health <= 0):
            j = 0
            for i in enemys:
                if (i.health <= 0):
                    j += 1
            if (j == len(enemys)):
                winner = True
        #Death Condition
        if(alder.health <= 0):
            fighting = False
            death()
        #Win
        elif(winner == True):
            for i in alder.special:
                i['active'] = False
                i['inEffect'] = 0
            fighting = False
            win(enemys)
        else:
            inEffect()
            for i in enemys:
                if(i.speed() > alder.speed() and count == 1 and i.health > 0):
                    enemyAttack(i, alder, bck)
            while(alder.cStatus == 'None'):
                if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False):
                    if(count == 1):
                        print('\nUse the command "3" or "appraise" to examine enemy health and information.')
                    elif(count == 2):
                        print('\nTo reduce damage from a incoming attack use command "2" or "block"')
                    elif(count == 3):
                        print('\nTo deal damage to the opponent use command "1" or "attack".')
                elif (c2Switch[0] == False and c2Switch[1] == True):
                    print('\nTo use a ranged weapon like the bow select a supported projectile from items, then on the next turn attack to fire.')
                print('\n',alder.name)
                if (alder.ammo['loaded'] == True):
                    print('Ranged weapon set')
                print("Health: ", alder.health, '/', alder.maxHealth, "| Stamina: ", alder.stamina, '/', alder.maxStamina)
                print("1) Attack     3) Appraise     5) Item")
                print("2) Block      4) Special      6) Flee")
                i = input('Action: ')
                if (i == '1' or i == 'attack' or i == 'Attack'):
                    print('\nEnemies')
                    j = 1
                    for i in enemys:
                        if (i.health > 0):
                            print(j, ': ', i.name)
                            j += 1
                    target = input('Attack: ')
                    j = 1
                    for i in enemys:
                        if (i.health > 0):
                            if (target == str(j)):
                                alder.cStatus = 'Attacking'
                                attack(alder, i)
                            j += 1
                elif (i == '2' or i == 'block' or i == 'Block'):
                    alder.cStatus = 'Blocking'
                    bck = alder.defence()
                elif (i == '3' or i == 'appraise' or i == 'Appraise'):
                    for i in enemys:
                        print('\n',i.name, 'Health:', i.health,'/',i.maxHealth)
                        print(i.desc)
                elif (i == '4' or i == 'special' or i == 'Special'):
                    alder.cStatus = 'Specializing'
                    special(alder)
                elif (i == '5' or i == 'item' or i == 'Item'):
                    item(alder, enemys)
                elif (i == '6' or i == 'flee' or i == 'Flee'):
                    i = input('Are you sure you want to run?(y/n)')
                    confirm = yn(i)
                    if (confirm == True): 
                        alder.cStatus = 'Escaping'
                        running = True
                        for i in enemys:
                            if (i.speed() > alder.speed()):
                                print('\nEscape Failed!')
                                running = False
                            elif (i.enId == '3'):
                                print('\nCannot run!')
                                running = False
                        if (running == True):
                                fighting = False
            for i in enemys:
                if(i.health > 0):
                    if(i.strat == 'Attacker'):
                        if (i.aliment != 'Caught'):
                            enemyAttack(i, alder, bck)
                        else:
                            escape = random.randrange(0, 100)
                            if (i.type == 'bug'):
                                if (escape >= 95):
                                    print(i.name, 'escaped the net!')
                                    i.aliment = 'None'
                                else:
                                    print('The', i.name,' is tangled in a net!')
                            elif (i.type == 'soldier'):
                                if (escape >= 30):
                                    print(i.name, 'escaped the net!')
                                else:
                                    print('The', i.name,' is tangled in a net!')
                        i.cStatus = 'Attacking'
                    elif(i.strat == 'Prey'):
                        if(i.health < i.maxHealth):
                            print(i.name, ' fled!')
                            i.cStatus = 'Escaping'
            for i in reversed(enemys):
                if(i.health > 0):
                    if (i.cStatus == 'Escaping'):
                        enemys.remove(i)
                        if (len(enemys) == 0):
                            fighting = False
                else:
                    i.cStatus = 'None'
            count += 1
            alder.cStatus = 'None'
#Yes or no answers
def yn(yesNo):
    while(yesNo != 'y' or yesNo != 'Y' or yesNo != 'yes' or yesNo != 'Yes' or
          yesNo != 'n' or yesNo != 'N' or yesNo != 'no' or yesNo != 'No'):
        if (yesNo == 'y' or yesNo == 'Y' or yesNo == 'yes' or yesNo == 'Yes'):
            return True
        elif (yesNo == 'n' or yesNo == 'N' or yesNo == 'no' or yesNo == 'No'):
            return False
        else:
            yesNo = input('"yes" or "no" responses only!: ')
#Examine background object
def examine(location):
    global game_active, chapter, part
    examining = True
    while (examining == True):
        print('\nExamine')
        print('Type "e" to end examining')
        for i in locations:
            if (location == i['locId']):
                print(i['name'])
        if (location == '1'):
            print("The cottage kitchen contained various 'pots' hanging on the wall. It had a 'stove' where a 'cauldron' was dangled on a chain. In addition, a smaller room served as the 'larder'. There was also a 'cupboard' and two 'tables', one of which had a wooden 'bowl' on it. Alder had been washing dishes in a 'basin' on the other table next to the 'window'.")
            e = input('Examine: ')
            if (e == 'cauldron' or e == 'Cauldron'):
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][1] == False):
                    print('Alder got a wet cloth and started scrubbing the cauldron. Florace looked into the living room at Kyla and then went over to help him.')
                    cont()
                    print('Florace:')
                    print('"Shh."')
                    sQuests[0]['required'][1] = True
                    examining = False
                else:
                    print("It was a small metal cauldron above the stove suspended by a chain. It was empty right now.")
                cont()
            elif (e == 'pots' or e == 'Pots'):
                print('Various pots and pans were hung on hooks in the wall.')
                cont()
            elif (e == 'cupboard' or e == 'Cupboard'):
                print('The cupboard was full of plates, bowls and other kitchen and dining utensils.')
                cont()
            elif (e == 'bowl' or e == 'Bowl'):
                if (PKSwitch[0] == True):
                    print('A large wooden bowl. It'"'"'s got hazelnuts in it.')
                    pickup = input('Do you want to pick up the hazelnuts.(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 Hazelnut(s) obtained')
                        itemCount(food[2], 5)
                        PKSwitch[0] = False
                        cont()
                else:
                    print('A large wooden bowl. It'"'"'s empty.')
                    cont()
            elif (e == 'basin' or e == 'Basin'):
                print('The basin Alder was washing in was full of water and bits of leftovers that Alder scraped off. Clean plates were next to it.')
                cont()
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(tutorialSwitch[2] == True):
                    print('Florace and Thay were talking on the other side of the window.')
                    cont()
                    print('Alder:')
                    print('"I'"'"'m coming out"')
                    chapter = '1'
                    tutorialSwitch[0] = False
                else:
                    print('The clearing is out front.')
                cont()
            elif (e == 'stove' or e == 'Stove'):
                print('The unlit fireplace was full of dry branches. The fire would heat the metal plates of the stove to cook meat.')
                cont()
            elif (e == 'table' or e == 'Table' or e == 'tables' or e == 'Tables'):
                print('A rectangular wooden table stood in the centre of the room while a thinner one stood by the window.')
                cont()
            elif (e == 'hornets' or e == 'Hornets'):
                if (tutorialSwitch[5] == False and c2Switch[0] == True):
                    print('The hornets Alder slew were hung up on hooks. To be cooked tonight')
                    cont()
            elif (e == 'larder' or e == 'Larder'):
                if (sQuests[1]['accepted'] == True):
                    print('The was only a single loaf of bread in the larder. It will have to do.')
                    sQuests[1]['completed'] = True
                elif (sQuests[1]['completed'] == True):
                    print('The larder was empty.')
                else:
                    print('A small cool room of shelves and hooks to store food, mostly empty except for a loaf of bread. Kyla’s familiar Tawie was out resupplying. Alder was not looking forward to her return.')
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '2'):
            print("The living room was a homely place that was accessible by both the front and back 'door' and lit by the 'windows'. It had two 'chairs' and a 'table' in front of a 'fireplace' as well as a single 'bookshelf' with three shelves full of books.")
            e = input('Examine: ')
            if (e == 'bookshelf' or e == 'Bookshelf'):
                if (sQuests[2]['accepted'] == True and sQuests[2]['required'][0] == False):
                    print('Alder carried each of the books and put them in a neat pile near the stairs.')
                    cont()
                    sQuests[2]['required'][0] = True
                elif(sQuests[2]['required'][0] == True):
                    print('The bookshelf was empty.')
                else:
                    print('The books in the living room bookshelf included:')
                    cont()
                    print('\tMagic the basics')
                    print('\tMagical things of history')
                    print('\tPotions')
                    print('\tDevelopers Note - Kyla'"'"'s cottage')
                    print('\tDevelopers Note - Wild and Wyrd Demo')
                    cont()
                    print('Read books option coming soon!')
                    if(c3Switch[0] == False):
                        read = input('Read Magical things of history (y/n)?')
                        confirm = yn(read)
                        if (confirm == True):
                            if(c3Switch[1] == True):
                                print('Alder:')
                                print('"A "Cohuleen Druith" hat."')
                                cont()
                                print('Alder:')
                                print('"The "Ring of Eluned"."')
                                cont()
                                print('Alder:')
                                print('"The "Gae Bulg" spear."')
                                cont()
                                print('Alder:')
                                print('"Found it!"')
                                cont()
                                print('Alder:')
                                print('"It’s called "Lief", "The sword of the seasons"."')
                                cont()
                                print('Kyla:')
                                print('"As I thought."')
                                cont()
                                print('Kyla:')
                                print('"But there is only one way to confirm this."')
                                cont()
                                print('Kyla unsheathes that sword and holds it in her hand. The blade darkened and bent and it was not long before it dropped off leaving only the handle.')
                                cont()
                                print('Kyla:')
                                print('"Boy you can have the sword back now, make sure you hold it by the grip."')
                                cont()
                                print('Alder says nothing as he picks up the sword. As he does, a new blade starts to grow from the rain-guard until it was back to its original glory.')
                                cont()
                                alder.weapon1 = weapons[1]
                                print(alder.weapon1['name'],'equiped!')
                                cont()
                                print('Florace:')
                                print('"What did you do?"')
                                cont()
                                print('Kyla:')
                                print('"The sword only sprouts for the Scion."')
                                cont()
                                print('Kyla:')
                                print('"In order words."')
                                cont()
                                print('Kyla:')
                                print('"You."')
                                cont()
                                dialog = [False, False, False]
                                while(dialog[0] == False or dialog[1] == False or dialog[2] == False):
                                    print('1: "What is a Scion?"')
                                    print('2: "Does this have anything to do with the mouse I saw in my dream?"')
                                    print('3: "What with the sword blade?"')
                                    c = input('Alder: ')
                                    if (c == '1'):
                                        print('Kyla:')
                                        print('"What is…!?"')
                                        cont()
                                        print('Kyla:')
                                        print('"How do you not know what the Scion is!?"')
                                        cont()
                                        print('Florace:')
                                        print('"I thought it was more important that he knew herbs and how to read and write than history."')
                                        cont()
                                        print('Kyla:')
                                        print('*Sigh*')
                                        cont()
                                        print('Kyla:')
                                        print('"The Scion is the great hero of Avalon."')
                                        cont()
                                        print('Kyla:')
                                        print('"They have an ability to pass on their knowledge and natural abilites after death."')
                                        cont()
                                        print('Kyla:')
                                        print('"One previous Scion has killed a dragon while another saved countless innocents from slavers."')
                                        cont()
                                        print('Kyla:')
                                        print('"And I knew one who put kings themselves in their rightful place."')
                                        cont()
                                        print('Kyla:')
                                        print('"But I digress."')
                                        cont()
                                        dialog[0] = True
                                    elif (c == '2'):
                                        print('Kyla:')
                                        print('"That mouse was no doubt Agrimus the Scion before you."')
                                        cont()
                                        print('Kyla:')
                                        print('"He appeared to you to pass on his title and sword."')
                                        cont()
                                        print('Kyla:')
                                        print('"I am shocked he chose you though."')
                                        cont()
                                        print('Kyla:')
                                        print('"He was the hero of the war against the humans of Glorion."')
                                        cont()
                                        print('Kyla:')
                                        print('"And out of countless potentials he goes for my servant."')
                                        cont()
                                        dialog[1] = True
                                    elif (c == '3'):
                                        print('Kyla:')
                                        print('"It’s in the book."')
                                        cont()
                                        print('Kyla:')
                                        print('"The sword blade is like a plant and the grip its roots."')
                                        cont()
                                        print('Kyla:')
                                        print('"It grows when the Scion holds it but when someone else holds the blade dies."')
                                        cont()
                                        dialog[2] = True
                                
                                print('???:')
                                print('"The rabbit seeks his burrow!"')
                                cont()
                                print('Alder, Florace and Kyla:')
                                print('"...?"')
                                cont()
                                print('Florace:')
                                print('"Who is that?"')
                                cont()
                                examining = False
                                c3Switch[1] = False
                            else:
                                print('\nLeif - The sword of seasons.')
                                print('\nAn illustration of a double edged sword and green and silver scabbard and decorations with thorny stem engraved around the grip, a leaf shaped rain-guard and a tear-shaped pommel.')
                                print('\tThe sword whos only master is the Scion. It blade is not metal from the earth but a leaf from a rare Wyrd tree. When weilded by any other it'"'"'s blade will wilt but in the Scions it will regrow.')
                                cont()
            elif (e == 'fireplace' or e == 'Fireplace'):
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][0] == False):
                    print('Alder got to work cleaning the fireplace using a brush and cloth. In the end his arms were completely black.')
                    cont()
                    print('Kyla:')
                    print('"Could you throw that ash outside."')
                    cont()
                    print('Kyla:')
                    print('"If it gets on the floor you'"'"'re cleaning it up."')
                    cont()
                    sQuests[0]['required'][0] = True
                    examining = False
                elif (sQuests[0]['required'][0] == False):
                    print('The fireplace was unlit. It was used last night and still had ash and soot in it.')
                    cont()
                    print('Alder:')
                    print('"I’ll clean it up later."')
                    cont()
                else:
                    print('The fireplace was unlit.')
                    cont()
            elif (e == 'chairs' or e == 'Chairs'):
                print('There were two wooden armchairs both with partridge feather cushions.')
                cont()
            elif (e == 'table' or e == 'Table'):
                if (c3Switch[4] == False and c3Switch[5] == True):
                    print('Jeb laid out his wares on the table.')
                    cont()
                    shop('Jeb')
                    if ((sQuests[1]['accepted'] == True and sQuests[1]['submitted'] != True) or (sQuests[2]['accepted'] == True and sQuests[2]['submitted'] != True)):
                            ab = input('Abandon quests?(y/n)')
                            confirm = yn(ab)
                            if (confirm == True):
                                if (sQuests[1]['accepted'] == True and sQuests[1]['submitted'] != True):
                                    sQuests[1]['accepted'] = False
                                    print(sQuests[1]['name'],' abandoned!')
                                if (sQuests[2]['accepted'] == True and sQuests[2]['submitted'] != True):
                                    sQuests[2]['accepted'] = False
                                    print(sQuests[1]['name'],' abandoned!')
                                switch[14] = True
                                part = '4'
                    else:
                        switch[14] = True
                        part = '4'
                    examining = False
                else:
                    print("A single round wooden table sat at a safe distance from the fire but close enough to feel its warmth.")
                    cont()
            elif (e == 'door' or e == 'Door'):
                print('There was a door for either side of the house, both leading outside.')
                cont()
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(c3Switch[1] == False and c3Switch[2] == True):
                    switch[11] = True
                    part = '2'
                    examining = False
                elif(c3Switch[2] == False and c3Switch[3] == True):
                    switch[12] = True
                    part = '3'
                    examining = False
                else:
                    print('There were four windows showing the clearing on either side of the cottage.')
                    cont()
            elif (e == 'wall' or e == 'Wall'):
                if (sQuests[2]['accepted'] == True and sQuests[2]['required'][1] == False):
                    print('Alder alined himself with where the tools hung in the shed on the over side of the wall.')
                    cont()
                    battle([Wall(), Null(), Null()])
                    if (alder.health > 0):
                        print('The swords power was incredable. With a bit of force it easily pierced the clay walls and Alder tore it down through the gap he battered into existance, with tools on the other side now fallen amoungst rubble. Kyla apparently found this ammusing. But a hole was made and Alder enter the shed.')
                        cont()
                        sQuests[2]['required'][1] = True
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '3'):
            print("The burrow was isolated from society within a deep wood. The 'sky' was clear blue and the late summer 'plant' life including 'mushrooms' were abundant amongst the 'trees' and 'rocks' of the forest. Part of the stone disguising the 'cottage', was actually an old 'shed' with a slanted roof, nearby was a large 'bramble' bush.")
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                print('It was a bright, clear blue.')
                cont()
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                print('There was a variety of late-summer mushrooms around the area.')
                cont()
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                print('Various weeds, wildflowers, moss and a bramble bush with ripe blackberries.')
                cont()
            elif (e == 'trees' or e == 'Trees'):
                print('Various trees made up the woodland, the most frequent were birch, rowen and holly.')
                cont()
            elif (e == 'rocks' or e == 'Rocks'):
                print('There were a few boulders in the area. None were as large as the cottage.')
                cont()
            elif (e == 'cottage' or e == 'Cottage'):
                print('The cottage was changed to look like a large boulder but in reality it had two floors and was made from white clay bricks. It was well protected against the elements and cosy, but Alder felt constricted.')
                cont()
            elif (e == 'shed' or e == 'Shed'):
                print('The shed had a single door with a window in it. From the outside it looked like part of the larger stone but in actuality it was made entirely of splintered wooden planks.')
                cont()
            elif (e == 'bush' or e == 'Bush' or e == 'blackberry' or e == 'Blackberry' or e == 'blackberry bush' or e == 'Blackberry Bush'  or e == 'bramble' or e == 'Bramble'):
                if (PKSwitch[2] == True):
                    print('The bramble bush was a convenient source of fresh fruit at this time of year. It still had a few blackberries on it.')
                else:
                    print('It still had a few blackberries on it but they were out of reach and Alder did not want to get pricked by its thorns.')
                if (PKSwitch[2] == True):
                    pickup = input('Do you want to pick up the blackberries.(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 blackberries(s) obtained')
                        itemCount(food[0], 5)
                        PKSwitch[2] = False
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][2] == False):
                    print('Alder picked some bramble leaves trying to avoid the thorns. He wondered what potion Kyla was going to use them for.')
                    count = 0
                    for i in inv:
                        if (i['type'] == 'ingredient'):
                                if (i['ingId'] == '1'):
                                    count += 1
                    if (count == 0):
                        itemCount(ingre[0], 1)
                    else:
                        print ('Alder already had some.')
                    examining = False
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '4'):
            if (c2Switch[2] == True):
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'. At the other end from the entrance was a 'table' used for crafts. Above it a 'bow' and 'quiver' full of 'arrows' were hung and an old 'sack' was slumped at its side.")
            else:
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'.")
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('A single window on the left side of the room.')
                cont()
                print('Outside, the woods could be seen.')
                cont()
            elif (e == 'tools' or e == 'Tools' or e == 'axe' or e == 'Axe' or e == 'saw' or e == 'Saw' or
                  e == 'pick' or e == 'Pick' or e == 'shovel' or e == 'Shovel' or e == 'sickle' or e == 'Sickle' or
                  e == 'rod' or e == 'Rod' or e == 'fishing' or e == 'Fishing' or e == 'fishing rod' or e == 'Fishing rod'):
                print('Various tools were hung on the wall and sat on the shelves.')
                cont()
                print('They included an axe, saw, pick, shovel, sickle and fishing rod.')
                cont()
            elif (e == 'pots' or e == 'Pots'):
                if (sQuests[2]['accepted'] == True and sQuests[2]['required'][2] == False):
                    print('Alder carried each pot one by one to the living room there weight depended on how full they were and what was in it. The heaviest was a pot full of ground up plant matter and weighed as much as a cannon ball. Alder brought the last one in with a sweat.')
                    cont()
                    location = '2'
                    sQuests[2]['required'][2] = True
                    examining = False
                elif(sQuests[2]['required'][2] == True):
                    print('There weren'"'"'t any pots left.')
                else:
                    print('The pots contained ingredients for potions. They were left in the shed to save space indoors. One of the pots was full of eyeballs.')
                    cont()
            elif (e == 'crates' or e == 'Crates' or e == 'boxes' or e == 'Boxes'):
                print('Kyla had put spare magical tools in boxes to keep them from breaking.')
                cont()
            elif (e == 'table' or e == 'Table'):
                if (PKSwitch[1] == True):
                    print("On the table was an unlit 'candle', a 'mortar' and 'pestle' and a hunting 'knife'.")
                    if (tutorialSwitch[3] == False):
                        pickup = input('Do you want to pick up the hunting knife.(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nHunting Knife obtained')
                            itemCount(weapons[2], 1)
                            PKSwitch[1] = False
                            examining = False
                            cont()
                else:
                    print("On the table was an unlit 'candle' and a 'mortar' and 'pestle'.")
                    cont()
            elif (e == 'candle' or e == 'Candle'):
                print('The candle was placed in a candlestick. It was unlit.')
                cont()
            elif (e == 'mortar' or e == 'Mortar' or e == 'pestle' or e == 'Pestle'):
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][2] == False):
                    for i in inv:
                        if (i['type'] == 'ingredient' and i['ingId'] == '1'):
                            print('Alder grinded the leaves with the pestle until it was powder. He then put it in a nearby pot containing the remnants of the same powder.')
                            cont()
                            sQuests[0]['required'][2] = True
                            examining = False
                else:
                    print('A mortar and pestle were on the table.')
                    cont()
                    print('Florace recently used them to grind ingredients for potions.')
                    cont()
            elif (e == 'knife' or e == 'Knife'):
                print('The knife was designed for hunting but it looks like someone has been using it to cut ingredients.')
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
            elif (c2Switch[2] == True):
                if (e == 'sack' or e == 'Sack'):
                    print('A cheaply made old burlap sack intended for foraging but it  nearly is on the verge of falling apart.')
                    if (PKSwitch[5] == True):
                        print('There'"'"'s a bandage inside.')
                        cont()
                        pickup = input('Do you want to pick up the bangage.(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nBandage obtained')
                            itemCount(items[0], 1)
                            PKSwitch[5] = False
                    cont()
                elif (e == 'bow' or e == 'Bow' or e == 'quiver' or e == 'Quiver' or e == 'arrows' or e == 'Arrows'):
                    print('A practise bow and quiver full of arrows. They were intended as a gift for Florace but she was never interested in archery, so Alder got them instead.')
                    cont()
        elif (location == '5'):
            print("Sunlight entered the room through the solitary curtainless 'window' of Alder's small bedroom which contained only a makeshift 'bed'.")
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('The window lacked curtains and was small. Alder could see the sunlight breaching the branches near of the Oldwyrm Woods near the edge of the clearing.')
                cont()
            elif (e == 'bed' or e == 'Bed'):
                print('It was cheaply made from dry wood and partridge feathers. It was powdered with herbs to stop it smelling. Alder made it with the help of Thay.')
                if (PKSwitch[4] == True):
                    pickup = input("Among the feathers were Alder's savings. Pick them up?(y/n)")
                    confirm = yn(pickup)
                    if (confirm == True):
                        coins = random.randrange(+2,+3)
                        print('\n', coins,' shillings obtained!')
                        shillings(coins)
                        PKSwitch[4] = False
                        cont()
                if ((tutorialSwitch[5] == False and tutorialSwitch[6] == True)  or (c2Switch[1] == False and c2Switch[2] == True)):
                    sleep = input('Would you like to rest?(y/n)')
                    confirm = yn(sleep)
                    if (confirm == True):
                        print('Alder got into his makeshift bed and drifted to sleep for the night.')
                        if (tutorialSwitch[5] == False and tutorialSwitch[6] == True):
                            if(sQuests[0]['accepted'] == True and sQuests[0]['submitted'] == False):
                                ab = input('Abandon quests?(y/n)')
                                confirm = yn(ab)
                                if (confirm == True):
                                    sQuests[0]['accepted'] = False
                                    print(sQuests[0]['name'],' abandoned!')
                                    tutorialSwitch[6] = False
                                    part = '1'
                                    switch[5] = True
                                    chapter = '2'
                                    examining = False
                                    bed()
                            else:
                                tutorialSwitch[6] = False
                                part = '1'
                                switch[5] = True
                                examining = False
                                chapter = '2'
                                bed()
                        else:
                            bed()
                            if(c2Switch[2] == True):
                                switch[7] = True
                                part = '3'
                                c2Switch[2] = False
                            examining = False
                        cont()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '6'):
            if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False):
                print("The cottage was out of sight, but being familiar with the surrounding 'plants', and 'rocks' Alder knew where he was. There were some 'crickets' nearby, perfect for tonight’s meal.")
            else:
                print("The cottage was out of sight, but being familiar with the surrounding 'plants', and 'rocks' Alder knew where he was.")
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                print('It was a bright, clear blue.')
                cont()
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                if (PKSwitch[3] == True):
                    print('There were a variety of late-summer mushrooms around the area. Many of which are edible.')
                    cont()
                    pickup = input('Do you want to pick up the mushrooms.(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n3 mushrooms(s) obtained')
                        itemCount(food[3], 3)
                        PKSwitch[3] = False
                else:
                    print('There was a variety of late-summer mushrooms around the area. Some circled the area as part of the spell need to go between the realms. Alder knew better than to pick these.')
                    cont()
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                print('Various weeds, wildflowers and moss.')
                cont()
            elif (e == 'trees' or e == 'Trees'):
                print('Various trees made up the woodland, the most frequent were birch, rowen and holly.')
                cont()
            elif (e == 'rocks' or e == 'Rocks' or e == 'boulder' or e == 'Boulder'):
                print('There were a few boulders in the area. There was a large one were the cottage was.')
                cont()
            elif (e == 'cottage' or e == 'Cottage'):
                print('The cottage was gone from sight. Replaced with a large boulder.')
                cont()
            elif (e == 'cricket' or e == 'Cricket' or e == 'crickets' or e == 'Crickets'):
                if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False):
                    print('Some large brown crickets were in the area.')
                    cont()
                    fight = input('Do you want to fight them.(y/n)')
                    confirm = yn(fight)
                    if (confirm == True):
                        print('Entering battle')
                        battle([Cricket(), Null(), Null()])
                        if(alder.cExp > 0):
                            print('Alder:')
                            print('"Hunt succesful."')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('As Alder collected the slain cricket the loud buzzing came at him from his side. Two hornet came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            battle([Hornet(), Hornet(), Null()])
                        elif(alder.cExp == 0):
                            print('Alder:')
                            print('"Come back you!"')
                            cont()
                            print('Alder tried in vain to get the cricket, but it had already jumped out of reach.')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('The loud buzzing of insect wing came from Alder'"'"'s side. Two hornet came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            battle([Hornet(), Hornet(), Null()])
                        if (alder.health <= 0 or game_active == False):
                            #print('When Alder is defeated he will lose some of his possessions such as currency. The story will be taken back to before the fight so another attempt can be made.')
                            location = '3'
                            alder.health = alder.maxHealth
                            alder.stamina = alder.maxStamina
                        else:
                            tutorialSwitch[5] = False
                            print('The hornets were twitching but Alder knew they were dead.')
                            cont()
                            print('Alder:')
                            print('"Did I anger them?"')
                            cont()
                            print('Alder was still puzzled by the attack but regardless it was time to return.')
                            cont()
                        examining = False
                else:
                    print('The other crickets had fled.')
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '7'):
            if(c2Switch[3] == True):
                print("Large 'trees' surrounded him in a neat circle like pillars; the 'branches' formed a mosaic ceiling. There was a 'light' from an unknown source that shone in the center in front of Alder.")
            else:
                print("The mouse was holding the 'sword's' hilt to Alder's hand while ghostly 'spectors' watched.")
            e = input('Examine: ')
            if(e == 'trees' or e == 'Trees' or e == 'pillars' or e == 'Pillars'):
                print('Giant trees formed a perfect circle around the clearing like pillars.')
            elif(e == 'ceiling' or e == 'Ceiling' or e == 'mosaic' or e == 'Mosaic' or e == 'branches' or e == 'Branches'):
                print('The ceiling was covered in various different leaves such as oak, cider, alder and many others which Alder did not recognise, their branches were curved so the whole was a spiralling mosaic.')
            elif(e == 'light' or e == 'Light'):
                print('From the centre of the clearing a misty light hung from unknown source. It illuminating the area as far as the trees.')
                examining = False
                if(c2Switch[3] == True):
                    switch[8] = True
                    part = '4'
            elif (e == 'e' or e == 'E'):
                examining = False
            elif(c2Switch[3] == False):
                if(e == 'sword' or e == 'Sword'):
                    print('The sword was a double edge and was dark green with silver decorations on the hilt and scabbard. Now that it was close Alder could see what looked like a thorny stem engraved around the grip, the rain-guard was shaped to resemble leaves and the pommel from Alder’s angle was tear-shaped. The scabbard was a dark green and it had a rounded slot carved into it.')
                    cont()
                    sword = input('Take the sword!(y/n)')
                    confirm = yn(sword)
                    if(confirm == True):
                        switch[9] = True
                        part = '5'
                        examining = False
                elif(e == 'ghosts' or e == 'Ghosts' or e == 'spectors' or e == 'Spectors'):
                    print('The ghostly specters lingered within the darkness between the trees. Every creature of Albion imaginable was there.')
                elif (e == 'e' or e == 'E'):
                    examining = False
            
#Talk to a character
def talk():
    global switch, tutorial1, part, location
    print('\nTalk')
    if (location == '1'):
        if (tutorialSwitch[5] == False and chapter == '1'):
            print('1: Florace')
            t = input('talk to: ')
            if (t == '1'):
                if(alder.health < alder.maxHealth):
                    print('Florace:')
                    print('"You look worse for wear."')
                    cont()
                    print('Florace:')
                    print('"Hold still I'"'"'ll help fix you up."')
                    cont()
                    alder.health = alder.maxHealth
                    print('Alder:')
                    print('"Thank you."')
                    cont()
                elif(alder.health == alder.maxHealth):
                    print('Florace:')
                    print('"You look tired."')
                    cont()
                    print('Florace:')
                    print('"Take a nap you'"'"'ll feel better"')
                    cont()
        else:
            print('There was no one to talk to')
    elif (location == '2'):
        if (tutorialSwitch[5] == False and chapter == '1'):
            if (sQuests[0]['accepted'] != True):
                print('1: Kyla(!)')
                t = input('talk to: ')
                if (t == '1'):
                    print('Madam Kyla was relaxed in her chair with her nose in a red book titled "A sorcerers guide to Dragons and Wyverns". She peered from the book to her servant.')
                    cont()
                    print('Kyla:')
                    print('"I take it that Mr Prickle has gone?"')
                    cont()
                    print('Alder:')
                    print('"Yes madam."')
                    cont()
                    print('Kyla:')
                    print('"Then I take it you are free boy?"')
                    cont()
                    print('Alder:')
                    print('"Yes madam."')
                    cont()
                    print('Kyla:')
                    print('"Then clean the fireplace, wash the cauldron in the kitchen and-"')
                    cont()
                    print('Kyla:')
                    print('"Ah!"')
                    cont()
                    print('Kyla:')
                    print('"I need you to grind some bramble leaves."')
                    cont()
                    print('Kyla:')
                    print('"Use the mortar in the shed to grind them into dust."')
                    cont()
                    print('Kyla:')
                    print('"And make sure the dust is left in the pot on the far end next to the table."')
                    cont()
                    print('Kyla:')
                    print('"That should keep you busy!"')
                    cont()
                    i = input('Do you accept this labour?(y/n):')
                    confirm = yn(i)
                    if(confirm == True):
                        print('Alder:')
                        print('"Yes madam."')
                        cont()
                        print('Kyla:')
                        print('"Excellent!"')
                        cont()
                        print('Alder accepted the chores')
                        sQuests[0]['accepted'] = True
                        cont()
                    else:
                        print('Alder:')
                        print('"..."')
                        cont()
                        print('Kyla:')
                        print('"Don'"'"'t you glare at me!"')
                        cont()
                        print('Kyla:')
                        print('"Work for your sanctuary!"')
                        cont()
                        print('Kyla:')
                        print('"I'"'"'m not permitting you here out of charity!"')
                        cont()
                        print('Kyla:')
                        print('"Work for your sanctuary!"')
                        cont()
                        print('Alder:')
                        print('"U-Um."')
                        cont()
                        print('Alder:')
                        print('"Y-Yes!"')
                        cont()
                        print('Alder:')
                        print('"Sorry madam."')
                        cont()
                        print('Alder knew better than to argue back. Alder accepted the chores.')
                        sQuests[0]['accepted'] = True
                        cont()
            else:
                print('1: Kyla')
                t = input('talk to: ')
                if (t == '1'):
                    if (sQuests[0]['completed'] != True):
                        print('Kyla:')
                        print('"Clean the fireplace, scrub the cauldron and grind the leaves."')
                        cont()
                        print('Kyla:')
                        print('"Those are your duties for the day."')
                        cont()
                    elif (sQuests[0]['completed'] == True and sQuests[0]['submitted'] != True):
                        print('Kyla:')
                        print('"Have you finished then?"')
                        cont()
                        print('Alder:')
                        print('"Yes madam."')
                        cont()
                        print('Kyla:')
                        print('"Good."')
                        cont()
                        sQuests[0]['submitted'] = True
                        print('Kyla:')
                        print('"I have no futher need for you."')
                        cont()
                        print('Kyla:')
                        print('"Do as you please."')
                        cont()
                        qComp(sQuests[0])
                    else:
                        print('Kyla:')
                        print('"I have no futher need for you."')
                        cont()
                        print('Kyla:')
                        print('"Do as you please."')
                        cont()
        elif (c2Switch[1] == False and chapter == '2'):
            print('1: Florace')
            print('2: Kyla')
            t = input('talk to: ')
            if (t == '1'):
                print('Florace:')
                print('"Don'"'"'t go too far from now on."')
                cont()
                print('Florace:')
                print('"I don'"'"'t want you getting caught."')
                cont()
            elif (t == '2'):
                print('Kyla:')
                print('"They will never find this cottage."')
                cont()
                print('Kyla:')
                print('"Needless worry."')
                cont()
        elif (c2Switch[2] == False and chapter == '2'):
            print('1: Florace')
            print('2: Kyla')
            t = input('talk to: ')
            if (t == '1'):
                print('Florace:')
                print('"Triss is very brave."')
                cont()
                print('Florace:')
                print('"She risks everything to help people get around the Gowls."')
                cont()
            elif (t == '2'):
                print('Kyla:')
                print('"I like the girl."')
                cont()
                print('Kyla:')
                print('"Shame she never stays."')
                cont()
        elif (chapter == '3'):
            if(c3Switch[1] == True):
                print('1: Florace')
                print('2: Kyla')
                t = input('talk to: ')
                if (t == '1'):
                    print('Florace:')
                    print('"I think we will need to have a long discussion about that sword Alder."')
                    cont()
                elif (t == '2'):
                    print('Kyla:')
                    print('"The book is called "Magical thing of history"."')
                    cont()
                    print('Kyla:')
                    print('"Go get it."')
                    cont()
            elif(c3Switch[2] == True):
                print('1: Florace')
                print('2: Kyla')
                t = input('talk to: ')
                if (t == '1'):
                    print('Florace:')
                    print('"I'"'"'ve never heard that voice before."')
                    cont()
                elif (t == '2'):
                    print('Kyla:')
                    print('"Hmm."')
                    cont()
            elif(c3Switch[5] == True):
                if (sQuests[1]['accepted'] != True):
                    print('1: Florace(!)')
                else:
                    print('1: Florace')
                if (sQuests[2]['accepted'] != True):
                    print('2: Kyla(!)')
                else:
                    print('2: Kyla')
                if(c3Switch[4] == True):
                    print('3: Weasel')
                elif(c3Switch[5] == True):
                    print('3: Jeb')
                t = input('talk to: ')
                if (t == '1'):
                    if (sQuests[1]['accepted'] != True):
                        print('Alder:')
                        print('"What the matter Florace?."')
                        cont()
                        print('Florace:')
                        print('"We need food supplies to get to Forton!"')
                        cont()
                        print('Alder:')
                        print('"like what?"')
                        cont()
                        print('Florace:')
                        print('"Take what you can from the larder."')
                        cont()
                        sQuests[1]['accepted'] = True
                    elif(sQuests[1]['completed'] != True):
                        print('Florace:')
                        print('"I wish we were better prepaired, but there'"'"'s nothing we can do about it"')
                        cont()
                    elif(sQuests[1]['submitted'] != True):
                        print('Alder:')
                        print('"This was all there was."')
                        cont()
                        print('Alder:')
                        print('"Will it be enough?"')
                        cont()
                        print('Florace:')
                        print('"I hope so."')
                        cont()
                        print('Florace:')
                        print('"Thanks Alder."')
                        cont()
                        sQuests[1]['submitted'] = True
                        qComp(sQuests[1])
                    else:
                        print('Florace:')
                        print('"You doing alright Alder?"')
                        cont()
                        print('Alder:')
                        print('"Fine."')
                        cont()
                        print('Alder:')
                        print('"But are you sure you want to give up your apprentiship?"')
                        cont()
                        print('Florace:')
                        print('"I'"'"'m not leaving you Alder!"')
                        cont()
                        print('Florace:')
                        print('"I'"'"'ll protect you no matter what!"')
                        cont()
                elif (t == '2'):
                    if (sQuests[2]['accepted'] != True):
                        print('Kyla:')
                        print('"Boy before I relieve you of my service I need you to gather my books from the bookshelf and the pots of ingredients from the shed and bring them here."')
                        cont()
                        print('Alder:')
                        print('"But the rat is outside how do I get to the shed?"')
                        cont()
                        print('Kyla:')
                        print('"You will have to break down the '"'wall'"'."')
                        cont()
                        print('Kyla:')
                        print('"He'"'"'ll never hear it with my sound nullifying spell."')
                        cont()
                        print('Kyla:')
                        print('"Don'"'"'t concern yourself with any mess we need to get those vaulbles out safely."')
                        cont()
                        sQuests[2]['accepted'] = True
                    elif(sQuests[2]['completed'] != True):
                        print('Kyla:')
                        print('"I need the books from the shelves and the pots from the shed."')
                        cont()
                    elif(sQuests[2]['submitted'] != True):
                        print('Kyla:')
                        print('"Excellent!"')
                        cont()
                        print('Kyla:')
                        print('"Get them in the bag!"')
                        cont()
                        print('Kyla had gotten a bag and with Alder'"'"'s assisstance placed the books and pots inside it one by one. The bag itself never got any larger or heavier while the pile eventually disappeared.')
                        cont()
                        print('Kyla:')
                        print('"Finish getting ready."')
                        cont()
                        print('Kyla:')
                        print('"We leave soon."')
                        cont()
                        sQuests[2]['submitted'] = True
                        qComp(sQuests[2])
                    else:
                        print('Kyla:')
                        print('"I was sloppy!"')
                        cont()
                        print('Kyla:')
                        print('"I should have arranged an escape route the moment Trissie told us about the Gowls!"')
                        cont()
                        print('Kyla:')
                        print('"Still I don'"'"'t like that they knew our password."')
                        cont()
                        print('Kyla:')
                        print('"Someone mush have snitched..."')
                        cont()
                if(c3Switch[3] == False and c3Switch[4] == True):
                    if (t == '3'):
                        switch[13] = True
                elif(c3Switch[4] == False and c3Switch[5] == True):
                    if (t == '3'):
                        print('Jeb:')
                        print('"What would you like Scion?"')
                        cont()
                        shop('Jeb')
                        if ((sQuests[1]['accepted'] == True and sQuests[1]['submitted'] != True) or (sQuests[2]['accepted'] == True and sQuests[2]['submitted'] != True)):
                            ab = input('Abandon quests?(y/n)')
                            confirm = yn(ab)
                            if (confirm == True):
                                if (sQuests[1]['accepted'] == True and sQuests[1]['submitted'] != True):
                                    sQuests[1]['accepted'] = False
                                    print(sQuests[1]['name'],' abandoned!')
                                if (sQuests[2]['accepted'] == True and sQuests[2]['submitted'] != True):
                                    sQuests[2]['accepted'] = False
                                    print(sQuests[1]['name'],' abandoned!')
                                switch[14] = True
                                part = '4'
                        else:
                            switch[14] = True
                            part = '4'
        else:
            print('There was no one to talk to')
    elif (location == '3'):
        if (chapter == '1'):
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
                            print('"He usually comes here for sanctuary or phantom cloak potions."')
                            cont()
                            dialog[0] = True
                        if (c == '2'):
                            print('Florace:')
                            print('"Well."')
                            cont()
                            print('Florace:')
                            print('"Kyla’s cast several illusions on the cottage, one of which makes it looks like a boulder from the outside."')
                            cont()
                            print('Florace:')
                            print('"She'"'"'s also muted the rooms and made our scents smell somewhat grassy."')
                            cont()
                            print('Florace:')
                            print('"We tend to call this place the burrow as it cannot be seen from the outside world."')
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
                            print('"This summer has been good to us all."')
                            cont()
                            dialog[0] = True
                        if (c == '2'):
                            print('Thay:')
                            print('"The usual, gave her the herbs she wanted and she gave me the potions I needed."')
                            cont()
                            print('Thay took out a vial of black liquid. Phantom Cloak; a magic potion that erased a creature’s presence when in darkness. It was one of many potions that brought patrons to the cottage. Alder never asked what they needed them for.')
                            cont()
                            dialog[1] = True
                        if (c == '3'):
                            print('Thay:')
                            print('"Well, to the north, there are more woodlands."')
                            cont()
                            print('Thay:')
                            print('"But to the south is the settlement in the valley where mice and other small beasts live."')
                            cont()
                            print('Thay:')
                            print('"In the west you’ll run into the river and if you climb to the treetops you can see Hare Hill in the east."')
                            cont()
                            print('Thay:')
                            print('"Wait!?"')
                            cont()
                            print('With sudden realization of who he was speaking to, Thay panicked at the thought of feeding the curiosity of the boy.')
                            cont()
                            print('Thay:')
                            print('"Alder, you aren'"'"'t thinking of going to these places are you!?"')
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
                            print('"If anyone sees you, you will be killed!!"')
                            cont()
                            print('Thay:')
                            print('"I cannot even express how much humans are hated!!"')
                            cont()
                            print('Alder:')
                            print('"Ok! Ok!"')
                            cont()
                            print('Alder:')
                            print('"I won’t go wandering!!"')
                            cont()
                            print('Alder:')
                            print('"I'"'"'m sorry!"')
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
                                print('Thay:')
                                print('"Oldwyrm woods is where we are right now."')
                                cont()
                                print('Thay:')
                                print('"This ancient woodland that goes on for miles."')
                                cont()
                                print('Thay:')
                                print('"There are many birds in these woods, unfortunately that includes birds of prey, but most go after small creatures so you'"'"'re alright."')
                                cont()
                                dialog2[0] = True
                            if (c == '5'):
                                print('Alder:')
                                print('"It’s not that I want to go there but I’d like to know."')
                                cont()
                                print('Thay:')
                                print('"It’s called Forton."')
                                cont()
                                print('Thay:')
                                print('"It’s known for its great library, taking in orphans within the region and being the resting place of the hero, Agrimus."')
                                cont()
                                print('Thay:')
                                print('"It is also one of the few mouse settlements that is not controlled by the woodland church."')
                                cont()
                                dialog2[1] = True
                            if (c == '6'):
                                print('Alder:')
                                print('"Florace and I sometimes go there to get water."')
                                cont()
                                print('Alder:')
                                print('"With caution of course."')
                                cont()
                                print('Alder:')
                                print('"We caught a fish in our bucket once."')
                                cont()
                                print('Thay:')
                                print('"Hmm. You sure that’s safe?"')
                                cont()
                                print('Thay:')
                                print('"There are many creatures drifting on the river."')
                                cont()
                                print('Thay:')
                                print('"Swimming in it too."')
                                cont()
                                print('Alder:')
                                print('"It’s alright."')
                                cont()
                                print('Alder:')
                                print('"Florence has always kept us hidden."')
                                cont()
                                print('Thay:')
                                print('"Err, ok then."')
                                cont()
                                dialog2[2] = True
                            if (c == '7'):
                                print('Alder:')
                                print('"It’s not that I want to go there, I’d just like to know."')
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
                                print('"But it is a difficult and exhausting hike and travelers need to scramble up rock walls in some places."')
                                cont()
                                print('Thay:')
                                print('"Unless they go through the rabbits tunnels."')
                                cont()
                                print('Thay:')
                                print('"Oh! Nevermind."')
                                cont()
                                print('Alder:')
                                print('"What?"')
                                cont()
                                print('Thay:')
                                print('"Just. Nevermind."')
                                cont()
                                dialog2[3] = True
                            if (c == '8'):
                                print('Thay:')
                                print('"Well. There was a certain king who did very, very bad things."')
                                cont()
                                print('Alder:')
                                print('"What kinds of things?"')
                                cont()
                                print('Thay:')
                                print('"Things you'"'"'re too young to hear."')
                                cont()
                                print('Thay:')
                                print('"But all you need to know is that he was cruel and unforgivable."')
                                cont()
                                print('Thay:')
                                print('"So unforgivable in fact that along with his followers, woodland folk even took vengeance on the humans who did not support him."')
                                cont()
                                print('Alder:')
                                print('"But why?"')
                                cont()
                                print('Alder:')
                                print('"What did they do?"')
                                cont()
                                print('Thay:')
                                print('"Nothing."')
                                cont()
                                print('Thay:')
                                print('"But that didn’t matter to those who had lost friends and family in the conflict."')
                                cont()
                                print('Thay:')
                                print('"Best for you to stay within the burrows border young one."')
                                cont()
                                print('Thay:')
                                print('"If you are seen."')
                                cont()
                                print('Thay:')
                                print('"You will be assumed aligned with the kings ideals and killed."')
                                cont()
                                print('Alder gave a sad longing look to the deep wood. He’d like to see more than the tiny patch he called home. But alas as Thay said, the danger was too great.')
                                cont()
                                dialog2[4] = True
                    switch[3] = True
                    part = '3'
                    tutorialSwitch[3] = False
                    tutorial1 = False
            elif (tutorialSwitch[4] == True):
                print('1: Florace')
                t = input('talk to: ')
                if (t == '1'):
                    dialog = [False]
                    while(dialog[0] == False):
                        print('Florace:')
                        print('"The knife should be in the shed. You can go once you'"'"'ve got it."')
                        cont()
                        dialog[0] = True
            elif (tutorialSwitch[5] == True):
                print('1: Florace')
                t = input('talk to: ')
                if (t == '1'):
                    if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False):
                        dialog = [False, False]
                        while(dialog[0] == False and dialog[1] == False):                    
                            print('1: "I have the knife!"')                  
                            print('2: "Nevermind"')
                            c = input('Alder: ')
                            if (c == '1'): 
                                print('Florace:')
                                print('"Fantastic!"')
                                cont()
                                print('Florace:')
                                print('"Just please don'"'"'t go too far."')
                                cont()
                                dialog[0] = True
                            if (c == '2'):
                                dialog[1] = True
            
            else:
                print('There was no one to talk to')
        elif(chapter == '2'):
            if (c2Switch[0] == False and c2Switch[1] == True):
                print('1: Trissie')
                t = input('talk to: ')
                if (t == '1'):
                    print('Trissie quickly set up a makeshift dummy out of leaves, sticks and a cheaply made old burlap sack that was intended for foraging. She then planted it into the ground so it would stand upright. The finished product was crude and clearly rushed, but would make a good target.')
                    cont()
                    print('Trissie:')
                    print('"That'"'"'ll do."')
                    cont()
                    print('Trissie:')
                    print('"Alder, wait there."')
                    cont()
                    print('Trissie went into the shed and retrived a bow and some arrows set aside for hunting. Alder thought she looked a little silly dragging the bow which was big even for him. The bow was originally meant for Florace, but finding herself unskilled she never used it. Trissie handed them to Alder.')
                    cont()
                    alder.weapon2 = weapons[3]
                    print('\nTraining bow equipped')
                    itemCount(projec[0], 5)
                    print('\n5 Primitive arrows obtained')
                    print('Trissie:')
                    print('"Now set the arrow in the bow, take aim and fire."')
                    cont()
                    print('Trissie:')
                    print('"Let'"'"'s begin."')
                    cont()
                    battle([Dummy(), Null(), Null()])
                    if (alder.health > 0 or game_active == True):
                        print('Trissie:')
                        print('"Nice shot!"')
                        cont()
                        print('Trissie:')
                        print('"But it will be hard for me to leave these woods if I stay any longer!"')
                        cont()
                        print('Alder:')
                        print('"There’s one more thing I’d like to know Triss."')
                        cont()
                        print('Trissie:')
                        print('"Yes?"')
                        cont()
                        dialog = [False, False]
                        while(dialog[0] == False and dialog[1] == False):
                            print('1: "What are the Gowls like?"')
                            print('2: "Will we see each other again soon?"')
                            c = input('Alder: ')
                            if (c == '1'):
                                print('Trissie:')
                                print('"Well, if I’d have to give an example?"')
                                cont()
                                print('Trissie:')
                                print('"I have a brother in the Gowls"')
                                cont()
                                print('Trissie points her thumb at her tail stump.')
                                cont()
                                print('Trissie:')
                                print('"And because I helped a human, he did this to me."')
                                cont()
                                branchSwitch[0] = '1'
                                dialog[0] = True
                            elif (c == '2'):
                                print('Trissie:')
                                print('"I’m not easy to capture but you must be careful and survive."')
                                cont()
                                print('Trissie:')
                                print('"Then I am sure we will meet again."')
                                cont()
                                branchSwitch[0] = '2'
                                dialog[1] = True
                        print('Trissie went towards the nearest tree and in an instant had climbed up and disappeared among the branches. It was as if she'"'"'d vanished. Leaving not even a rustle of leaves.')
                        cont()
                        print('Alder returned to the cottage a little disappointed with Trissie gone so soon. But he had work to do and he set about his remaining chores for the day.')
                        cont()
                        c2Switch[1] = False
            else:
                print('There was no one to talk to')
        elif (chapter == '3'):
            if (c3Switch[2] == False and c3Switch[3] == True):
                print('1: Rat')
                t = input('talk to: ')
                if (t == '1'):
                    print('Alder did not want to get too close to the rat. Even if he could not touch or speak to him.')
            else:
                print('There was no one to talk to')
                    
    elif(location == '7'):
        if(c2Switch[2] == False):
            print('1: Mouse')
            t = input('talk to: ')
            if (t == '1'):
                print('Mouse:')
                print('"..."')
                cont()
                print('The mouse did not speak just looked at Alder warmly.')
                cont()
        else:
            print('There was no one to talk to.')
    else:
        print('There was no one to talk to.')
#Move to another location
def move():
    global location, part, tutorial1, tutorialSwitch, c2Switch
    print('\nMove')
    for i in locations:
        if (location == i['locId']):
            print('Currently:',i['name'])
    if (location == '1'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            if(tutorialSwitch[0] == True):
                tutorialSwitch[0] = False
            print('Alder moved to the living room of the cottage.')
            alder.stamina -= 1    
            cont()
    elif (location == '2'):
        print('1: Kitchen')
        print('2: Outside')
        print('3: Alder'"'"'s room')
        if (sQuests[2]['required'][1] == True):
            print('4: Shed')
        m = input('Move to: ')
        if (m == '1' or m == 'kitchen' or m == 'Kitchen'):
            location = '1'
            print('Alder moved to the kitchen.')
            alder.stamina -= 1    
            cont()
        elif (m == '2'):
            if (c3Switch[1] == False and c3Switch[2] == True and chapter == '3'):
                print('Florace:')
                print('"Wait Alder!"')
                cont()
                print('Florace:')
                print('"Keep close to me."')
                cont()
                print('Florace:')
                print('"To the window."')
                cont()
            elif (c3Switch[2] == False and c3Switch[5] == True and chapter == '3'):
                print('with the Gowl'"'"'s outside it wasn'"'"'t worth risking')
            else:
                location = '3'
                print('Alder moved outside the cottage through the front door.')
                alder.stamina -= 1
                cont()
                if(tutorialSwitch[1] == True and chapter == '1'):
                    part = '2'
                    tutorialSwitch[1] = False
                    switch[1] = True
                    tutorial1 = False
                elif(c3Switch[5] == False):
                    switch[15] = True
                    c3Switch[6] = False
        elif (m == '3'):
            location = '5'
            print('Alder moved upstairs and into his bedroom.')
            alder.stamina -= 1    
            cont()
        elif (sQuests[2]['required'][1] == True):
            if (m == '4'):
                location = '4'
                print('Alder moved through the hole and into the shed.')
                alder.stamina -= 1    
                cont()
    elif (location == '3'):
        print('1: Living Room')
        print('2: Shed')
        print('3: Woods')
        m = input('Move to: ')
        if (m == '1'):
            if (tutorialSwitch[2] == False and tutorialSwitch[5] == True):
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
            elif (c2Switch[0] == True):
                location = '2'
                print('Alder moved to the living room of the cottage.')
                alder.stamina -= 1
                switch[6] = True
                part = '2'
            elif (c3Switch[2] == False and c3Switch[3] == True):
                location = '2'
                print('Alder moved to the living room of the cottage.')
                alder.stamina -= 1
                switch[13] = True
            else:
                location = '2'
                print('Alder moved to the living room of the cottage.')
                alder.stamina -= 1    
                cont()
        elif (m == '2'):        
            location = '4'
            print('Alder moved to the shed at the side of the cottage.')  
            alder.stamina -= 1  
            cont()
        elif (m == '3'):
            if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False and alder.weapon1['wpId'] != '0'):
                location = '6'
                print('Alder left the cottage grounds.')
                alder.stamina -= 1    
                cont()
            else:
                print('It'"'"'s dangerous to leave the cottage unarmed.')
                cont()
    elif (location == '4'):
        if (sQuests[2]['required'][1] == True):
            print('1: Living room')
        else:
            print('1: Outside')
        m = input('Move to: ')
        if (m == '1'):
            if (sQuests[2]['required'][1] == True):
                location = '2'
                print('Alder went back through the hole into the living room of the cottage.')
                alder.stamina -= 1
                cont()
            else:
                location = '3'
                print('Alder left the shed and back to the front of the cottage.')
                alder.stamina -= 1
                cont()
    elif (location == '5'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            if (chapter == '3' and c3Switch[0] == True):
                print('Alder jumped out of bed and ran into the living room and is soon joined by Florace.')
                cont()
                print('Florace:')
                print('*Groan*')
                cont()
                print('Florace:')
                print('"Alder, it'"'"'s really early, don’t wake me."')
                cont()
                print('Florace gives Alder an annoyed look before she notices the sword he was holding.')
                cont()
                print('Florace:')
                print('"Alder, what is that!!"')
                cont()
                print('Alder:')
                print('"It’s a sword!"')
                cont()
                print('Florace:')
                print('"Why do you have a sword and where did it come from!"')
                cont()
                print('Alder:')
                print('"A mouse in my dreams gave it to me."')
                cont()
                print('Florace:')
                print('"What!?"')
                cont()
                print('She was confused by Alder'"'"'s response but it was clear she was sceptical.')
                cont()
                print('Kyla:')
                print('"Heh Heh."')
                cont()
                print('Kyla:')
                print('"What'"'"'s this about a sword?"')
                cont()
                print('Kyla had come out of her room somewhat amused by Floraces shouts. She then looks at Alder. Her eyes widen as she sees the sword that Alder had.')
                cont()
                print('Kyla:')
                print('"Boy, let me see that sword!"')
                cont()
                print('Alder:')
                print('"Um?"')
                cont()
                print('Alder:')
                print('"O-ok."')
                cont()
                print('Alder hands the sword over to Kyla and with Floraces assistance she takes it to the table downstairs.')
                cont()
                print('Kyla:')
                print('"It can’t be?"')
                cont()
                print('Kyla:')
                print('"Boy, in the bookshelf, there should be a blue book on magical artefacts, could you get it."')
                cont()
                print('Kyla:')
                print('"Look for the page that has this sword in it."')
                cont()
                print('Alder:')
                print('"Right."')
                c3Switch[0] = False
            else:
                print('Alder went down stairs into the living room.')
            alder.stamina -= 1
            cont()
    elif (location == '6'):
        print('1: Cottage grounds')
        print('2: Deep Woods')
        m = input('Move to: ')
        if (m == '1'):
            location = '3'
            if(tutorialSwitch[5] == False):
                print('Alder:')
                print('"Florace! I'"'"'m done!"')
                cont()
                print('Florace was having a conversation with Thay, when they looked at Alder they immediately noticed the swollen red marks where the hornets had stung his exposed skin.')
                cont()
                print('Florace:')
                print('"Alder what happened, are you ok!"')
                cont()
                print('Alder:')
                print('"Um!?"')
                cont()
                print('Alder:')
                print('"I got stung by hornets a few times but i'"'"'m alright!"')
                cont()
                print('Florace:')
                print('*Sigh*')
                cont()
                print('Florace:')
                print('"Give the bugs and the knife to me and go relax yourself."')
                cont()
                print('Thay:')
                print('"Here some plantain might ease some of your discomfort."')
                cont()
                print('Alder passed the bug meat and the hunting knife over to her. Florace went inside the cottage to prepare the crickets for supper. Thay applied poultice of greater plantain to Alder stings.')
                for i in inv:
                    if (i['type'] == 'food'):
                        if (i['itemId'] == '5'):
                            inv.remove(i)
                alder.weapon1 = weapons[0]
                alder.health += 10
                print('\nHunting Knife unequiped')
                cont()
                mQuests[0]['submitted'] = True
                part = '4'
                switch[4] = True
            alder.stamina -= 1
        elif (m == '2'):
            print('Alder once got lost after he strayed too far from the cottage.')
            cont()
            print('He spent hours in the dark until Florace found him crying and scared.')
            cont()
            print('Kyla was indifferent to the situation.')
            cont()
    elif (location == '7'):
        print('Alder could not move.')
#Save the game
def save(location, chapter, part):
    data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, branchSwitch, shill, inv, PKSwitch, mQuests, sQuests, alder]
    #print (location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, branchSwitch, shill, inv, PKSwitch, mQuests, sQuests, alder)
    i = input('Save in file "1", "2" or "3":')
    if (i == '1'):
        PIK = 'data/file1.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')
    elif (i == '2'):
        PIK = 'data/file2.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')
    elif (i == '3'):
        PIK = 'data/file3.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')

def inventory():
    listItems = []
    bag = True
    j = ''
    while(bag == True):
        #View the items in inventory
        #The same items should be counted to keep the list clear
        #Items should be in a order based on the item type
        #Input should allow the list to be narrowed down or print all items
        print('\nInventory')
        print('Shillings: ', shill)
        count = 1
        listItems.clear()
        if (j == '' or j == 'food' or j == 'Food' or
            j == 'consumables' or j == 'Consumables'):
            print('Food')
            for i in inv:
                if (i['type'] == 'food'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'healing' or j == 'Healing' or
            j == 'health' or j == 'Health'):
            print('Healing')
            for i in inv:
                if (i['type'] == 'healing'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'projectiles' or j == 'Projectiles'):
            print('Projectiles')
            for i in inv:
                if (i['type'] == 'projectile' or i['type'] == 'projectile'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'weapons' or j == 'Weapons'):
            print('Weapons')
            for i in inv:
                if (i['type'] == 'weapon' or i['type'] == 'bow' or i['type'] == 'sheild'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'armour' or j == 'Armour'):
            print('armour')
            for i in inv:
                if (i['type'] == 'hat' or i['type'] == 'shirt' or i['type'] == 'trousers'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'ingredients' or j == 'Ingredients'):
            print('Ingredients')
            for i in inv:
                if (i['type'] == 'ingre'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        print('\n1: Appraise')
        print('2: Use')
        print('3: Equip')
        print('e - Exit')
        i = input('Item: ')
        if (i == '' or i == 'food' or i == 'Food' or i == 'consumables' or i == 'Consumables' or i == 'healing' or i == 'Healing' or
            i == 'health' or i == 'Health' or i == 'weapons' or i == 'Weapons'  or i == 'armour' or i == 'Armour' or
            i == 'projectiles' or i == 'Projectiles' or i == 'ingredients' or i == 'Ingredients' or
            i == '1' or i == '2' or i == '3' or i == 'e'):
            j = i
        #Appraise items in inventory
        if (j == '1'):
            appraise = input('\nItem number: ')
            count = 1
            for i in listItems:
                if (appraise == str(count)):
                    if (i['type'] != 'food'):
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nDescription: ', i['description'])
                    else:
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nStamina Recovered: ', i['recovers'])
                count += 1
        elif (j == '2'):
            equip()
        elif (j == 'e'):
            bag = False
        if (j == '1' or j == '2' or i == '3'):
            j = ''
    
#Achive objectives
def achive():
    for q in mQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            if (q['questId'] == '1'):
                amount = 0
                for i in inv:
                    if (i['type'] == 'food'):
                        if (i['itemId'] == q['required']['itemId']):
                            amount += i['count']
                if (amount >= 2):
                    q['completed'] = True
                else:
                    q['completed'] = False
    for q in sQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            if (q['type'] == 'action'):
                count = 0
                for i in q['required']:
                    if (i == True):
                        count += 1
                if (count == len(q['required'])):
                    q['completed'] = True
            if (q['type'] == 'collect'):
                count = 0
                for i in q['required']:
                    for j in inv:
                        if(i['type'] == j['type']):
                            if(i['itemId'] == j['itemId']):
                                if (j['count'] == q['qnt'][count]):
                                    q['completed'] = True
                    count += 1
                    
#Print the objectives
def objective():
    print("\nObjectives")
    print("Main:")
    if(tutorialSwitch[0] == True):
        print("\tYou will need to have a quick look around. Type "'"examine" or "e"'" to explore the room Alder is currently in then type in an 'object' from that room like the window.")
    elif(tutorialSwitch[1] == True):
        print('\tAlder needs to go outside. He will have to "move"("m") through the living room and then move outside.')
    elif(tutorialSwitch[2] == True):
        print('\tTalk(t) to Florace.')
    elif(tutorialSwitch[3] == True):
        print('\tTalk(t) to Thay.')
    elif(tutorialSwitch[4] == True):
        print('\tExamine table in the shed, pick up knife and "equip"("x") as main weapon.')
    elif(tutorialSwitch[5] == True):
        for q in mQuests:
            if(q['accepted'] == True and q['submitted'] != True):
                if (q['questId'] == '1'):
                    if(alder.weapon1['wpId'] != '2'):
                        print('\tPick up and equip hunting knife.')
                    else:
                        amount = 0
                        for i in inv:
                            if (i['type'] == 'food'):
                                if (i['itemId'] == '5'):
                                    amount += i['count']
                        print('\t', q['desc'],' (',amount,'/',q['qnt'],')')
    elif(tutorialSwitch[6] == True):
        print('\tReturn to the cottage and examine to bed to end the day.')
        print('\tTalk to characters if a character has a "!" mark then they will quest for Alder.')
    elif(c2Switch[0] == True):
        print('\tMove to the living room to attend meeting.')
    elif(c2Switch[1] == True):
        print('\tTalk to Trissie for archery practise')
    elif(c2Switch[2] == True):
        print('\tGo to bed.')
    elif(c2Switch[3] == True):
        print('\tExplore strange place.')
    elif(c3Switch[0] == True and chapter == '2'):
        print('\tTake sword!')
    elif(c3Switch[0] == True and chapter == '3'):
        print('\tGet Florace!')
    elif(c3Switch[1] == True):
        print('\tRead "Read Magical things of history".')
    elif(c3Switch[2] == True):
        print('\tLook out living room window.')
    elif(c3Switch[3] == True):
        print('\tLook out living room window.')
    elif(c3Switch[4] == True):
        print('\tTalk to weasel')
    elif(c3Switch[5] == True):
        print('\tBuy from Jeb.')
    elif(c3Switch[6] == True):
        print('\tLeave cottage.')
        
    print("\nSide:")
    for q in sQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            print('Quest: ',q['name'], ' Client: ',q['client'])
            if (q['type'] == 'action'):
                j = 0
                for i in q['desc']:
                    print('\t',i, q['required'][j])
                    j += 1
            elif (q['type'] == 'collect'):
                j = 0
                for i in q['desc']:
                    for k in inv:
                        for l in q['required']:
                            amount = 0
                            if (k['type'] == l['type'] and k['itemId'] == l['itemId']):
                                amount = k['count']
                                print('\t',i, '(', amount, '/', q['qnt'][j],')')
                            elif (amount == 0):
                                if(l['type'] == 'food'):
                                    for m in food:
                                        if (m['type'] == l['type'] and m['itemId'] == l['itemId']):
                                            print('\t',i, '(', amount, '/', q['qnt'][j],')')
                    j += 1
            if(q['reward'] != 'none' and q['rewardCount'] > 0):
                if q['reward'] == 'shillings':
                    print('\tReward: ', 'Shillings', 'x', q['rewardCount'],'\n')
                elif q['reward'] == 0:
                    print('\tReward: ', 'Shillings', 'x', q['rewardCount'],'\n')
                else:
                    print('\tReward: ', q['reward']['name'], 'x', q['rewardCount'],'\n')
def helper():
    print("\nCommand: e, examine, Examine - Allows Alder to investigate his surroundings. Examinating further can get an item to pickup.")
    print("Command: m, move, Move - Move to the next area.")
    print("Command: t, talk, Talk - Talk to a character.")
    print("Command: z, stats, Stats - Print the statistics of the playable characters.")
    print("Command: o, objective, Objective - Print the main and side quests.")
    print("Command: i, items, Items - View inventory.")
    print("Command: x, equip, Equip - Equip item.")
    print("Command: k, skill, Skill - Unlock Skill.")
    print("Command: s, save, Save - Save the game.")
    print("Command: 1, 2, etc - When you have a list of options.")    
    print("Command: y, Y, yes, Yes or, n, N, no, No - (y/n) statments.")
    print("(!) - Quest available")
    print("Command: q, quit, Quit - Leave to the main menu")

def helper2():
    print("Command: 1, attack, Attack - Deal damage to an opponent using a primary weapon.")
    print("Command: 2, defence, Defence - Absorb damage from an incoming attack.")
    print("Command: 3, appraise, Appraise - Get details on enemies.")
    print("Command: 4, special, Special - Use a special skill.")
    print("Command: 5, item, Item - Use an item from inventory.")
    print("Command: 6, flee, Flee - Escape the battle.")
    print("Food: Items used to recover stamina.")
    print("Medicine: Items used to heal or remove a status condition.")
    print("Ranged Weapons: To use a ranged weapon select a supported projectile from items then on the next turn attack to fire.")
    print("Throwing Items: Items such as nets can be thrown ")
    print("Order of combat: Fastest combatant.")

def free(location, chapter, part):
    global game_active, tutorial1
    hunger(False)
    achive()
    if (game_active == True):
        print('\nInteract')
        if(tutorialSwitch[0] == True):
            print("You will need to have a quick look around. Type "'"examine" or "e"'" to explore the room Alder is currently in, then type in an 'object' from that room. If you are having trouble with what to do, check the "'"objectives"("o")'"")
        elif(tutorialSwitch[1] == True):
            print('Alder needs to go outside. He will have to "move"("m") through the living room and then outside.')
        elif(tutorialSwitch[2] == True):
            print('While we wait for Thay let'"'"'s "talk"("t") to Florace.')
        elif(tutorialSwitch[3] == True):
            print('Some dialogs can unlock new ones. Let'"'"'s talk to Thay now.')
        elif(tutorialSwitch[4] == True):
            print('Alder will need the knife which is somewhere in the shed. Examine the area to find and pick up the knife and "equip"("x") the knife from your "items"("i") inventory as main weapon.')
        elif(tutorialSwitch[5] == True):
            print('Leave the cottage grounds and examine the area to find an opponent to fight. There will be six options available for each turn. Type "h2", "help2" or "Help2" for more details.')
        elif(tutorialSwitch[6] == True):
            print('Return to the cottage and sleep to bring an end to the day and the tutorial.')
        print("Health: ", alder.health, '/', alder.maxHealth, "| Stamina: ", alder.stamina, '/', alder.maxStamina)
        print("Type command: h, help, Help - For help.")
        action = input('Enter Command: ')
        if (action == 'e' or action == 'examine' or action == 'Examine'):
            examine(location)
        elif (action == 't' or action == 'talk' or action == 'Talk'):
            talk()
        elif (action == 'm' or action == 'move' or action == 'Move'):
            move()
        elif (action == 'z' or action == 'stats' or action == 'Stats:'):
            alder.stats()
        elif (action == 'o' or action == 'objective' or action == 'Objective'):
            objective()
        elif (action == 'i' or action == 'items' or action == 'Items'):
            if (location != '7'):
                inventory()
            else:
                print('Alder did not have anything with him.')
        elif (action == 'x' or action == 'equip' or action == 'Equip'):
            if (location != '7'):
                equip()
            else:
                print('Alder did not have anything with him.')
        elif (action == 'k' or action == 'skill' or action == 'Skill'):
            skillTree(alder)
        elif (action == 'h' or action == 'help' or action == 'Help'):
            helper()
        elif (action == 'h2' or action == 'help2' or action == 'Help2'):
            helper2()
        elif (action == 's' or action == 'save' or action == 'Save'):
            save(location, chapter, part)
        elif (action == 'q' or action == 'quit' or action == 'Quit'):
            print ("Are you sure you wan to quit to menu y/n")
            q = input('Enter Command: ')
            if (q == 'y' or q == 'Y' or q == 'yes' or q == 'Yes'):
                game_active = False

def game():
    global switch, tutorial1, location, chapter, part, location, shill, tutorialSwitch, c2Switch, c3Switch
    print('Chapter: ', chapter)
    print('The game will now begin. Press enter to print the next line.')
    print("You may skip the dialogue by typing 'skip' then pressing enter.")
    while (game_active == True):
        if (tutorComp == False):
            tutorial1 = True
        if (chapter == '0'):
            prologue = True
            skip = False
            f = open("data/Cutscenes.txt", "rt")
            for i in f:
                if(skip == False):
                    line = i.split('$ ')
                    if (line[0] == chapter):
                        newline = line[4].split('£')
                        if (len(newline) > 1):
                            print(newline[0],'\n',newline[1])
                        else:
                            print(line[4])
                        s = input()
                        if(s == 'skip'):
                            skip = True
            prologue = False
            chapter = '1'
        if (chapter == '1'):
            chapter1 = True
            if (switch[0] == True):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '0' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[0] = False
            elif (switch[1] == True and part == '2'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '1' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[1] = False
            elif (switch[2] == True and part == '2'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '2' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[2] = False
            elif (switch[3] == True and part == '3'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '3' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                mQuests[0]['accepted'] = True
                switch[3] = False
            elif (switch[4] == True and part == '4'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '4' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[4] = False
            if (game_active == True):
                free(location, chapter, part)
        if (chapter == '2'):
            if (switch[5] == True and part == '1'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '5' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                location = '3'
                switch[5] = False
            elif (switch[6] == True and part == '2'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '6' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[6] = False
                c2Switch[0] = False
            elif (switch[7] == True and part == '3'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '7' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                location = '7'
                switch[7] = False
            elif (switch[8] == True and part == '4'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '8' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                c2Switch[3] = False
                switch[8] = False
            elif (switch[9] == True and part == '5'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '9' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                chapter = '3'
                part = '1'
                switch[9] = False
                switch[10] = True
                part = '1'
            if (game_active == True):
                free(location, chapter, part)
        if (chapter == '3'):
            author = False
            if (switch[10] == True and part == '1'):
                location = '5'
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '10' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                switch[10] = False
            elif (switch[11] == True and part == '2'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '11' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                c3Switch[2] = False
                switch[11] = False
            elif (switch[12] == True and part == '3'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '12' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                c3Switch[3] = False
                switch[12] = False
            elif (switch[13] == True and part == '3'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '13' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                print('10 shillings obtained!\n')
                shill += 10
                c3Switch[4] = False
                switch[13] = False
            elif (switch[14] == True and part == '4'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '14' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                c3Switch[5] = False
                switch[14] = False
            elif (switch[15] == True and part == '4'):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter and line[1] == '15' and line[2] == part):
                            newline = line[4].split('£')
                            if (len(newline) > 1):
                                print(newline[0],'\n',newline[1])
                            else:
                                print(line[4])
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                author = True
                switch[15] = False
            while (author == True):
                print('James Stockwell:')
                print('"Thank you for playing the demo for the Wild and Wyrd. Please let me know if there are any errors or grammer mistakes. Please support me if you want to see more of Alder'"'"'s story."')
                cont()
            if (game_active == True):
                free(location, chapter, part)

def loadGame():
    global game_active, location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, branchSwitch, shill, inv, PKSwitch,mQuests,sQuests,alder
    PIK = ''
    op = input('Open save file "1", "2" or "3": ')
    if (op == '1'):
        PIK = 'data/file1.dat'
    elif (op == '2'):
        PIK = 'data/file2.dat'
    elif (op == '3'):
        PIK = 'data/file3.dat'
    try:
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
            c2Switch = data[8]
            c3Switch = data[9]
            branchSwitch = data[10]
            shill = data[11]
            inv = data[12]
            PKSwitch = data[13]
            mQuests = data[14]
            sQuests = data[15]
            alder = data[16]
            game_active = True
    except:
        print('Saved file not found!')

def menu():
    global menu_active, chapter, part, chapter1, tutorComp, game_active, switch, tutorialSwitch, c2Switch, c3Switch, shill, inv, PKSwitch, location
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
            inv = []
            shill = 0
            for i in PKSwitch:
                i = True
            #Story Switches
            for i in switch:
                i = False
            switch[0] = True
            for i in tutorialSwitch:
                i = True
            for i in c2Switch:
                i = True
            for i in c3Switch:
                i = True
            for i in branchSwitch:
                i = '0'
            for i in mQuests:
                i['accepted'] = False
                i['completed'] = False
                i['submitted'] = False
            for i in sQuests:
                i['accepted'] = False
                i['completed'] = False
                i['submitted'] = False
            #Alder Stats
            alder.name = 'Alder'
            alder.maxHealth = 60
            alder.health = alder.maxHealth
            alder.maxStamina = 60
            alder.stamina = alder.maxStamina
            alder.cLvl = 1
            alder.cExp = 0
            alder.baseAttack = 10
            alder.baseDefence = 10
            alder.baseSpeed = 5
            alder.baseEvasion = 5
            alder.head = armours[0]
            alder.body = armours[1]
            alder.legs = armours[3]
            alder.weapon1 = weapons[0]
            alder.weapon2 = weapons[0]
            #Start Game
            game()
        elif (action == 'l'):
            loadGame()
            if (game_active == True):
                #Start Game
                game()
        elif (action == 'q'):
            menu_active = False
menu()
quit()
