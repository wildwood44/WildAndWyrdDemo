import os
import pickle
import random
from data import typeSpf
from data import playableChars
from data import enemyUnits
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
#enumerated classes
SpecialType1 = typeSpf.SpecialType1
SpecialType2 = typeSpf.SpecialType2
AttackType = typeSpf.AttackType
SpellType = typeSpf.SpellType
CombatStatus = typeSpf.CombatStatus
ArmourType = typeSpf.ArmourType
Weapon1Type = typeSpf.Weapon1Type
Weapon2Type = typeSpf.Weapon2Type
ItemType = typeSpf.ItemType
        
Florace = {'pId' : '2', 'name' : 'Florace', 'combatLvl' : '1', 'combatExp' : 0,
         'maxHealth': 150, 'attack' : 15, 'defence' : 10, 'speed' : 7, 'evasion' : 2, 'maxStamina' : 100,
         'head' : 'None', 'body' : 'Apprentice Witch Shirt', 'legs' : 'Apprentice Witch Dress', 'weapon1' : 'None', 'weapon2': 'None'
         }
party = [{'pId' : '1', 'name' : 'Alder', 'title' : 'Servant', 'species' : 'Human', 'inParty' : True},
         {'pId' : '2', 'name' : 'Florace', 'title' : 'Gaurdian', 'species' : 'Human', 'inParty' : False},
         {'pId' : '3', 'name' : 'Dean', 'title' : 'Watch Squire', 'species' : 'Water Shrew', 'inParty' : False}
         ]
#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : Weapon1Type.sword, 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0, 'priority': 3},
           {'wpId' : '1', 'name' : 'Lief', 'type' : Weapon1Type.sword, 'description' : 'Legendary sword of the Scion.',
            'attack' : 100, 'weight' : 5, 'count' : 0, 'priority': 3},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : Weapon1Type.dagger, 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0, 'priority': 3},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : Weapon2Type.bow, 'description' : 'A large bow made for practice.',
            'attack' : 20, 'weight' : 2, 'count' : 0, 'priority': 4},
           {'wpId' : '1', 'name' : 'Wooden Sheild', 'type' : Weapon2Type.shield, 'description' : 'A basic round wooden shield.',
            'defence' : 20, 'weight' : 1, 'count' : 0, 'priority': 4}
           ]

armours = [{'armId' : '1', 'name' : 'None', 'type' : ArmourType.hat, 'description' : '',
          'defence' : 0, 'weight' : 0, 'count' : 0, 'priority': 5},
          {'armId' : '1', 'name' : 'Old Tunic', 'type' : ArmourType.shirt, 'description' : 'An old shirt with holes in it.',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 6},
          {'armId' : '2', 'name' : 'Travelling Cloak', 'type' : ArmourType.shirt, 'description' : 'A too large black cloak. Good for keeping ou of sight but heavy.',
          'defence' : 10, 'weight' : 10, 'count' : 0, 'priority': 6},
          {'armId' : '1', 'name' : 'Worn Trousers', 'type' : ArmourType.trousers, 'description' : 'An old pair of trousers long past their prime',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 7}
          ]
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : ItemType.food,
          'recovers' : 2, 'count' : 0, 'priority': 1},
        {'itemId' : '4', 'name' : 'Mushroom', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : ItemType.food,
          'recovers' : 10, 'count' : 0, 'priority': 1},
        {'itemId' : '6', 'name' : 'Brown Bread', 'type' : ItemType.food,
          'recovers' : 50, 'count' : 0, 'priority': 1}
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : ItemType.healing, 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0, 'priority': 2}
         ]
projec = [{'itemId' : '1', 'name' : 'Primitive Arrow', 'type' : ItemType.projectile, 'description' : 'Arrows made from readily available materials.',
           'weapon' : Weapon2Type.bow, 'damage' : 10, 'count' : 0, 'priority': 8},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : ItemType.toss,  'description' : 'A rope net to catch your enemies.',
           'weapon' : 'none', 'damage' : 0, 'count' : 0, 'priority': 9}
          ]
ingre = [{'ingId' : '1', 'name' : 'Bramble leaves', 'type' : ItemType.ingredient, 'description' : 'The leaves of a blackberry bush',
          'count' : 0, 'priority': 10}
         ]
#Inventory
shill = 0
inv = []
PKSwitch = [True, True, True, True, True, True]

#Quests
mQuests = [{'questId':'1','client':'Florace','name':'Bug hunt', 'desc':'Collect two pieces of bug meat', 'reward' : '', 'rewardCount' : 0,
            'type':'collect', 'required':{'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : ItemType.food}, 'qnt' : 2,
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
#Universal Specials
manuvers = [{'spId':'1','name':'Advence', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
           {'spId':'2','name':'Retreat', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
           ]
spells = []
combinations = []
#Location
locations = [{"locId" : "1", "name" : "Cottage Kitchen"},
             {"locId" : "2", "name" : "Cottage Living Room"},
             {"locId" : "3", "name" : "Cottage Clearing"},
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
data = [location, chapter, part, tutorial1, tutorComp, chapter1, switch, tutorialSwitch, c2Switch, c3Switch, branchSwitch, shill, inv, PKSwitch, mQuests, sQuests]

#Set Class
alder = playableChars.Alder()

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
                print(count,': ', i['name'], ' stat increaced by ', i['boost'])
                count += 1
            elif (i['No'] == '2' and i['active'] == False and temp == True):
                print(count,': ', i['name'], '  stat increaced by  ', i['boost'])
                count += 1
            elif (i['No'] == '3' and i['active'] == False and temp == True):
                print(count,': ', i['name'], '  stat increaced by  ', i['boost'])
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
        for i in p.abilities:
            if (i['unlocked'] == False):   
                print(count,': ', i['name'], ' - ', i['effect'])
                count += 1
        sa = input('Boost: ')
        count = 1
        for i in p.abilities:
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
        if (item['type'] == Weapon1Type.sword and i['type'] == Weapon1Type.sword or
            item['type'] == Weapon1Type.dagger and i['type'] == Weapon1Type.dagger or
            item['type'] == Weapon1Type.spear and i['type'] == Weapon1Type.spear or
            item['type'] == Weapon1Type.axe and i['type'] == Weapon1Type.axe or
            item['type'] == Weapon1Type.mace and i['type'] == Weapon1Type.mace or
            item['type'] == Weapon1Type.staff and i['type'] == Weapon1Type.staff):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.shield and i['type'] == Weapon2Type.shield):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.bow and i['type'] == Weapon2Type.bow):
            if (i['wpId'] == item['wpId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.crossbow and i['type'] == Weapon2Type.crossbow):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.sling and i['type'] == Weapon2Type.sling):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.shield and i['type'] == Weapon2Type.shield):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.wand and i['type'] == Weapon2Type.wand):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ArmourType.hat and i['type'] == ArmourType.hat):
            if (i['armId'] == item['armId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ArmourType.shirt and i['type'] == ArmourType.shirt):
            if (i['armId'] == item['armId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ArmourType.trousers and i['type'] == ArmourType.trousers):
            if (i['armId'] == item['armId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.food and i['type'] == ItemType.food):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.healing and i['type'] == ItemType.healing):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.projectile and i['type'] == ItemType.projectile):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.toss and i['type'] == ItemType.toss):
            if (i['itemId'] == item['itemId']):
                i['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.ingredient and i['type'] == ItemType.ingredient):
            if (i['ingId'] == item['ingId']):
                i['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] = amount
        inv.append(item)
    inv.sort(key=itemLister, reverse=False)

#The item should be equipped
#If the item is not starting clothing then it should be return to the inventory
#Only items of speciec type can be equipped
def equip(p):
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
                if(i['type'] == ArmourType.hat):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.head['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equipped')
                        if(alder.head['armId'] != '0'):
                            inv.append(p.head)
                        p.head = i
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
                if(i['type'] == ArmourType.shirt):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.body['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equipped')
                        if(alder.body['armId'] != '1'):
                            inv.append(p.body)
                        p.body = i
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
                if(i['type'] == ArmourType.trousers):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.legs['defence'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equipped')
                        if(alder.legs['armId'] != '1'):
                            inv.append(p.legs)
                        p.legs = i
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
                if(i['type'] == Weapon1Type.sword or i['type'] == Weapon1Type.dagger or i['type'] == Weapon1Type.spear or
                   i['type'] == Weapon1Type.axe or i['type'] == Weapon1Type.mace or i['type'] == Weapon1Type.staff):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon1['attack'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(p.weapon1['wpId'] != '0'):
                            inv.append(p.weapon1)
                        p.weapon1 = i
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
                if(i['type'] == Weapon2Type.bow or i['type'] == Weapon2Type.crossbow or i['type'] == Weapon2Type.sling or
                   i['type'] == Weapon2Type.shield or i['type'] == Weapon2Type.wand):
                    count +=1
                    equipable.append(i)
                    if(i['type'] == Weapon2Type.bow):
                        if (p.weapon2['type'] == Weapon2Type.bow or p.weapon2['type'] == Weapon2Type.crossbow or p.weapon2['type'] == Weapon2Type.sling):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == Weapon2Type.crossbow):
                        if (p.weapon2['type'] == Weapon2Type.bow or p.weapon2['type'] == Weapon2Type.crossbow or p.weapon2['type'] == Weapon2Type.sling):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == Weapon2Type.sling):
                        if (p.weapon2['type'] == Weapon2Type.bow or p.weapon2['type'] == Weapon2Type.crossbow or p.weapon2['type'] == Weapon2Type.sling):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == Weapon2Type.shield):
                        if (p.weapon2['type'] == Weapon2Type.shield):
                            print(count, ': ', i['name'], '- Defence: +', i['defence'] - p.weapon2['defence'])
                        else:
                            print(count, ': ', i['name'], '- Defence: +', i['defence'])
                    elif(i['type'] == Weapon2Type.wand):
                        print(count, ': ', i['name'], '- Spell: ', i['spell'])
                        for j in p.spells:
                            if (j['spId'] == i['wpId']):
                                j['unlocked'] = True
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(p.weapon2['wpId'] != '0'):
                            inv.append(p.weapon2)
                        p.weapon2 = i
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

#Use Item
def useItem(p):
    use = []
    count = 1
    print('\nBag Items')
    for i in inv:
        if(i['type'] == ItemType.healing or i['type'] == ItemType.food):
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
                if (i['type'] == ItemType.healing):
                    p.health += i['heals']
                    print(p.name, ' recoved ', i['heals'], ' health')
                    if (p.health > p.maxHealth):
                        p.health = p.maxHealth
                elif (i['type'] == ItemType.food):
                    p.stamina += i['recovers']
                    print(p.name, ' recoved ', i['recovers'], ' stamina')
                    if (p.stamina > p.maxStamina):
                        p.stamina = p.maxStamina
                i['count'] -= 1
                if(i['count'] <= 0):
                    inv.remove(i)
            count +=1
        use.clear()
#The user should buy items from shop
def shop(seller):
    shopping = True
    while(shopping == True):
        if(seller == 'Jeb'):
            print('\nFeel free to browse my wares.')
            print('1: Bandage ', 'Remaining: ', '5 Cost: 5')
            print('2: Dried Fruit' , 'Remaining: ', '5 Cost: 1')
            print('3: Hazel Nuts ', 'Remaining: ', '5 Cost: 1')
            print('e - Exit')
            p = input('Purchase: ')
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

#Attack Enemy
def attack(p, e):
    numOfAtk = 1
    impact = 0
    if (p.weapon1['type'] == Weapon1Type.dagger):
        numOfAtk += 1
    target = p.accuracy() + 100 - e.evasion()
    hit = random.randrange(0,100)
    critical = random.randrange(0,100)
    p.stamina -= 5
    while(numOfAtk > 0):
        if (p.ammo['loaded'] == True):
            p.cStatus = 'RAttacking'
            if (hit < target):
                impact = random.randrange(p.attackRanged() - 3, p.attackRanged() + 3)
                impact += p.ammo['damage']
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + e.defence())))
                im = impact
                if (e.cStatus == CombatStatus.Blocking):
                    impact = round(impact/10)
                    if (impact <= 0):
                        impact = 1
                    im = impact
                    if (e.weapon2['type'] == Weapon2Type.shield):
                        if (e.weapon2['defence'] > 0):
                            print('Attack blocked!')
                            impact -= e.weapon2['defence']
                            if (impact < 0):
                                impact = 0
                print('\n',p.name,' fired a', p.ammo['name'], '!')
                if(critical >= 90):
                    print('Critical Hit!')
                    if (p.weapon2['type'] == Weapon2Type.sling):
                        e.aliment = 'Stun'
                e.health -= impact
                print(e.name, ' took ', impact, ' damage!')
                p.ammo['loaded'] = False
                if(e.health <= 0):
                    print(e.name, ' defeated.')
                return im
            else:
                print('\n',p.name,' Missed')
                return 0
        else:
            p.cStatus = CombatStatus.Attacking
            if ((e.aliment['outRange'] != True or (e.aliment['outRange'] == True and p.weapon1['type'] == Weapon1Type.spear)) and
                (p.aliment['outRange'] != True or (p.aliment['outRange'] == True and p.weapon1['type'] == Weapon1Type.spear)) and
                (e.aliment['outRange'] != True and p.aliment['outRange'] != True)):
                if (hit < target):
                    impact = random.randrange(p.attack() - 5, p.attack() + 5)
                    if(p.weapon1['wpId'] != '0'):
                        if (critical >= 90):
                            impact += 10
                        impact = round(impact * (100/(100 + e.defence())))
                        im = impact
                        if (impact <= 0):
                            impact = 1
                        if (e.cStatus == CombatStatus.Blocking):
                            impact = round(impact/10)
                            if (impact <= 0):
                                impact = 1
                            im = impact
                            if (e.weapon2['defence'] > 0):
                                if (p.weapon1['type'] == Weapon1Type.axe):
                                    print('Shield repealed!')
                                    e.cStatus = CombatStatus.Normal
                                else:
                                    print('Attack blocked!')
                                    impact -= e.weapon2['defence']
                                if (impact < 0):
                                    impact = 0
                        e.health -= impact
                        if (p.cStatus == CombatStatus.Countered):
                            print('\n',p.name,' countered!')
                        else:
                            print('\n',p.name,' attacked!')
                        if(critical >= 90):
                            print('Critical Hit!')
                            if (p.weapon1['type'] == Weapon1Type.mace):
                                e.aliment['stun'] = True
                        print(e.name, ' took ', impact, ' damage!')
                        if(e.health <= 0):
                            print(e.name, ' defeated.')
                        return im
                    else:
                        print('\nBut',p.name, ' was unarmed')
                        return 0
                else:
                    print('\n',p.name,' Missed')
                    return 0
            else:
                print('\n', e.name, ' was out of range')
        numOfAtk -= 1
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
def inEffect(p, e):
    for i in alder.abilities:
        if(i['active'] == True):
            i['inEffect'] -= 1
            if (i['inEffect'] <= 0):
                i['active'] = False
                print(alder.name,"'s ", i['name'], ' has worn off.')

def magic(p, t, e, spell):
    hit = random.randrange(0,100)
    damage = spell['damage']
    if (p.weapon1['type'] == Weapon1Type.staff):
        boost = damage / 20
        if (boost < 1):
            boost = 1
        damage += round(boost)
    count = 1
    if (spell['type'] == 'offence'):
        for i in e:
            print(count, ') ', i.name)
            count += 1
    elif (spell['type'] == 'support'):
        for i in t:
            if (i.pId != p.pId):
                print(count, ') ', i.name)
                count += 1
    if (hit < spell['effectivness']):
        if (spell['type'] == 'offence'):
            target = input('Cast on:')
            if (spell['attackType'] == 'single'):
                count = 1
                for i in e:
                    if (target == str(count)):
                        if (spell['spId'] == '1'):
                            i.aliment['poison'] = True
                        elif (spell['spId'] == '2'):
                            i.aliment['fungus'] = True
                        elif (spell['spId'] == 'comb1'):
                            i.aliment['poison'] = True
                            i.aliment['fungus'] = True                        
                    count +=1
                if(damage > 0):
                    i.health -= damage
                    print(i.name, 'took', damage, 'from', spell['name'],'!')
        if (spell['type'] == 'support'):
            target = input('Cast on:')
            if (spell['attackType'] == 'single'):
                count = 1
                for i in t:
                    if (target == str(count)):
                        if (spell['spId'] == 'f1'):
                            i.health += damage
                            if (i.health > i.maxHealth):
                                i.health = i.maxHealth
                        elif (spell['spId'] == '4'):
                            i.stamina += damage
                            if (i.stamina > i.maxStamina):
                                i.stamina = i.maxStamina
        if (spell['type'] == 'enhance'):
            if (spell['spId'] == '3'):
                p.stamina += damage
    else:
        print('The spell missed!')
        
def manuver(p, e, m):
    if (m['specialType'] == SpecialType1.manuver):
        if (m['spId'] == 'a1'):
            if (p.health < p.maxHealth/5):
                p.stamina -= m['cost']
                m['inEffect'] = 6
        if (m['spId'] == '1'):
            active = True
            for i in e:
                if(i.aliment['outRange'] == False):
                    active = False
            if (p.aliment['outRange'] == True):
                p.aliment['outRange'] = False
                print(p.name,'advanced closer!')
            elif (active == True):
                for i in e:
                    i.aliment['outRange'] = False
                print(p.name,'advanced closer!')
            else:
                print(p.name,'is too close!')
        if (m['spId'] == '2'):
            if (p.aliment['outRange'] == False):
                p.aliment['outRange'] = True
                print(p.name,'retreated to the rear!')
            else:
                print(p.name,'is too far away!')

def combine(spell1, spell2):
    for i in combinations:
        if (i['components'][0] == spell1['spId'] and i['components'][1] == spell2['spId']):
            return i
    
def special(p, h, e, r):
    print('\nSpecial Ability')
    if(p.aliment['outRange'] == True):
        print(' 1 Position) Advance - 10 Stamina')
    else:
        print(' 1 Position) Retreat - 10 Stamina')
    offensive = p.special_off()
    support = p.special_sup()
    enhance = p.special_enc()
    print(' 2 Offensive) ',offensive['name'], ' - ', offensive['effect'], ' - ', offensive['cost'], ' stamina\n',
          '3 Support) ',support['name'], ' - ', support['effect'], ' - ', support['cost'], ' stamina\n',
          '4 Enhance) ',enhance['name'], ' - ', enhance['effect'], ' - ', enhance['cost'], ' stamina')
    sp = input('Use: ')
    if (sp == "1" or sp == "advance" or sp == "retreat"):
        p.cStatus = CombatStatus.Specializing
        if(p.aliment['outRange'] == True):
            p.stamina -= manuvers[0]['cost']
            manuver(p,e,manuvers[0])
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':manuvers[0]['name']})
        else:
            p.stamina -= manuvers[1]['cost']
            manuver(p,e,manuvers[1])
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':manuvers[1]['name']})
    elif ((sp == "2" or sp == "offence" or sp == "offensive") and offensive['spId'] != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= offensive['cost']
        if(offensive['specialType'] == SpecialType1.manuver):
            manuver(p,e,offensive)
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':offensive['name']})
        elif(offensive['specialType'] == 'spell'):
            magic(p, h, e, offensive)
            print('\n', p.name, ' uses ', offensive['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.magic, 'Spell':offensive['name']})
    elif ((sp == "3" or sp == "support") and support['spId'] != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= support['cost']
        if(offensive['specialType'] == SpecialType1.manuver):
            manuver(p,e,support)
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':support['name']})
        elif(offensive['specialType'] == 'spell'):
            magic(p, h, e, support)
            print('\n', p.name, ' uses ', support['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.magic, 'Spell':support['name']})
    if ((sp == "4" or sp == "enhance") and enhance['spId'] != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= enhance['cost']
        if(enhance['specialType'] == SpecialType1.manuver):
            manuver(p,e,enhance)
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':enhance['name']})
        elif(enhance['specialType'] == 'spell'):
            magic(p, h, e, enhance)
            print('\n', p.name, ' uses ', offensive['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.magic, 'Spell':enhance['name']})


#Use Item
def item(p, e, r):
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
                if(i['type'] == ItemType.healing):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'food' or y == 'Food' or
            y == 'consumables' or y == 'Consumables'):
            print('Food')
            for i in inv:
                if(i['type'] == ItemType.food):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'projectiles' or y == 'Projectiles'):
            print('Projectiles')
            for i in inv:
                if(i['type'] == ItemType.projectile or i['type'] == ItemType.toss):
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
                    if (i['type'] == ItemType.healing):
                        p.health += i['heals']
                        print(p.name, ' recoved ', i['heals'], ' health')
                        if (p.health > p.maxHealth):
                            p.health = p.maxHealth
                        p.cStatus = CombatStatus.Using
                        using = False
                    elif (i['type'] == ItemType.food):
                        p.stamina += i['recovers']
                        print(p.name, ' recoved ', i['recovers'], ' stamina')
                        if (p.stamina > p.maxStamina):
                            p.stamina = p.maxStamina
                        p.cStatus = CombatStatus.Using
                        using = False
                    elif (i['type'] == ItemType.projectile):
                        print(u, count)
                        if (i['weapon'] == Weapon2Type.bow):
                            if(p.weapon2['type'] == Weapon2Type.bow):
                                print('\nArrow loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                p.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Bow required!')
                                using = False
                        elif (i['weapon'] == Weapon2Type.crossbow):
                            if(p.weapon2['type'] == Weapon2Type.crossbow):
                                print('\nBolt loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                p.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Crossbow required!')
                                using = False
                        elif (i['weapon'] == Weapon2Type.sling):
                            if(p.weapon2['type'] == Weapon2Type.sling):
                                print('\nStone loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                p.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Sling required!')
                                using = False
                    elif (i['type'] == ItemType.toss):
                        count = 1
                        for j in e:
                            print(count, ': ', j.name)
                            count += 1
                        count = 1
                        target = input('Throw at: ')
                        for j in e:
                            if (target == str(count)):
                                print('\n',p.name,'threw ', i['name'])
                                j.aliment['caught'] = True 
                                p.cStatus = CombatStatus.Using
                                using = False
                            count += 1
                    i['count'] -= 1
                    if(i['count'] <= 0):
                        inv.remove(i)
                    r.append({'Id': p.pId, 'Who':p.name, 'Item': i['name'], 'Status':p.cStatus, 'ItemType':i['type']})
                count +=1
            if u == 'e':
                using = False
            use.clear()
#Combat order
def fightOrder(e):
    return e.speed()
            
#Combat interface
def battle(e):
    os.system('clear')
    global alder
    heroes = [alder]
    enemys = []
    record = []
    for i in e:
        count = 1
        if i.enId != '0':
            i.inId = str(count)
            enemys.append(i)
        count += 1
    combatants = heroes + enemys
    fighting = True
    winner = False
    count = 1
    for i in heroes:
        if (i.weapon2['type'] == Weapon2Type.shield):
            i.shield = i.weapon2['defence']
    while(fighting == True):
        for i in heroes:
            hunger(i)
        #Order combatents by fastest to slowest
        combatants.sort(key=fightOrder, reverse=True)
        for i in combatants:
            if (fighting == True):
                #Win condition
                if (enemys[0].health <= 0):
                    k = 0
                    for remaining in enemys:
                        if (remaining.health <= 0):
                            k += 1
                    if (k == len(enemys)):
                        winner = True
                #Death Condition
                if(i.health <= 0 and i.type == 'playable'):
                    k = 0
                    for remaining in heroes:
                        if (remaining.health <= 0):
                            k += 1
                    if (k == len(heroes)):
                        death()
                        return False
                #Win
                elif(winner == True):
                    for j in alder.abilities:
                        j['active'] = False
                        j['inEffect'] = 0
                    fighting = False
                    win(enemys)
                    return True
                if (i.type == 'playable' and i.health > 0):
                    #Automatic special
                    automatic = i.special_auto()
                    if(automatic['spId'] != '0'):
                        if(automatic['specialType'] == SpecialType1.manuver):
                            manuver(i,e,automatic)
                            print('\n',automatic['name'],'is active.')
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':automatic['name']})
                        elif(automatic['specialType'] == 'spell'):
                            magic(i, h, e, automatic)
                            print('\n',automatic['name'],'is active.')
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'SpecialType':SpecialType1.magic, 'Spell':automatic['name']})
                    inEffect(i, enemys)
                    i.cStatus = CombatStatus.Normal
                    while(i.cStatus == CombatStatus.Normal):
                        for j in enemys:
                            if j.message(count) != None:
                                print (j.message(count))
                        print('\n',i.name)
                        if (i.ammo['loaded'] == True):
                            print('Ranged weapon set!')
                        print("Health: ", i.health, '/', i.maxHealth, "| Stamina: ", i.stamina, '/', i.maxStamina)
                        print("1) Attack     3) Appraise     5) Item")
                        print("2) Block      4) Special      6) Flee")
                        j = input('Action: ')
                        if (j == '1' or j == 'attack' or j == 'Attack'):
                            print('\nEnemies')
                            k = 1
                            for j in enemys:
                                if (j.health > 0):
                                    print(k, ': ', j.name)
                                    k += 1
                            target = input('Attack: ')
                            k = 1
                            for j in enemys:
                                if (j.health > 0):
                                    if (target == str(k)):
                                        impact = attack(i, j)
                                        if (j.cStatus == CombatStatus.Blocking and impact > 0):
                                            j.weapon2['defence'] -= impact
                                        record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'Hit': j, 'Damage':impact})
                                    k += 1
                        elif (j == '2' or j == 'block' or j == 'Block'):
                            i.cStatus = CombatStatus.Blocking
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus})
                        elif (j == '3' or j == 'appraise' or j == 'Appraise'):
                            for j in enemys:
                                print('\n',j.name, 'Health:', j.health,'/',j.maxHealth)
                                print(j.desc)
                        elif (j == '4' or j == 'special' or j == 'Special'):
                            special(i, heroes, enemys, record)
                        elif (j == '5' or j == 'item' or j == 'Item'):
                            item(i, enemys, record)
                        elif (j == '6' or j == 'flee' or j == 'Flee'):
                            j = input('Are you sure you want to run?(y/n)')
                            if (j == 'y' or j == 'Y' or j == 'yes' or j == 'Yes'):
                                i.cStatus = CombatStatus.Escaping
                                record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus})
                                return False
                else:
                    if(i.health > 0):
                        if (i.aliment['poison'] == True):
                            poison = i.maxHealth / 10
                            if (round(poison) < 0):
                                poison = 1
                            i.health -= round(poison)
                            print(i.name, 'took', round(poison), 'damage from poison!')
                            record.append({'Id': i.enId, 'Who':i.name, 'Type': i.type, 'Aliment':'poison', 'Damage':round(poison)})
                        if (i.aliment['caught'] == True):
                            escape = random.randrange(0, 100)
                            if (i.type == 'bug'):
                                if (escape >= 95):
                                    print('The',i.name, 'escaped the net!')
                                    i.aliment['caught'] = False
                                else:
                                    print('The', i.name,' is tangled in a net!')
                            elif (i.type == 'soldier'):
                                if (escape >= 30):
                                    print(i.name, 'escaped the net!')
                                    i.aliment['caught'] = False
                                else:
                                    print(i.name,' is tangled in a net!')
                            record.append({'Id': i.enId, 'Who':i.name, 'Type': i.type, 'Aliment':'caught', 'Caught':i.aliment['caught']})
                        elif (i.aliment['stun'] == True):
                            print(i.name, 'was stunned!')
                            i.aliment['stun'] = False
                        else:
                            impact = i.action(i, heroes, record)[0]
                for j in reversed(enemys):
                    if (j.cStatus == CombatStatus.Escaping):
                        enemys.remove(j)
                        if (len(enemys) == 0):
                            fighting = False
                            return True
        count += 1
        alder.cStatus = CombatStatus.Normal
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
#Read books
def reading(series, book):
    bookPages = []
    readType = 'lines'
    f = open("data/books.txt", "rt")
    skip = False
    for i in f:
        line = i.split('$ ')
        if (line[0] == series and line[1] == book):
            readType = line[3]
            bookPages.append(i)
    print('')
    if (readType == 'lines'):
        for i in bookPages:
            line = i.split('$ ')
            if (line[0] == series and line[1] == book):
                image = line[5]
                content = line[6]
                tabbedline = line[6].split('£')
                if (image != 'None'):
                    print(image)
                if (len(tabbedline) > 1):
                    for i in tabbedline:
                        print('\t',i.strip('\n'))
                else:
                    print('\n',content.strip('\n'))
    elif (readType == 'story'):
        for i in bookPages:
            if(skip == False):
                line = i.split('$ ')
                if (line[0] == series and line[1] == book):
                    image = line[5]
                    content = line[6]
                    tabbedline = line[6].split('£')
                    if (image != 'None'):
                        print(image)
                    if (len(tabbedline) > 1):
                        for i in tabbedline:
                            print('\t',i)
                    else:
                        print('\n',content.strip('\n'))
                    s = input()
                    if(s == 'skip'):
                        skip = True
    elif (readType == 'random'):
        i = random.choice(bookPages)
        line = i.split('$ ')
        if (line[0] == series and line[1] == book):
            image = line[5]
            content = line[6]
            tabbedline = line[6].split('£')
            if (image != 'None'):
                print(image)
            if (len(tabbedline) > 1):
                for i in tabbedline:
                    print('\t',i)
            else:
                print('\n',content.strip('\n'))
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
            print("The cottage kitchen contained various 'pots' hanging on the wall. It had a 'stove' where a 'cauldron' was dangling on a chain. In addition, a smaller room served as the 'larder'. There was also a 'cupboard' and two 'tables', one of which had a wooden 'bowl' on it. Alder had been washing dishes in a 'basin' on the other table next to the 'window'.")
            e = input('Examine: ')
            if (e == 'cauldron' or e == 'Cauldron'):
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][1] == False):
                    print('Alder got a wet cloth and started scrubbing the cauldron. Florace peeked into the living room at Kyla and then went over to help him.')
                    cont()
                    print('Florace:')
                    print('"Shh."')
                    sQuests[0]['required'][1] = True
                    examining = False
                else:
                    print("A small metal cauldron was suspended above the stove by a chain. It was empty right now.")
                cont()
            elif (e == 'pots' or e == 'Pots'):
                print('Various pots and pans were hung on hooks along the wall.')
                cont()
            elif (e == 'cupboard' or e == 'Cupboard'):
                print('The cupboard was full of plates, bowls and other kitchen and dining utensils.')
                cont()
            elif (e == 'bowl' or e == 'Bowl'):
                if (PKSwitch[0] == True):
                    print('A large wooden bowl. It has hazelnuts in it.')
                    pickup = input('Take the hazelnuts?(y/n)')
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
                print('The basin Alder was washing in was full of water from Alder cleaning dishes. Clean plates were lined up to the side.')
                cont()
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(tutorialSwitch[2] == True):
                    print('Florace and Thay were talking outside the window.')
                    cont()
                    print('Alder:')
                    print('"I'"'"'m coming out"')
                    chapter = '1'
                    tutorialSwitch[0] = False
                else:
                    print('The clearing at the front of of the cottage can be seen through the window.')
                cont()
            elif (e == 'stove' or e == 'Stove'):
                print('The stove was made of metal plates above an unlit fireplace full of dry branches. The fire would heat the metal plates of the stove to cook meat.')
                cont()
            elif (e == 'table' or e == 'Table' or e == 'tables' or e == 'Tables'):
                print('A rectangular wooden table stood in the centre of the room while a thinner one with a basin stood by the window.')
                cont()
            elif (e == 'hornets' or e == 'Hornets'):
                if (tutorialSwitch[5] == False and c2Switch[0] == True):
                    print('The hornets Alder slew were hung up on hooks. To be cooked for supper.')
                    cont()
            elif (e == 'larder' or e == 'Larder'):
                if (sQuests[1]['accepted'] == True):
                    print('There was only a single loaf of bread in the larder. It would have to do.')
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
            if (sQuests[2]['required'][1] == True):
                print('There was a large hole in the wall.')
            e = input('Examine: ')
            if (e == 'bookshelf' or e == 'Bookshelf'):
                if (sQuests[2]['accepted'] == True and sQuests[2]['required'][0] == False):
                    print('Alder carried each of the books and put them in a neat pile near the stairs.')
                    cont()
                    sQuests[2]['required'][0] = True
                elif(sQuests[2]['required'][0] == True):
                    print('The bookshelf was empty.')
                else:
                    read = ''
                    while (read != 'e'):
                        print('\nThe books in the living room bookshelf include:')
                        print('\t1) Magic: The Basics')
                        print('\t2) Magical Articles of History')
                        print('\t3) Potions')
                        print('\t4) Developers Note - Kyla'"'"'s cottage')
                        print('\t5) Developers Note - Wild and Wyrd Demo')
                        print('\te) Close')
                        read = input('Read: ')
                        if(read == '1'):
                            reading('1', '1')
                        elif(read == '2'):
                            if(c3Switch[0] == False and c3Switch[1] == True):
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
                                print('Kyla unsheathed that sword and held it in her hand. The blade darkened and bent and it was not long before it dropped off leaving only the handle.')
                                cont()
                                print('Kyla:')
                                print('"Boy you can have the sword back now, make sure you hold it by the grip."')
                                cont()
                                print('Alder said nothing as he picked up the sword. As he did, a new blade started to grow from the rain-guard until it was back to its original glory.')
                                cont()
                                alder.weapon1 = weapons[1]
                                print(alder.weapon1['name'],'equipped!')
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
                                    print('3: "What'"'"'s with the sword blade?"')
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
                                        print('"They are able to pass on their knowledge and natural abilites after death."')
                                        cont()
                                        print('Kyla:')
                                        print('"One previous Scion killed a dragon, while another saved countless innocents from slavers."')
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
                                        print('"That mouse was no doubt Agrimus; the Scion before you."')
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
                                        print('"When held by the Scion it grows and strengthens, when held by any other it weakens and dies."')
                                        cont()
                                        dialog[2] = True
                                print('???:')
                                print('"The rabbit seeks his burrow!"')
                                cont()
                                print('*Click*')
                                print('*Ring*')
                                cont()
                                print('The door unlocked and the bell chimed in responce to the words of the voice outside. The ringing filled the resounded throught the cottage but was prevelant in the already alerted living room.')
                                cont()
                                print('Alder, Florace and Kyla:')
                                print('"...?"')
                                cont()
                                print('Florace:')
                                print('"Who is that?"')
                                cont()
                                read = 'e'
                                examining = False
                                c3Switch[1] = False
                            else:
                                reading('1', '2')
                        elif(read == '3'):
                            reading('1', '3')
                        elif(read == '4'):
                            reading('2', '1')
                        elif(read == '5'):
                            reading('2', '2')
                    
            elif (e == 'fireplace' or e == 'Fireplace'):
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][0] == False):
                    print('Alder got to work cleaning the fireplace using a brush and cloth. By the end his arms were completely blackened by soot.')
                    cont()
                    print('Kyla:')
                    print('"Throw that ash outside."')
                    cont()
                    print('Kyla:')
                    print('"If it gets on the floor, you'"'"'re cleaning it up."')
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
                    print("A single round wooden table sat a safe distance from the fire, but close enough to feel its warmth.")
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
                    print('Alder aligned himself with where the tools hung in the shed on the other side of the wall.')
                    cont()
                    victory = battle([enemyUnits.Wall(), Null(), Null()])
                    if (victory == True):
                        print('The swords power was incredible. With a bit of force it easily pierced the clay walls and Alder tore it down through the gap he had created, the tools on the other side now fallen amongst rubble. Kyla apparently found this amusing. But the hole allowed Alder to enter the shed.')
                        cont()
                        sQuests[2]['required'][1] = True
                        examining = False
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '3'):
            print("The burrow was within a deep wood, isolated from society. The 'sky' was clear blue and the late summer 'plant' was abundant amongst the 'trees' and 'rocks' of the forest. Part of the stone disguising the 'cottage', was actually an old 'shed' with a slanted roof, nearby was a large 'bramble' bush.")
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                print('It was a bright, clear blue.')
                cont()
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                print('There were a variety of late-summer mushrooms growinig around the area.')
                cont()
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                print('Various weeds, wildflowers and moss interspersed with bramble bushes holding ripe blackberries.')
                cont()
            elif (e == 'trees' or e == 'Trees'):
                print('Various trees made up the woodland, the majority were birch, rowen and holly.')
                cont()
            elif (e == 'rocks' or e == 'Rocks'):
                print('There were a few boulders in the area. None were as large as the cottage.')
                cont()
            elif (e == 'cottage' or e == 'Cottage'):
                print('While the cottage was made to look like a large boulder from the outside, it actually had two floors and was made from white clay bricks. It was cosy and well protected against the elements, but Alder had always felt constricted.')
                cont()
            elif (e == 'shed' or e == 'Shed'):
                print('The shed had a single old door. From the outside it looked like part of the larger stone, but it was really made entirely of splintered wooden planks.')
                cont()
            elif (e == 'bush' or e == 'Bush' or e == 'blackberry' or e == 'Blackberry' or e == 'blackberry bush' or e == 'Blackberry Bush'  or e == 'bramble' or e == 'Bramble'):
                if (PKSwitch[2] == True):
                    print('The bramble bush was a convenient source of fresh fruit at this time of year. It still had a few blackberries on it.')
                else:
                    print('It still had a few blackberries on it but they were out of reach and Alder did not want to get pricked by its thorns.')
                if (PKSwitch[2] == True):
                    pickup = input('Pick the blackberries?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 blackberries obtained')
                        itemCount(food[0], 5)
                        PKSwitch[2] = False
                if (sQuests[0]['accepted'] == True and sQuests[0]['required'][2] == False):
                    print('Alder picked some bramble leaves, careful to avoid the thorns. He wondered what potion Kyla was going to use them for.')
                    count = 0
                    for i in inv:
                        if (i['type'] == ItemType.ingredient):
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
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'. Opposite the entrance was a 'table' used for crafts with an old 'sack' was slumped against it and a 'bow' and 'quiver' full of 'arrows'.")
            else:
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'. Opposite the entrance was a 'table' used for crafts.")
            if (sQuests[2]['required'][1] == True):
                print('There was a large hole in the wall.')
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('A single window was to the left upon entering through the doorway.')
                cont()
                print('it'"'s"' angle meant that upon looking through, only the woods could been seen.')
                cont()
            elif (e == 'tools' or e == 'Tools' or e == 'axe' or e == 'Axe' or e == 'saw' or e == 'Saw' or
                  e == 'pick' or e == 'Pick' or e == 'shovel' or e == 'Shovel' or e == 'sickle' or e == 'Sickle' or
                  e == 'rod' or e == 'Rod' or e == 'fishing' or e == 'Fishing' or e == 'fishing rod' or e == 'Fishing rod'):
                print('Various tools were hung on the wall and sat on the shelves, including an axe, saw, pick, shovel, sickle and fishing rod.')
                cont()
            elif (e == 'pots' or e == 'Pots'):
                if (sQuests[2]['accepted'] == True and sQuests[2]['required'][2] == False):
                    print('Alder carried each pot one by one to the living room, their weight varyied by how full they were and what was in them. The heaviest pot was full of ground up plant matter and weighed as much as a cannon ball. Alder brought the last one in with great strain.')
                    cont()
                    location = '2'
                    sQuests[2]['required'][2] = True
                    examining = False
                elif(sQuests[2]['required'][2] == True):
                    print('There weren'"'"'t any pots left.')
                else:
                    print('The pots contained potion ingredients, left in the shed to save space in the main cottage. One pot was completely filled with eyeballs.')
                    cont()
            elif (e == 'crates' or e == 'Crates' or e == 'boxes' or e == 'Boxes'):
                print('Kyla had put spare magical tools in study crates to keep them from breaking.')
                cont()
            elif (e == 'table' or e == 'Table'):
                if (PKSwitch[1] == True):
                    print("On the table was an unlit 'candle', a 'mortar' and 'pestle' and a hunting 'knife'.")
                    if (tutorialSwitch[3] == False):
                        pickup = input('Take the hunting knife?(y/n)')
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
                        if (i['type'] == ItemType.ingredient and i['ingId'] == '1'):
                            print('Alder ground the leaves with the pestle until they were powder. He then put them in a nearby pot containing remnants of the same powder.')
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
                    print('The old burlap sack was intended for foraging, but was cheaply made and on the verge of falling apart.')
                    if (PKSwitch[5] == True):
                        print('There'"'"'s a bandage inside.')
                        cont()
                        pickup = input('Take the bandage.(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nBandage obtained')
                            itemCount(items[0], 1)
                            PKSwitch[5] = False
                    cont()
                elif (e == 'bow' or e == 'Bow' or e == 'quiver' or e == 'Quiver' or e == 'arrows' or e == 'Arrows'):
                    print('A practice bow and a quiver full of arrows. They were intended as a gift for Florace but she was never interested in archery, so they were passed to Alder instead.')
                    cont()
        elif (location == '5'):
            print("Sunlight beamed through the solitary curtainless 'window' of Alder's small bedroom, which contained only a makeshift 'bed'.")
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('Through the small, curtainless window, Alder could see sunlight breaching the branches of the Oldwyrm Woods near the edge of the clearing.')
                cont()
            elif (e == 'bed' or e == 'Bed'):
                print('It was cheaply made from dry wood and partridge feathers. It was powdered with herbs to stop it smelling. Thay helped Alder make it.')
                if (PKSwitch[4] == True):
                    pickup = input("Among the feathers were Alder's savings. Take them?(y/n)")
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
                    print('There were a variety of late-summer mushrooms growing around the area. Many of which are edible.')
                    cont()
                    pickup = input('Take the mushrooms?(y/n)')
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
                        battle([enemyUnits.Cricket(), Null(), Null()])
                        if(alder.cExp > 0):
                            print('Alder:')
                            print('"Hunt succesful."')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('As Alder collected the slain cricket, a loud buzzing came at him from his side. Two hornets came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            battle([enemyUnits.Hornet(), enemyUnits.Hornet(), Null()])
                        elif(alder.cExp == 0):
                            print('Alder:')
                            print('"Come back you!"')
                            cont()
                            print('Alder tried in vain to get the cricket, but it had already jumped out of reach.')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('The loud buzzing of insect wings came from Alder'"'"'s side. Two hornets came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            battle([enemyUnits.Hornet(), enemyUnits.Hornet(), Null()])
                        if (alder.health <= 0 or game_active == False):
                            #print('When Alder is defeated he will lose some of his possessions such as currency. The story will be taken back to before the fight so another attempt can be made.')
                            location = '3'
                            alder.health = alder.maxHealth
                            alder.stamina = alder.maxStamina
                        else:
                            tutorialSwitch[5] = False
                            print('The hornets were still twitching, but Alder knew they were dead.')
                            cont()
                            print('Alder:')
                            print('"Did I anger them?"')
                            cont()
                            print('Alder was puzzled by the attack but regardless it was time to return to Florace.')
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
                print('From the centre of the clearing a misty light hung from unknown source, illuminating the area as far as the trees.')
                examining = False
                if(c2Switch[3] == True):
                    switch[8] = True
                    part = '4'
            elif (e == 'e' or e == 'E'):
                examining = False
            elif(c2Switch[3] == False):
                if(e == 'sword' or e == 'Sword'):
                    print('The double edged sword was a dark green with silver embellishments along the hilt and scabbard. It was a size suited for a mouse but would still be heavy for one. Now that it was closer Alder could see detail in its design. What looked like a thorny stem engraved around the grip, the rain-guard was shaped to resemble leaves and the pommel was tear-shaped. A rounded slot was carved into the scabbard.')
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
            t = input('Talk to: ')
            if (t == '1'):
                if(alder.health < alder.maxHealth):
                    print('Florace:')
                    print('"You look worse for wear."')
                    cont()
                    print('Florace:')
                    print('"Hold still, I'"'"'ll help fix you up."')
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
                    print('"Take a nap, you'"'"'ll feel better."')
                    cont()
        else:
            print('There was no one to talk to.')
    elif (location == '2'):
        if (tutorialSwitch[5] == False and chapter == '1'):
            if (sQuests[0]['accepted'] != True):
                print('1: Kyla(!)')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Madam Kyla was relaxed in her chair with her nose in a red book titled "A sorcerers guide to Dragons and Wyverns". She peered from the book to Alder.')
                    cont()
                    print('Kyla:')
                    print('"I take it Mr Prickle has gone?"')
                    cont()
                    print('Alder:')
                    print('"Yes, Madam."')
                    cont()
                    print('Kyla:')
                    print('"Making you free boy?"')
                    cont()
                    print('Alder:')
                    print('"Yes, Madam."')
                    cont()
                    print('Kyla:')
                    print('"Then clean the fireplace, wash the cauldron in the kitchen and..."')
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
                    print('"Leave the dust in the pot on the far end next to the shed table."')
                    cont()
                    print('Kyla:')
                    print('"That should keep you busy!"')
                    cont()
                    i = input('Do you accept this labour?(y/n):')
                    confirm = yn(i)
                    if(confirm == True):
                        print('Alder:')
                        print('"Yes, Madam."')
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
                t = input('Talk to: ')
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
            t = input('Talk to: ')
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
            t = input('Talk to: ')
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
            #print(c3Switch)
            if(c3Switch[1] == True):
                print('1: Florace')
                print('2: Kyla')
                t = input('Talk to: ')
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
                t = input('Talk to: ')
                if (t == '1'):
                    print('Florace:')
                    print('"I'"'"'ve never heard that voice before."')
                    cont()
                    print('Florace:')
                    print('"Check the window."')
                    cont()
                elif (t == '2'):
                    print('Kyla:')
                    print('"Hmm."')
                    cont()
            elif(c3Switch[6] == True):
                if (sQuests[1]['accepted'] != True):
                    print('1: Florace(!)')
                else:
                    print('1: Florace')
                if (sQuests[2]['accepted'] != True):
                    print('2: Kyla(!)')
                else:
                    print('2: Kyla')
                if(c3Switch[3] == False and c3Switch[4] == True):
                    print('3: Weasel')
                elif(c3Switch[4] == False and c3Switch[5] == True):
                    print('3: Jeb')
                t = input('Talk to: ')
                if (t == '1'):
                    if (sQuests[1]['accepted'] != True):
                        print('Alder:')
                        print('"What the matter Florace?."')
                        cont()
                        print('Florace:')
                        print('"We need food supplies to get to Forton!"')
                        cont()
                        print('Alder:')
                        print('"Like what?"')
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
                        print('"Thank you, Alder."')
                        cont()
                        sQuests[1]['submitted'] = True
                        qComp(sQuests[1])
                    else:
                        print('Florace:')
                        print('"Are you doing alright Alder?"')
                        cont()
                        print('Alder:')
                        print('"Fine."')
                        cont()
                        print('Alder:')
                        print('"But are you sure you want to give up your apprenticeship?"')
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
                        print('"Boy, gather my books from the bookshelf and the pots of ingredients from the shed and bring them here."')
                        cont()
                        print('Alder:')
                        print('"But the rat is outside, how do I get to the shed?"')
                        cont()
                        print('Kyla:')
                        print('"You will have to break down the '"'wall'"'."')
                        cont()
                        print('Kyla:')
                        print('"He'"'"'ll never hear it with my sound nullifying spell."')
                        cont()
                        print('Kyla:')
                        print('"Don'"'"'t concern yourself with any mess we need to get those valuables out safely."')
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
                        print('Kyla pulled out a bag and with Alder'"'"'s assistance placed the books and pots inside it one by one. The bag itself never got any larger or heavier while the pile gradually disappeared.')
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
                        print('"Still, I don'"'"'t like that they knew our password."')
                        cont()
                        print('Kyla:')
                        print('"Someone must have snitched..."')
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
            print('There was no one to talk to.')
    elif (location == '3'):
        if (chapter == '1'):
            if (tutorialSwitch[2] == True):
                print('1: Florace')
                t = input('Talk to: ')
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
                            print('"He usually comes here for sanctuary or potions."')
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
                            print('"This place cannot be seen from the outside world, so we tend to call it the burrow."')
                            cont()
                            dialog[1] = True
                    switch[2] = True
                    tutorial1 = False
                    tutorialSwitch[2] = False
            elif (tutorialSwitch[3] == True):
                print('1: Thay')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog = [False, False, False]
                    dialog2 = [False, False, False, False, False]
                    while(dialog[0] == False or dialog[1] == False or dialog2[4] == False):
                        print('1: "How was your journey?"')
                        print('2: "How did it go with Madame Kyla?"')
                        print('3: "What'"'"'s it like beyond the burrow?"')
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
                            print('"The usual, gave her the herbs she wanted in exchange for the potions I need."')
                            cont()
                            print('Thay reached into his bag and pulled out a vial of black liquid. Phantom Cloak; a magic potion that erased a creature’s presence when in darkness. It was one of the many potions that brought patrons to the cottage. Alder never asked what they needed them for.')
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
                            print('"West you’ll run into the river and if you climb to the treetops you can see Hare Hill east from here."')
                            cont()
                            print('Thay:')
                            print('"Wait!?"')
                            cont()
                            print('Seeing growing interest and curiosity on Alder'"'"'s face, Thay abruptly began to show concern.')
                            cont()
                            print('Thay:')
                            print('"Alder, you aren'"'"'t thinking of going to these places are you!?"')
                            cont()
                            print('Alder:')
                            print('"I..."')
                            cont()
                            print('Alder:')
                            print('"think, it would be nice to see new places."')
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
                            print('"I cannot even express how much humans are hated these days!!"')
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
                            print('"I’d never forgive myself if anything were to happen to you."')
                            cont()
                            print('Alder realised that the hedgehog was getting agitated and so decided to move on.')
                            cont()
                            dialog[2] = True
                        if (dialog[2] == True):
                            if (c == '4'):
                                print('Thay:')
                                print('"Oldwyrm woods is where we are right now."')
                                cont()
                                print('Thay:')
                                print('"This ancient woodland goes on for miles."')
                                cont()
                                print('Thay:')
                                print('"There are many birds in these woods and unfortunately that includes birds of prey, but most go after small creatures so you'"'"'ll be alright."')
                                cont()
                                dialog2[0] = True
                            if (c == '5'):
                                print('Alder:')
                                print('"It’s not that I want to go there, I’d just like to know."')
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
                                print('"At the top is the capital, Breabuck."')
                                cont()
                                print('Thay:')
                                print('"But it is a difficult and exhausting hike. Some routes lead to rock walls travelers need to scramble up."')
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
                                print('"Best for you to stay within the burrows borders young one."')
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
                t = input('Talk to: ')
                if (t == '1'):
                    dialog = [False]
                    while(dialog[0] == False):
                        print('Florace:')
                        print('"The knife should be in the shed. You can go once you'"'"'ve got it."')
                        cont()
                        dialog[0] = True
            elif (tutorialSwitch[5] == True):
                print('1: Florace')
                t = input('Talk to: ')
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
                print('There was no one to talk to.')
        elif(chapter == '2'):
            if (c2Switch[0] == False and c2Switch[1] == True):
                print('1: Trissie')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Trissie quickly set up a makeshift dummy out of leaves, sticks and a cheaply made old burlap sack that was intended for foraging before planting it in the ground so it would stand upright. The finished product was crude and clearly rushed, but would make a good target.')
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
                    battle([enemyUnits.Dummy(), Null(), Null()])
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
                                print('"I’m not easy to catch but you must be careful and stay safe."')
                                cont()
                                print('Trissie:')
                                print('"If you do, I'"'"'m sure we'"'"'ll meet before long."')
                                cont()
                                branchSwitch[0] = '2'
                                dialog[1] = True
                        print('Trissie moved swiftly towards the nearest tree and in an instant had climbed up and disappeared among the branches. It was as if she'"'"'d vanished. Leaving not even a rustle of leaves.')
                        cont()
                        print('Alder returned to the cottage a little disappointed with Trissie gone so soon. But he had work to do and he set about his remaining chores for the day.')
                        cont()
                        c2Switch[1] = False
            else:
                print('There was no one to talk to.')
        elif (chapter == '3'):
            if (c3Switch[2] == False and c3Switch[3] == True):
                print('1: Rat')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Alder did not want to get too close to the rat. Even if he could not touch or speak to him.')
            else:
                print('There was no one to talk to.')
                    
    elif(location == '7'):
        if(c2Switch[3] == False):
            print('1: Mouse')
            t = input('Talk to: ')
            if (t == '1'):
                print('Mouse:')
                print('"..."')
                cont()
                print('The mouse smimled warmly at Alder, but did not say a word.')
                cont()
        else:
            print('There was no one to talk to.')
    else:
        print('There was no one to talk to.')
#Move to another location
def move():
    global location, part, tutorial1, tutorialSwitch, c2Switch, c3Switch
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
                print('With the Gowl'"'"'s outside it wasn'"'"'t worth risking.')
            else:
                location = '3'
                if(c3Switch[5] == False):
                    print('The group exited the cottage through the back door.')
                else:
                    print('Alder exited the cottage through the front door.')
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
            print('Alder entered the shed at the side of the cottage.')  
            alder.stamina -= 1  
            cont()
        elif (m == '3'):
            if (mQuests[0]['accepted'] == True and mQuests[0]['completed'] == False and alder.weapon1['wpId'] != '0'):
                location = '6'
                print('Alder left the cottage grounds.')
                alder.stamina -= 1    
                cont()
            else:
                print('It'"'"'s dangerous to leave the cottage grounds unarmed.')
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
                print('Alder left the shed and returned to the front of the cottage.')
                alder.stamina -= 1
                cont()
    elif (location == '5'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            if (chapter == '3' and c3Switch[0] == True):
                print('Alder jumped out of bed and hurriedly knocked on Florace'"'"'s door. She soon groggily came out.')
                cont()
                print('Florace:')
                print('*Groan*')
                cont()
                print('Florace:')
                print('"Alder, it'"'"'s really early, don’t wake me."')
                cont()
                print('Florace gave Alder an annoyed look before she noticed the sword in his hands.')
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
                print('She was confused by Alder'"'"'s response and it was clear she was sceptical.')
                cont()
                print('Kyla:')
                print('"Heh Heh."')
                cont()
                print('Kyla:')
                print('"What'"'"'s this about a sword?"')
                cont()
                print('Kyla had come out of her room somewhat amused by Floraces shouts. When she looked at Alder her eyes widened as she noticed the sword that Alder had.')
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
                print('Alder hands the sword over to Kyla and with Floraces assistance she took it to the table downstairs.')
                cont()
                print('Kyla:')
                print('"It can’t be?"')
                cont()
                print('Kyla:')
                print('"Boy, in the bookshelf, there should be a blue book on magical artefacts, bring it here."')
                cont()
                print('Kyla:')
                print('"Look for the page that has this sword in it."')
                cont()
                print('Alder:')
                print('"Right."')
                c3Switch[0] = False
            else:
                print('Alder moved downstairs into the living room.')
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
                print('Florace was having a conversation with Thay. When they looked at Alder they immediately noticed the swollen red marks where the hornets had stung his exposed skin.')
                cont()
                print('Florace:')
                print('"Alder what happened? Are you ok!?"')
                cont()
                print('Alder:')
                print('"Um..."')
                cont()
                print('Alder was briefly suprised by Florace'"'"'s concern, but he knew she could get paranoid when it can to his safety.')
                cont()
                print('Alder:')
                print('"I got stung by hornets a few times but I'"'"'m alright!"')
                cont()
                print('Florace:')
                print('*Sigh*')
                cont()
                print('Florace:')
                print('"Give the bugs and the knife to me and go relax yourself."')
                cont()
                print('Thay:')
                print('"Here some plantain might ease your discomfort."')
                cont()
                print('Alder passed the bug meat and the hunting knife over to her. Florace went inside the cottage to prepare the crickets for supper while Thay applied poultice of greater plantain to Alder stings.')
                for i in inv:
                    if (i['type'] == ItemType.food):
                        if (i['itemId'] == '5'):
                            inv.remove(i)
                alder.weapon1 = weapons[0]
                alder.health += 10
                print('\nHunting Knife unequipped')
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
            print('Kyla had been indifferent to the incident.')
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
                if (i['type'] == ItemType.food):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'healing' or j == 'Healing' or
            j == 'health' or j == 'Health'):
            print('Healing')
            for i in inv:
                if (i['type'] == ItemType.healing):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'projectiles' or j == 'Projectiles'):
            print('Projectiles')
            for i in inv:
                if (i['type'] == ItemType.projectile):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'weapons' or j == 'Weapons'):
            print('Weapons')
            for i in inv:
                if (i['type'] == Weapon1Type.sword or i['type'] == Weapon1Type.dagger or i['type'] == Weapon1Type.spear or
                   i['type'] == Weapon1Type.axe or i['type'] == Weapon1Type.mace or i['type'] == Weapon1Type.staff or
                    i['type'] == Weapon2Type.bow or i['type'] == Weapon2Type.shield or i['type'] == Weapon2Type.crossbow or i['type'] == Weapon2Type.sling):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'armour' or j == 'Armour'):
            print('armour')
            for i in inv:
                if (i['type'] == ArmourType.hat or i['type'] == ArmourType.shirt or i['type'] == ArmourType.trousers):
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
                    if (i['type'] != ItemType.food):
                        print('Name: ', i['name'], ' - Type: ', i['type'].name, ' - \nDescription: ', i['description'])
                    else:
                        print('Name: ', i['name'], ' - Type: ', i['type'].name, ' - \nStamina Recovered: ', i['recovers'])
                count += 1
        elif (j == '2'):
            useItem(alder)
        elif (j == '3'):
            equip(alder)
        elif (j == 'e'):
            bag = False
        if (j == '1' or j == '2' or j == '3'):
            j = ''
    
#Achive objectives
def achive():
    for q in mQuests:
        if(q['accepted'] == True and q['submitted'] != True):
            if (q['questId'] == '1'):
                amount = 0
                for i in inv:
                    if (i['type'] == ItemType.food):
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
                            if (i['type'] == ItemType.food):
                                if (i['itemId'] == '5'):
                                    amount += i['count']
                        print('\t', q['desc'],' (',amount,'/',q['qnt'],')')
    elif(tutorialSwitch[6] == True):
        print('\tReturn to the cottage and examine to bed to end the day.')
        print('\tTalk to characters if a character has a "!" mark then they will quest for Alder.')
    elif(c2Switch[0] == True):
        print('\tMove to the living room to attend meeting.')
    elif(c2Switch[1] == True):
        print('\tTalk to Trissie for archery practice')
    elif(c2Switch[2] == True):
        print('\tGo to bed.')
    elif(c2Switch[3] == True):
        print('\tExplore strange place.')
    elif(c3Switch[0] == True and chapter == '2'):
        print('\tTake sword!')
    elif(c3Switch[0] == True and chapter == '3'):
        print('\tGet Florace!')
    elif(c3Switch[1] == True):
        print('\tRead "Read Magical articles of history".')
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
                                if(l['type'] == ItemType.food):
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
    print("\nCommand: e, examine, Examine - Allows Alder to investigate his surroundings. Examinating further may reveal an item you can pickup.")
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
    print("Command: q, quit, Quit - Exit to the main menu")

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
            print('While we wait for Thay, let'"'"'s "talk"("t") to Florace.')
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
                equip(alder)
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
                            print(newline[0],'\n',newline[1].strip('\n'))
                        else:
                            print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
                            s = input()
                            if(s == 'skip'):
                                skip = True
                f.close()
                chapter = '3'
                part = '1'
                switch[9] = False
                switch[10] = True
                part = '1'
            elif (game_active == True):
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
                                print(newline[0],'\n',newline[1].strip('\n'))
                            else:
                                print(line[4].strip('\n'))
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
