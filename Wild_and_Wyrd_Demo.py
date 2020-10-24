import os
import pickle
import random
#Loop
menu_active = True
game_active = True
tutorial1 = True
chapter1 = False
#Story Switches
chapter = '0'
part = '1'
tutorComp = False
switch = [True, False, False, False, False, False, False, False, False, False, False, False, False]
tutorialSwitch = [True, True, True, True, True, True, True]
c2Switch = [True, True, True, True, True]
c3Switch = [True, True, True, True, True]
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
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
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
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2,'\n'
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
        self.Exp = 5
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
            'attack' : 5, 'weight' : 1, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : 'bow', 'description' : 'A large bow made for practise.',
            'attack' : 10, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Wooden Sheild', 'type' : 'sheild', 'description' : 'A basic round wooden sheild.',
            'defence' : 20, 'weight' : 1, 'count' : 0}
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
          'recovers' : 2, 'count' : 0},
        {'itemId' : '4', 'name' : 'Mushroom', 'type' : 'food',
          'recovers' : 5, 'count' : 0},
        {'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : 'food',
          'recovers' : 10, 'count' : 0}
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0}
         ]
projec = [{'itemId' : '1', 'name' : 'Primative Arrow', 'type' : 'projectile',
           'weapon' : 'bow', 'damage' : 10, 'count' : 0},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : 'toss',
           'weapon' : 'none', 'damage' : 0, 'count' : 0}
          ]
ingre = [{'ingId' : '1', 'name' : 'Phantom moss', 'type' : 'ingredient', 'description' : 'A purplish moss that disappears at night',
          'count' : 0}
         ]
#Inventory
shill = 0
inv = []
PKSwitch = [True, True, True, True, True]

#Quests
mQuests = [{'questId':'1','client':'Florace','name':'Bug hunt', 'desc':'Collect two pieces of bug meat', 'reward' : '',
            'required':{'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : 'food'}, 'qnt' : 2,
            'accepted':False,'completed':False, 'submitted':False}
           ]
sQuests = [{'questId':'1','client':'Kyla','name':'Servents work', 'desc':['Clean fireplace:', 'Scrub caldron:', 'Grind phantom moss in mortar:'], 'reward' : '',
            'required':[False, False, False], 'qnt' : 1,
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
         {'actorId' : '5', 'name' : 'Jeb', 'species' : 'weasel', 'title' : 'Merchant'}
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
    print(p.cNext, ' ', p.cExp)
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
        sbl = []
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
    print('Shillings: ', shill)
#Recover health and stamina
def bed():
    alder.health = alder.maxHealth
    alder.stamina = alder.maxStamina
#Increment items
#Add a new item to the inventory if is is not already in there
def itemCount(item, amount):
    inInv = False
    for i in inv:
        if (item['type'] == 'weapon' and i['type'] == 'weapon'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'sheild' and i['type'] == 'sheild'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'bow' and i['type'] == 'bow'):
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
        elif (item['type'] == 'projectile' and i['type'] == 'projectile'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'toss' and i['type'] == 'toss'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'ingredient' and i['type'] == 'ingredient'):
            if (i['ingId'] == item['ingId']):
                item['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] += amount
        inv.append(item)

#Use Item
def useItem(p):
    use = []
    count = 1
    print('\nBag Items')
    for i in inv:
        if(i['type'] == 'healing' or i['type'] == 'food'):
            print(count, ': ', i['name'], ' x', i['count'])
            use.append(i)
            count += 1
    print('e - exit')
    if(count != 0):
        count = 1
        u = input('use item: ')
        for i in use:
            if (u == str(count)):
                print(i['name'])
                if (i['type'] == 'healing'):
                    p.health += i['heals']
                    print(p.name, ' recoved ', i['heals'], ' health')
                    if (p.health > p.maxHealth):
                        p.health = p.maxHealth
                elif (i['type'] == 'food'):
                    p.stamina += i['recovers']
                    print(p.name, ' recoved ', i['recovers'], ' stamina')
                    if (p.stamina > p.maxStamina):
                        p.stamina = p.maxStamina
                i['count'] -= 1
                if(i['count'] <= 0):
                    inv.remove(i)
            count +=1
        use.clear()

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
    for i in alder.special:
        i['active'] = False
        i['inEffect'] = 0
    alder.health = alder.maxHealth
    alder.stamina = alder.maxHealth
    print('\nAlder was slain.')
    cont()
    dostuff = False
#Hunder
def hunger():
    if(alder.stamina <= 0):
        alder.health -= 1
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
            if (impact <= 0):
                impact = 1
            if (p.cStatus == 'Blocking'):
                temp = impact
                impact -= b
                if (impact < 0):
                    impact = 0
                alder.cStatus = 'None'
            p.health -= impact
            print('\n',e.name,' attacked!')
            if(critical >= 90):
                print('Critical Hit!')
            print(p.name, ' took ', impact, ' damage!')
            return b
        else:
            print('\n',e.name,' Missed')
    else:
        print('\n',e.name, ' did not attack!')

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
            if (critical >= 90):
                impact += 10
            impact = round(impact * (100/(100 + e.defence())))
            if (impact <= 0):
                impact = 1
            e.health -= impact
            print('\n',p.name,' attacked!')
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
    for i in p.special:
        if (i['unlocked'] == True):
            print(i['spId'], ') ',i['name'], ' - ', i['cost'], ' stamina')
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
    count = 1
    print('\nBag Items')
    for i in inv:
        if(i['type'] == 'healing' or i['type'] == 'food'or i['type'] == 'projectile'or i['type'] == 'toss'):
            print(count, ': ', i['name'], ' x', i['count'])
            use.append(i)
            count += 1
    print('e - exit')
    if(count != 0):
        count = 1
        u = input('use item: ')
        for i in use:
            if (u == str(count)):
                #print(i['name'])
                if (i['type'] == 'healing'):
                    p.health += i['heals']
                    print(p.name, ' recoved ', i['heals'], ' health')
                    if (p.health > p.maxHealth):
                        p.health = p.maxHealth
                        alder.cStatus = 'Using'
                elif (i['type'] == 'food'):
                    p.stamina += i['recovers']
                    print(p.name, ' recoved ', i['recovers'], ' stamina')
                    if (p.stamina > p.maxStamina):
                        p.stamina = p.maxStamina
                        alder.cStatus = 'Using'
                elif (i['type'] == 'projectile'):
                    if (i['weapon'] == 'bow'):
                        if(p.weapon2['type'] == 'bow'):
                            if(p.ammo['loaded'] != True):
                                print('\n',i['name'],' loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                alder.cStatus = 'Using'
                            else:
                                print(i['name'],' already loaded!')
                        else:
                            print('Bow required!')
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
                        count += 1
                i['count'] -= 1
                if(i['count'] <= 0 and alder.cStatus == 'Using'):
                    inv.remove(i)
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
        hunger()
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
                        print('\nTo get more details about the enemy using the command "3" or "appraise" to get its current health and details about the enemy.')
                        count += 1
                    elif(count == 2):
                        print('\nIf you have an item use the command "5" or "item" to use it from you inventory.')
                    elif(count == 3):
                        print('\nTo reduce damage from a incoming attack use command "2" or "block"')
                    elif(count == 4):
                        print('\nTo deal damage to the opponent use command "1" or "attack".')
                elif (c2Switch[2] == False and c2Switch[3] == True):
                    print('\nTo use a ranged weapon like the bow select a the supported projectile in this case the primative arrow from items then on the next turn attack to fire it.')
                print('\n',alder.name)
                print("Health: ", alder.health, '/', alder.maxHealth, "| Stamina: ", alder.stamina, '/', alder.maxStamina)
                print("1) Attack     3) Appraise     5) Item")
                print("2) Block      4) Special      6) Flee")
                i = input('Action: ')
                if (i == '1' or i == 'attack' or i == 'Attack'):
                    print('\nEnemies')
                    alder.cStatus = 'Attacking'
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
                    if (i == 'y' or i == 'Y' or i == 'yes' or i == 'Yes'): 
                        alder.cStatus = 'Escaping'
                        for i in enemys:
                            if (i.speed() > alder.speed()):
                                print('Escape Failed!')
                            else:
                                fighting = False
            for i in enemys:
                if(i.health > 0):
                    if(i.strat == 'Attacker'):
                        print(i.health)
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
#Examine background object
def examine(location):
    global chapter, part
    print('\nExamine')
    if (location == '1'):
        print('The cottage kitchen contained various pots and pans hanging on the wall. It had a stove where a cauldron was dangled on a chain. There a cupboard and two tables one of which had an empty bowl on it. Alder had been washing dishes in a basin on the other table next to the window.')
        e = input('Examine: ')
        if (e == 'cauldron' or e == 'Cauldron'):
            if (sQuests[0]['accepted'] == True and sQuests[0]['required'][1] == False):
                print('Alder got a wet cloth and started rubbing the cauldren. Florace looked into the living room at Kyla and then went over to help him.')
                cont()
                print('Florace:')
                print('"Shh."')
                sQuests[0]['required'][1] = True
            else:
                print("It was a small metal cauldron above the stove suspended by a chain. It was empty right now.")
            cont()
        elif (e == 'cupboard' or e == 'Cupboard'):
            print('The Cupboard was full of plates, bowls and other kitchen and dining utensils.')
            cont()
        elif (e == 'bowl' or e == 'Bowl'):
            if (PKSwitch[0] == True):
                print('A large wooden bowl. It'"'"'s got hazelnuts in it.')
                pickup = input('Do you want to pick up the hazelnuts.(y/n)')
                if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                    print('\n5 Hazelnut(s) obtained')
                    itemCount(food[2], 5)
                    PKSwitch[0] = False
                    cont()
            else:
                print('A large wooden bowl. It'"'"'s empty.')
                cont()
        elif (e == 'basin' or e == 'Basin'):
            print('The basin Alder was washing was full of water and bits of leftover that Alder scraped off. Clean plates were next to it.')
            cont()
        elif (e == 'window' or e == 'Window'):
            if(tutorialSwitch[2] == True):
                print('Florace and Thay were talking on the other side of the window.')
                cont()
                print('Alder:')
                print('"I'"'"'m coming out"')
                cont()
                chapter = '1'
                tutorialSwitch[0] = False
            else:
                print('The clearing is out front.')
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
            if (sQuests[0]['accepted'] == True and sQuests[0]['required'][0] == False):
                print('Alder got to work cleaning the fireplace using a brush and cloth. In the end his arms were completely black.')
                cont()
                print('Kyla:')
                print('"Could you throw that ash outside."')
                cont()
                print('Kyla:')
                print('"If it gets on the floor you cleaning it up."')
                cont()
                sQuests[0]['required'][0] = True
            elif (sQuests[0]['required'][0] == False):
                print('The fireplace was unlit. It was used last night and still had ash and soot in it.')
                cont()
                print('Alder:')
                print('"I’ll clean it up later."')
                cont()
            else:
                print('The fireplace was unlit.')
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
            if (sQuests[0]['accepted'] == True and sQuests[0]['required'][2] == False):
                print('The purple moss must be what Kyla wants.')
                cont()
                count = 0
                for i in inv:
                    if (i['type'] == 'ingredient'):
                            if (i['ingId'] == '1'):
                                count += 1
                if (count == 0):
                    itemCount(ingre[0], 1)
                else:
                    print ('Alder already had some.')
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
            if (PKSwitch[2] == True):
                pickup = input('Do you want to pick up the blackberries.(y/n)')
                if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                    print('\n5 blackberries(s) obtained')
                    itemCount(food[0], 5)
                    PKSwitch[2] = False
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
                if (tutorialSwitch[3] == False):
                    pickup = input('Do you want to pick up the hunting knife.(y/n)')
                    if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                        print('\nHunting Knife obtained')
                        itemCount(weapons[2], 1)
                        PKSwitch[1] = False
                        cont()
            else:
                print('On the table was an unlit candle and a mortar and pestle')
                cont()
        elif (e == 'candle' or e == 'Candle'):
            print('The candle was placed in a candlestick. It was unlit.')
            cont()
        elif (e == 'mortar' or e == 'Mortar' or e == 'pestle' or e == 'Pestle'):
            if (sQuests[0]['accepted'] == True and sQuests[0]['required'][2] == False):
                for i in inv:
                    if (i['type'] == 'ingredient' and i['ingId'] == '1'):
                        print('Alder grinded the moss with the pestle until it was a purple powder. He then put it in a nearby pot containing the remnants of a similar powder.')
                        cont()
                        sQuests[0]['required'][2] = True
            else:
                print('A mortar and pestle were on the table.')
                cont()
                print('Florace recently used it to grind ingredients for potions.')
                cont()
        elif (e == 'knife' or e == 'Knife'):
            print('The knife was designed for hunting but it looks like someone has been using it to cut ingredients.')
            cont()
    elif (location == '5'):
        print('Sunlight entered the room easily through the curtainless window of Alder solitary and small bedroom which only contained a makeshift bed.')
        e = input('Examine: ')
        if (e == 'window' or e == 'Window'):
            print('The window lacked curtains and was small. Alder could see the sunlight breaching the branches of the WyrmWoods.')
            cont()
        elif (e == 'bed' or e == 'Bed'):
            print('It was cheaply made from dry wood and partridge feathers. It was powdered with herbs to stop it smelling. Alder made it with the help of Thay.')
            if (PKSwitch[4] == True):
                pickup = input("Amoung the feathers were Alder's savings. Pick them up?(y/n)")
                if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                    coins = random.randrange(+2,+3)
                    print('\n', coins,' shillings obtained')
                    shillings(coins)
                    PKSwitch[4] = False
                    cont()
            if ((tutorialSwitch[5] == False and tutorialSwitch[6] == True)  or (c2Switch[3] == False and c2Switch[4] == True)):
                sleep = input('Would you like to rest?(y/n)')
                if (sleep == 'y' or sleep == 'Y' or sleep == 'yes' or sleep == 'Yes'):
                    print('Alder got into his makeshift bed and drifted to sleep for the night.')
                    if (c2Switch[3] == False):
                        if(sQuests[0]['accepted'] == True and sQuests[0]['submitted'] == False):
                            ab = input('Abandon quests?(y/n)')
                            if (ab == 'y' or ab == 'Y' or ab == 'yes' or ab == 'Yes'):
                                sQuests[0]['accepted'] = False
                                print(sQuests[0]['name'],' abandoned!')
                                switch[7] = True
                                part = '3'
                                bed()
                        else:
                            switch[7] = True
                            part = '3'
                            bed()
                    else:
                        bed()
                        if(tutorialSwitch[6] == True):
                            tutorialSwitch[6] = False
                            part = '1'
                            switch[5] = True
                            chapter = '2'
                    cont()
    elif (location == '6'):
        print('The impossible fauna of the fairy realm had completely disappeared. This meant that Alder was now back in the normal realm of his origin. While he was in the fairy realm grass could not bend when he stepped on it and stone would not move no matter how hard he pulled but now he can interact with the world as he pleased. Near to where he was were some crickets, perfect for tonight’s meal.')
        e = input('Examine: ')
        if (e == 'sky' or e == 'Sky'):
            print('It was a bright, clear blue.')
            cont()
        elif (e == 'mushroom' or e == 'Mushroom'):
            if (PKSwitch[3] == True):
                print('There was a variety of late-summer mushrooms around the area. Many of which are edible.')
                cont()
                pickup = input('Do you want to pick up the mushrooms.(y/n)')
                if (pickup == 'y' or pickup == 'Y' or pickup == 'yes' or pickup == 'Yes'):
                    print('\n3 mushrooms(s) obtained')
                    itemCount(food[3], 3)
                    PKSwitch[3] = False
            else:
                print('There was a variety of late-summer mushrooms around the area. Some circled the area as part of the spell need to go between the realms. Alder knew better than to pick these.')
                cont()
        elif (e == 'plants' or e == 'Plants'):
            print('Various weeds, wildflowers and moss.')
            cont()
        elif (e == 'trees' or e == 'Trees'):
            print('Various trees made up the woodland, the most frequent were birch, rowen and holly.')
            cont()
        elif (e == 'rocks' or e == 'Rocks' or e == 'boulder' or e == 'Boulder'):
            print('There were a few boulders in the area. There was a large one were the cottage was.')
            cont()
        elif (e == 'cottage' or e == 'Cottage'):
            print('The cottage was gone from sight. Replace with a large boulder.')
            cont()
        elif (e == 'cricket' or e == 'Cricket' or e == 'crickets' or e == 'Crickets'):
            if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False):
                print('Some large brown crickets were in the area.')
                cont()
                fight = input('Do you want to fight them.(y/n)')
                if (fight == 'y' or fight == 'Y' or fight == 'yes' or fight == 'Yes'):
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
                        print('Alder tried but in vain to get the cricket which had already jumped out of reach.')
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
                    tutorialSwitch[5] = False
                    print('The hornets were twitching but Alder knew they were dead.')
                    cont()
                    print('Alder:')
                    print('"Did I anger them?"')
                    cont()
                    print('Alder was still puzzled by the attack but regardless it was time to return.')
                    cont()
            else:
                print('The other crickets had fled.')
    elif (location == '7'):
        if(c2Switch[4] == True):
            print('Large trees surrounded him in a neat circle like pillars; the branches formed a mosaic ceiling. There was a light from an unknown source that shone in the center in front of Alder.')
        else:
            print('The mouse was holding the sword'"'"'s hilt to Alder'"'"'s hand while ghostly spectors watch.')
        e = input('Examine: ')
        if(e == 'trees' or e == 'Trees' or e == 'pillars' or e == 'Pillars'):
            print('Giant trees formed a perfect circle around the clearing like pillars.')
        elif(e == 'ceiling' or e == 'Ceiling' or e == 'mosaic' or e == 'Mosaic'):
            print('The ceiling was covered in various different leaves such as oak, cider, alder and many others which Alder did not recognise, their branches were curved so the whole was a spiralling mosaic.')
        elif(e == 'light' or e == 'Light'):
            print('From the centre of the clearing a misty light hung from an unspecifiable source like water from a fountain. It illuminated the area as far as the trees.')            
            if(c2Switch[4] == True):
                switch[8] = True
                part = '4'
        elif(c2Switch[4] == False):
            if(e == 'sword' or e == 'Sword'):
                print('The sword was a double edge and was dark green with silver decorations on the hilt and scabbard. Now that it was close Alder could see what looked like a thorny stem engraved around the grip, the rain-guard was shaped to resemble leaves and the pommel from Alder’s angle was tear-shaped. The scabbard was a dark green and it had a rounded slot carved into it.')
                cont()
                sword = input('Take the sword!(y/n)')
                if(sword == 'y' or sword == 'Y' or sword == 'yes' or sword == 'Yes'):
                    switch[9] = True
                    part = '5'
            elif(e == 'ghosts' or e == 'Ghosts' or e == 'spectors' or e == 'Spectors'):
                print('The ghostly specters lingered within the darkness between the trees. Every creature of Albion imaginable was there.')

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
                    print('"Hold still I'"'"'l help fix you up."')
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
                    print('Madam Kyla was relaxed in her chair with her nose in a red book titled "An sorcerers guide to Dragons and Wyverns". She peered from the book to her servent.')
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
                    print('"I need you to grind some phantom moss."')
                    cont()
                    print('Kyla:')
                    print('"Just so we are clear!"')
                    cont()
                    print('Kyla:')
                    print('" It'"'"'s the purple moss that can be found outside!"')
                    cont()
                    print('Kyla:')
                    print('"Use the mortar in the shed to grind it into dust!"')
                    cont()
                    print('Kyla:')
                    print('"And put the dust it in the pot on the far end!"')
                    cont()
                    print('Kyla:')
                    print('"That should keep you busy for the rest of the day!"')
                    cont()
                    i = input('Do you accept this labour?(y/n):')
                    if(i == 'y' or i == 'Y' or i == 'yes' or i == 'Yes'):
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
                        print('"If you don'"'"'t work I will freeze you in place for a week!"')
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
                        print('"Clean the fire place, scrub the cauldren and grind the moss."')
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
                    else:
                        print('Kyla:')
                        print('"I have no futher need for you."')
                        cont()
                        print('Kyla:')
                        print('"Do as you please."')
                        cont()
        
        elif (tutorialSwitch[6] == False and c2Switch[0] == True and chapter == '2'):
            print('1: Florace')
            t = input('talk to: ')
            if (t == '1'):
                print('Alder:')
                print('"Florace!"')
                cont()
                print('Alder:')
                print('"Trissie'"'"'s here!"')
                cont()
                print('Alder:')
                print('"Trissie'"'"'s here!"')
                cont()
                print('Florace:')
                print('"Claim done Alder."')
                cont()
                print('Florace:')
                print('"I’ll let Kyla know. You go out and greet her."')
                cont()
                print('Florace:')
                print('"You go out and greet her."')
                cont()
                print('Alder:')
                print('"Yes Florace!"')
                cont()
                c2Switch[0] = False
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
                            print('"Well there are two realms in Avalon."')
                            cont()
                            print('Florace:')
                            print('"The world of fairies and magical monsters that we called the Wyrd and the world of men, mice and such that the fairies call the Wild."')
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
                            print('"It’s not entirely accurate but we tend to call this place the burrow since it cannot be seen from the Wild."')
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
                    tutorialSwitch[3] = False
                    tutorial1 = False
            elif (tutorialSwitch[4] == True):
                print('1: Florace')
                t = input('talk to: ')
                if (t == '1'):
                    dialog = [False]
                    while(dialog[0] == False):
                        print('Florace:')
                        print('"The knife should be in the shed. I'"'"'ll let you out once you'"'"'ve got it."')
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
                                print('"I'"'"'ll send you out of the Wyrd."')
                                cont()
                                print('Florace:')
                                print('"When you have some meat, I'"'"'ll let you back in."')
                                cont()
                                print('Florace:')
                                print('"Just please don'"'"'t go too far."')
                                cont()
                                location = '6'
                                print('Florace waved her hands a bright light and smoke appeared in them. Light shone from several points around circling the cottage which then turned into a boulder. Florace and Thay were gone from sight.')    
                                cont()
                                dialog[0] = True
                            if (c == '2'):
                                dialog[1] = True
        elif(chapter == '2'):
            if (c2Switch[0] == True):
                print('1: Squirrel')
                t = input('talk to: ')
                if (t == '1'):
                    print('The squirrel could not see Alder. He needed to let either Florace or Kyla to let her in.')
            elif (c2Switch[1] == True):
                print('1: Trissie')
                t = input('talk to: ')
                if (t == '1'):
                    print('Alder:')
                    print('"Hi Trissie!"')
                    cont()
                    print('Trissie:')
                    print('"Please don'"'"'t stand next to me when Miss Kyla is letting me in Alder!"')
                    cont()
                    print('Alder:')
                    print('"Oh!"')
                    cont()
                    print('Alder:')
                    print('"Sorry Triss."')
                    cont()
                    print('Alder found Trissie fun to be around but it sounded like she was in a hurry. He could not help but feel dejected by her hast.')
                    cont()
                    print('Alder:')
                    print('"Ok."')
                    cont()
                    print('Trissie:')
                    print('"Aw."')
                    cont()
                    print('Trissie:')
                    print('"Don’t make that face."')
                    cont()
                    print('Trissie:')
                    print('"Say?"')
                    cont()
                    print('Trissie:')
                    print('"Why don'"'"'t I give you some archery lessons before I leave?"')
                    cont()
                    print('As Alder brightens up at the thought. But those emotions were cut when Trissie mumbled ')
                    cont()
                    print('Trissie:')
                    print('"You might need them."')
                    cont()
                    print('Florace:')
                    print('"Triss!"')
                    cont()
                    print('Florace was staring from the entrance of the cottage door. She went back in with Trissie.')
                    cont()
                    c2Switch[1] = False
            elif (c2Switch[2] == False and c2Switch[3] == True):
                print('1: Trissie')
                t = input('talk to: ')
                if (t == '1'):
                    print('Trissie quickly set up a makeshift dummy out of leaves, sticks and a cheaply made old burlap sack that was intended for foraging. She then planted it into the ground so it would stand upright. The finished product was crude and clearly rushed and resembled a sack on a stick with leaves coming out of the openings.')
                    cont()
                    print('Trissie:')
                    print('"That'"'"'ll do."')
                    cont()
                    print('Trissie:')
                    print('"Alder, wait there."')
                    cont()
                    print('Trissie goes into the shed, looks around and finds a bow and some arrows set aside for hunting. Alder thought she looked a little silly as she was dragging the bow which was big even for Alder, that was because the bow was originally meant for Florace but she never used it finding herself unskilled with it. Trissie brought them to Alder.')
                    cont()
                    alder.weapon2 = weapons[3]
                    print('\nTraining bow equiped')
                    itemCount(projec[0], 5)
                    print('\n5 Primative arrows obtained')
                    print('Trissie:')
                    print('"Now set the arrow in the bow, take aim and fire."')
                    cont()
                    print('Trissie:')
                    print('"Let'"'"'s begin."')
                    cont()
                    battle([Dummy(), Null(), Null()])
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
                            print('"and because I helped a human, he did this to me."')
                            cont()
                            dialog[0] = True
                        elif (c == '2'):
                            print('Trissie:')
                            print('"I’m not easy to capture but you must be careful and survive."')
                            cont()
                            print('Trissie:')
                            print('"Then I am sure we will meet again."')
                            cont()
                            dialog[1] = True
                    print('As soon as Florace let her out, Trissie went towards the nearest tree and in an instant climbed up it and disappeared among the branches. It was as if she vanished. There was not even a rustle of leaves.')
                    cont()
                    print(' Alder returned to the cottage a little disappointed with Trissie gone so soon. But he had work to do and he set about his remaining chores.')
                    cont()
                    c2Switch[3] = False
                    
#Move to another location
def move():
    global location, part, tutorial1, tutorialSwitch, c2Switch
    print('\nMove')
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
        m = input('Move to: ')
        if (m == '1' or m == 'kitchen' or m == 'Kitchen'):
            location = '1'
            print('Alder moved to the kitchen.')
            alder.stamina -= 1    
            cont()
        elif (m == '2'):
            location = '3'
            print('Alder moved outside the cottage through the front door.')
            alder.stamina -= 1
            cont()
            if(tutorialSwitch[1] == True and chapter == '1'):
                part = '2'
                tutorialSwitch[1] = False
                switch[1] = True
                tutorial1 = False
            elif (c2Switch[0] == False and c2Switch[1] == True and chapter == '2'):
                print('As soon as Alder left for the outside we went straight towards Trissie. He impatiently waited as the squirrel drew nearer to the house repeating chanting the secret phrase over and over while the other three men had also left the cottage to greet her. After a short while, Kyla finally appeared in the window and waved her hand. Trissie turned to face Alder and jumped back with shock.')
                cont()
                print('Trissie:')
                print('"AHHH!"')
                cont()
        elif (m == '3'):
            location = '5'
            print('Alder moved upstairs and into his bedroom.')
            alder.stamina -= 1    
            cont()
    elif (location == '3'):
        print('1: Living Room')
        print('2: Shed')
        print('3: Leave cottage')
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
            elif (c2Switch[1] == False and c2Switch[2] == True):
                location = '2'
                print('Alder moved to the living room of the cottage.')
                alder.stamina -= 1
                switch[6] = True
                part = '2'
                c2Switch[2] = False
            else:
                location = '2'
                print('Alder moved to the living room of the cottage.')
                alder.stamina -= 1    
                cont()
        elif (m == '2'):        
            location = '4'
            print('Alder moved to the shed on the side of the cottage.')  
            alder.stamina -= 1  
            cont()
        elif (m == '3'):
            print('Alder once got lost after he strayed too far from the cottage.')
            cont()
            print('He spend hours in the dark until Florace found him crying and scared.')
            cont()
            print('Kyla was indifferent to the situation.')
            alder.stamina -= 1
            cont()
    elif (location == '4'):
        print('1: Outside')
        m = input('Move to: ')
        if (m == '1'):
            location = '3'
            print('Alder left the shed and back to the front of the cottage.')
            alder.stamina -= 1
            cont()
    elif (location == '5'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            print('Alder went down stairs into the living room.')
            alder.stamina -= 1
            cont()
    elif (location == '6'):
        print('1: Cottage grounds')
        m = input('Move to: ')
        if (m == '1'):
            location = '3'
            if(tutorialSwitch[5] == False):
                print('Alder:')
                print('"Florace! I'"'"'m done!"')
                cont()
            print('The air rippled and the cottage reappeared.')
            cont()
            if(tutorialSwitch[5] == False):
                print('Florace:')
                print('"Alder I saw the hornets attacking, are you ok!"')
                cont()
                print('Alder:')
                print('"Um!?"')
                cont()
                print('Alder:')
                print('"I got stung a few times but i'"'"'m alright!"')
                cont()
                print('Florace:')
                print('*Sigh*')
                cont()
                print('Florace:')
                print('"Give the bugs and the knife to me and go relax yourself."')
                cont()
                print('Alder passed the bug meat and the hunting knife over to her. Florace went inside the cottage to place the crickets most likely in the kitchen for supper. Thay came up to him. He looked ready to go.')
                for i in inv:
                    if (i['type'] == 'food'):
                        if (i['itemId'] == '5'):
                            inv.remove(i)
                alder.weapon1 = weapons[0]
                print('\nHunting Knife unequiped')
                cont()
                mQuests[0]['submitted'] = True
                print('Quest Complete')
                cont()
                part = '4'
                switch[4] = True
            alder.stamina -= 1
    elif (location == '7'):
        print('Alder could not move.')
#Save the game
def save(location, chapter, part):
    data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, shill, inv, PKSwitch, mQuests, sQuests, alder]
    print (location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, shill, inv, PKSwitch, mQuests, sQuests, alder)
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
        print('2: Use')
        print('3: Equip')
        print('e - Exit')
        i = input('Action: ')

        #Appraise items in inventory
        if (i == '1' or i == 'appraise' or i == 'Appraise'):
            appraise = input('\nItem number: ')
            count = 1
            for i in inv:
                if (appraise == str(count)):
                    if (i['type'] != 'food'):
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nDescription: ', i['description'])
                    else:
                        print('Name: ', i['name'], ' - Type: ', i['type'], ' - \nStamina Recovered: ', i['recovers'])
                count += 1
        elif (i == '2' or i == 'use' or i == 'Use'):
            useItem(alder)
        elif (i == '3' or i == 'equip' or i == 'Equip'):
            equip()
        elif (i == 'e'):
            print()
            bag = False
    
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
            if (q['questId'] == '1'):
                count = 0
                for i in q['required']:
                    if (i == True):
                        count += 1
                if (count == len(q['required'])):
                    q['completed'] = True
                    
#Print the objectives
def objective():
    print("\nObjectives")
    print("Main:")
    if(tutorialSwitch[0] == True):
        print('\tYou will need to have a quick look around. Type "examine" or "e" to explore the room Alder is currently in.')
    elif(tutorialSwitch[1] == True):
        print('\tAlder needs to go outside. He will have to "move"("m") through the living room and then outside.')
    elif(tutorialSwitch[2] == True):
        print('\tTalk(t) to Florace.')
    elif(tutorialSwitch[3] == True):
        print('\tTalk(t) to Thay.')
    elif(tutorialSwitch[4] == True):
        print('\tExamine table in shed, pick up knife and equip(x) in main weapons.')
    for q in mQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            if (q['questId'] == '1'):
                if(alder.weapon1['wpId'] != '2'):
                    print('Pick up and equip hunting knife.')
                else:
                    amount = 0
                    for i in inv:
                        if (i['type'] == 'food'):
                            if (i['itemId'] == '5'):
                                amount += i['count']
                    print('\t', q['desc'],' (',amount,'/',q['qnt'],')')
    print("Side:")
    for q in sQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            if (q['questId'] == '1'):
                j = 0
                for i in q['desc']:
                    print('\t',i, q['required'][j])
                    j += 1
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
    print("Ranged Weapons: To use a ranged weapon select a projectile from items then on the next turn attack to fire.")
    print("Throwing Items: Items such as nets can be thrown ")
    print("Order of combat: Fastest combatant.")

def free(location, chapter, part):
    global game_active, tutorial1
    hunger()
    achive()
    print('\nInteract')
    if(tutorialSwitch[0] == True):
        print('You will need to have a quick look around. Type "examine" or "e" to explore the room Alder is currently in.')
    elif(tutorialSwitch[1] == True):
        print('Alder needs to go outside. He will have to "move"("m") through the living room and then outside.')
    elif(tutorialSwitch[2] == True):
        print('While we wait for Thay Let'"'"'s "talk"("t") to Florace.')
    elif(tutorialSwitch[3] == True):
        print('Alder'"'"'s job around the cottage is to entertain guests. Let'"'"'s talk to Thay now.')
    elif(tutorialSwitch[4] == True):
        print('Alder will need the knife in the shed examine the area to find and pick up the knife and "equip"("x") the knife from your "items"("i") inventory.')
    elif(tutorialSwitch[5] == True):
        print('Find an opponent to fight. There will be six options available for each turn. Type "h2", "help2" or "Help2" for more details.')
    elif(tutorialSwitch[6] == True):
        print('Return to the cottage and bring an end to the day and the tutorial.')
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
        inventory()
    elif (action == 'x' or action == 'equip' or action == 'Equip'):
        equip()
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
    global switch, tutorial1, location, chapter, part, location
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
                print('"I need you to go to find an insect or two and bring it back for supper."')
                cont()
                print('Alder:')
                print('"Ok."')
                cont()
                mQuests[0]['accepted'] = True
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
                switch[3] = False
            elif (switch[4] == True and part == '4'):
                print('Thay:')
                print('"I’m heading off now lad."')
                cont()
                print('Alder:')
                print('"Already!"')
                cont()
                print('Alder:')
                print('"Well, take care than."')
                cont()
                print('Thay:')
                print('"I will."')
                cont()
                print('Thay:')
                print('"Goodbye lad."')
                cont()
                print('And with that, the hedgehog left. Leaving the burrow for lands unknown to Alder. He headed back to the cottage. Back to his daily chores of cleaning, gathering and grinding leaves until his hands were sore. As the day came to an end the residents of the cottage were unaware of the shadows that came ever closer.')
                cont()
                switch[4] = False
            free(location, chapter, part)
        if (chapter == '2'):
            if (switch[5] == True and part == '1'):
                print('\nChapter 2')
                print('Dawn came, sunlight striking Alder’s face through the curtainless window. He began his day like normal, going downstairs to eat his breakfast of nuts and berries scavenged from the foot of trees and bushes, then clean the plates and cups using water gathered from rain or the nearest point of the river. The day was set to be a very mundane one, where Alder could only hope that a guest would come, just as Thay did the day before. Otherwise, today he will only be sweeping floors, chopping wood and foraging mushrooms allowing the hours tick by until it was time for the next chore.')
                cont()
                print('Alder:')
                print('*Yawn*')
                cont()
                print('The dull boredom was broken to Alder excitement when a squirrel he knew came down from the trees and ran into the area with the cottage. The squirrel was female but wore male clothing, strapped to her back was a bow and quiver and the tip half of her tail missing. She spoke to her surroundings in a loud whisper.')
                cont()
                print('Squirrel:')
                print('"The rabbit seeks his burrow!"')
                cont()
                print('Squirrel:')
                print('"The rabbit seeks his burrow!"')
                cont()
                print('She was trying to get into the burrow, Alder needed to let someone know about the guest.')
                cont()
                location = '3'
                switch[5] = False
            elif (switch[6] == True and part == '2'):
                print('Trissie had rested her bow and quiver on the wall and hopped onto one of the chairs on the table. Kyla was opposite her in her rocking chair while everyone else stood around the table as spectators. Alder walked over to take position next to Florace. With everyone gathered Trissie began.')
                cont()
                print('Trissie:')
                print('"I’ll make this quick!"')
                cont()
                print('Trissie:')
                print('"There are Gowl knights patrolling these woods!"')
                cont()
                print('Kyla and Florace sat upright and began muttering to each other.')
                cont()
                print('Florace:')
                print('"Do you think they know of the cottage?"')
                cont()
                print('Kyla:')
                print('"Not unless one of our clients has sold us out."')
                cont()
                print('Kyla:')
                print('"Even so their search shall come up empty."')
                cont()
                print('Trissie:')
                print('"I don’t know. "')
                cont()
                print('Trissie:')
                print('"There'"'"'s quite a few of them and they are setting up camps."')
                cont()
                print('Trissie:')
                print('"They seemed certain that they would find something."')
                cont()
                print('Kyla:')
                print('"My magic is strong."')
                cont()
                print('Kyla:')
                print('"They’ll never find this place."')
                cont()
                print('Trissie:')
                print('"I hope so."')
                cont()
                print('Trissie:')
                print('"Anyway, the woods are full of soldiers, most of whom appear to be new recruits"')
                cont()
                print('Kyla:')
                print('"That proves my point!"')
                cont()
                print('Kyla:')
                print('"Whatever they know, their sending saplings, they cannot be very confident about it!"')
                cont()
                print('Trissie:')
                print('"Being overseen by several captains apparently ordered by Darrunt himself!"')
                cont()
                print('The mood dimmed but Kyla remained confident. Alder had rarely been involved in conversations about the dangers of the outside world and was unsure how to feel. He whispered to Florace as Kyla dismissed Trissie’s warning.')
                cont()
                print('Alder:')
                print('"Who’s Darrunt?"')
                cont()
                print('Florace:')
                print('"He is the leader of the Gowls."')
                cont()
                print('Florace:')
                print('"He is known for hating humans more than anything."')
                cont()
                print('Florace:')
                print('"If he found us then we would be as good as dead."')
                cont()
                print('While Alder and Florace whispered to each other Kyla had relaxed back into her chair at the end of her rebuttal.')
                cont()
                print('Kyla:')
                print('"We’ll lay low for the next few days, we are well stocked and have enough water to last us a few days."')
                cont()
                print('Kyla:')
                print('"Thank you for your warnings, Trissie dear."')
                cont()
                print('Kyla:')
                print('"But I think we will be fine."')
                cont()
                print('Trissie:')
                print('"If you say so."')
                cont()
                print('Trissie:')
                print('"I think I’ll scarper out of these woods for the time being until things quiet down."')
                cont()
                print('Trissie:')
                print('"Alder?"')
                cont()
                print('Trissie:')
                print('"I promised you archery lessons?"')
                cont()
                print('Alder:')
                print('"Yes."')
                cont()
                print('Trissie:')
                print('"Then meet me outside."')
                cont()
                print('Trissie leaves through the front door. From inside the cottage, Alder could see her picking up a large stick and sticking it into the ground.')
                cont()
                c2Switch[2] = False
                switch[6] = False
            elif (switch[7] == True and part == '3'):
                print('After a while, the light of day dimmed as the sky turned orange signifying the day was coming to an end. Alder wondered if Thay and Trissie got away all right. The three residents of the cottage had roasted hornet for supper.')
                cont()
                print('Alder returns to his bed unaware that this would be his last time in it and that his life would never again be the same as it had been. Change is inevitable whether or not you want or even expect it.')
                cont()
                print('Alder:')
                print('"........."')
                cont()
                print('Alder:')
                print('"................hm?"')
                cont()
                print('Alder:')
                print('"Wha...?"')
                cont()
                print('Alder wakes in an empty clearing.')
                cont()
                location = '7'
                switch[7] = False
            elif (switch[8] == True and part == '4'):
                print('Countless ghostly figures appear from the darkness between the trees. All of them were creatures of the woodlands from mice to wolves. But there were no humans among them.')
                cont()
                print('The ground in front of Alder started to burst up and a bulky mouse wearing a metal chest plate and a belt which was attached to a red cloth covering his waist, it held a sword by his right side. Despite being nearly half the size of Alder'"'"'s leg, Alder was still intimidated. His face was that of a seasoned warrior, with the agile yet strong figure by mouse standards at least.')
                cont()
                print('The mouse walked up to Alder until he was standing right in front of him staring him directly in his eyes. In surreality only possible in dreams the mouse picked Alder up and took him over to the hole where he had emerged from. Alder was still surprised by his however and panicked but something was stopping him from moving how he wanted.')
                cont()
                print('Alder:')
                print('"Wait!"')
                cont()
                print('Alder:')
                print('"What’s happening!?"')
                cont()
                print('Alder:')
                print('"What are you doing!?"')
                cont()
                print('The mouse gently placed Alder in the hole and carefully reset the soil until Alder’s body was submerged in the soil with his head and hands sticking out at the surface.')
                cont()
                print('The mouse then grabbed the handle of his sword with his right paw and pulled it out. It looked as sharp and the metal shone like a star. Alder thought for a second that he was going to use the sword to cut him.')
                cont()
                print('Alder:')
                print('"Ahh!"')
                cont()
                print('The mouse’s expression displayed surprise and then an apologetic head scratch conveyed that he did not mean any harm, he pulled out the scabbard and fitted the sword back into it and placed the hilt in Alder’s hand.')
                cont()
                c2Switch[4] = False
                switch[8] = False
            elif (switch[9] == True and part == '5'):
                print('Alder took the sword by the grip, to his surprise, it grew in size to fit in his hand. Feeling the sword he found it surprisingly light and was comforting to hold as though it was always meant to be in his grasp.')
                cont()
                print('Turning the sword over Alder found another slot the same as the other side.')
                cont()
                print('???:')
                print('"..."')
                cont()
                print('The mouse said nothing, only smiled, he beckoned Alder to kneel. Alder compiled and the mouse patted him on his shoulders as he nodded his head and closed his eyes and continued burning Alder. He was still silent but Alder had a strange sensation of a voice in his head saying to him...')
                cont()
                print('Good luck. My Scion.')
                cont()
                chapter = '3'
                part = '1'
                switch[9] = False
                switch[10] = True
                part = '1'
            free(location, chapter, part)
        if (chapter == '3'):
            if (switch[10] == True and part == '1'):
                location = '5'
                print('\nChapter 3')
                switch[10] = False
            free(location, chapter, part)

def loadGame():
    global location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, shill, inv, PKSwitch,mQuests,sQuests,alder
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
        shill = data[10]
        inv = data[11]
        PKSwitch = data[12]
        mQuests = data[13]
        sQuests = data[14]
        alder = data[15]

def menu():
    global menu_active, chapter, part, chapter1, tutorComp, game_active, switch, tutorialSwitch, c2Switch, shill, inv, PKSwitch
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
            PKSwitch = [True, True, True, True, True]
            #Story Switches
            switch = [True, False, False, False, False, False, False, False, False, False, False, False, False]
            tutorialSwitch = [True, True, True, True, True, True, True]
            c2Switch = [True, True, True, True, True]
            for i in mQuests:
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
            alder.head = armors[0]
            alder.body = armors[1]
            alder.legs = armors[3]
            alder.weapon1 = weapons[0]
            alder.weapon2 = weapons[0]
            #Start Game
            game()
        elif (action == 'l'):
            game_active = True
            loadGame()
            #Start Game
            game()
        elif (action == 'q'):
            menu_active = False
menu()
quit()
