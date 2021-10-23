import os
import random
import pickle
from data import typeSpf
from data import playableChars
from data import enemyUnits
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

#Enemy Units
class Null:
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'

def gainExperience(p):
    experience = input('Increase experience by how much?: ')
    if (experience.isdigit()):
        e = int(experience)
        p.cExp += e
    else:
        print('Number values only!')
    
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
                   

#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : Weapon1Type.sword, 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : Weapon1Type.sword, 'description' : 'Legendary sword of the Scion.',
            'attack' : 500, 'weight' : 5, 'count' : 0},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : Weapon1Type.dagger, 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0},
           {'wpId' : '3', 'name' : 'Relic Sword', 'type' : Weapon1Type.sword, 'description' : '',
            'attack' : 10, 'weight' : 3, 'count' : 0},
           {'wpId' : '4', 'name' : 'Relic Spear', 'type' : Weapon1Type.spear, 'description' : '',
            'attack' : 8, 'weight' : 3, 'count' : 0},
           {'wpId' : '5', 'name' : 'Relic Axe', 'type' : Weapon1Type.axe, 'description' : '',
            'attack' : 12, 'weight' : 3, 'count' : 0},
           {'wpId' : '6', 'name' : 'Old Club', 'type' : Weapon1Type.mace, 'description' : '',
            'attack' : 10, 'weight' : 4, 'count' : 0},
           {'wpId' : '7', 'name' : 'Crooked Stick', 'type' : Weapon1Type.staff, 'description' : '',
            'attack' : 3, 'weight' : 2,
            'spId' : ['0'], 'spells' : [''],'count' : 0},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : Weapon2Type.bow, 'description' : 'A large bow made for practise.',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Crossbow', 'type' : Weapon2Type.crossbow, 'description' : '',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Grass Sling', 'type' : Weapon2Type.sling, 'description' : 'A sling made from grass; not very practical',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Wooden Shield', 'type' : Weapon2Type.shield, 'description' : 'A basic round wooden shield.',
            'defence' : 20, 'weight' : 4, 'count' : 0},
           {'wpId' : '1', 'name' : 'Poison wand', 'type' : Weapon2Type.wand, 'description' : 'A wand containing a weak poison',
            'spId' : '1', 'spell' : 'Poison Nettle', 'weight' : 1, 'count' : 0},
           {'wpId' : '8', 'name' : 'Mushroom staff', 'type' : Weapon1Type.staff, 'description' : '',
            'attack' : 3, 'weight' : 2,
            'spId' : ['2', '3', '4'], 'spells' : ['Grow mushrooms','Grow mushrooms','Grow mushrooms'], 'count' : 0}
           ]

armours = [{'armId' : '1', 'name' : 'None', 'type' : ArmourType.hat, 'description' : '',
          'defence' : 0, 'weight' : 0, 'count' : 0},
          {'armId' : '1', 'name' : 'Old Tunic', 'type' : ArmourType.shirt, 'description' : 'An old shirt with holes in it.',
          'defence' : 1, 'weight' : 1, 'count' : 0},
          {'armId' : '2', 'name' : 'Travelling Cloak', 'type' : ArmourType.shirt, 'description' : 'A too large black cloak. Good for keeping ou of sight but heavy.',
          'defence' : 10, 'weight' : 10, 'count' : 0},
          {'armId' : '1', 'name' : 'Worn Trousers', 'type' : ArmourType.trousers, 'description' : 'An old pair of trousers long past their prime',
          'defence' : 1, 'weight' : 1, 'count' : 0}
          ]
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : ItemType.food,
          'recovers' : 3, 'count' : 0},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : ItemType.food,
          'recovers' : 3, 'count' : 0},
        {'itemId' : '4', 'name' : 'Raw Bug Meat', 'type' : ItemType.food,
          'recovers' : 10, 'count' : 0}
        ]
projec = [{'itemId' : '1', 'name' : 'Primitive Arrow', 'type' : ItemType.projectile, 'description' : 'Arrows made from stone heads and twigs.',
           'weapon' : Weapon2Type.bow, 'damage' : 10, 'count' : 0},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : ItemType.toss,  'description' : 'A rope net to catch your enemies.',
           'weapon' : 'none', 'damage' : 0, 'count' : 0},
          {'itemId' : '3', 'name' : 'Wooden Bolt', 'type' : ItemType.projectile,  'description' : '',
           'weapon' : Weapon2Type.crossbow, 'damage' : 10, 'count' : 0},
          {'itemId' : '4', 'name' : 'Softstone', 'type' : ItemType.projectile,  'description' : '',
           'weapon' : Weapon2Type.sling, 'damage' : 10, 'count' : 0}
          ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : ItemType.healing, 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0}
         ]
#Universal Specials
manuvers = [{'spId':'1','name':'Advence', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
           {'spId':'2','name':'Retreat', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
           ]
spells = [{'spId':'1','name':'Poison nettles', 'type':SpecialType2.offence, 'specialType':SpecialType1.spell, 'spellType':SpellType.Nature, 'attackType' : AttackType.single, 'damage' : 1, 'cost':10, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Poisons an opponent'},
          {'spId':'2','name':'Grow mushrooms', 'type':SpecialType2.offence, 'specialType':SpecialType1.spell, 'spellType':SpellType.Nature, 'attackType' : AttackType.single, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Grow mushrooms on your enemy to hinder them.'},
          {'spId':'3','name':'Grow mushrooms', 'type':SpecialType2.enhance, 'specialType':SpecialType1.spell, 'spellType':SpellType.Nature, 'attackType' : AttackType.single, 'damage' : 9, 'cost':0, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':"Grow edable mushrooms for an ally to restore stamina."},
          {'spId':'4','name':'Grow mushrooms', 'type':SpecialType2.support, 'specialType':SpecialType1.spell, 'spellType':SpellType.Nature, 'attackType' : AttackType.single, 'damage' : 9, 'cost':0, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Grow edable mushrooms for the caster to restore stamina.'}
          ]
combinations = [{'spId':'comb1','name':'Poisonous mushrooms', 'type':SpecialType2.offence, 'specialType':SpecialType1.spell, 'spellType':SpellType.Nature, 'attackType' : AttackType.single, 'damage' : 9, 'cost':0, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False,
                 'components':['1', '2'],'effect':'Grow poisinous mushrooms on the enemy.'}
          ]
#Inventory
inv = []
#Set playable characters
alder = playableChars.Alder()
florace = playableChars.Florace()

#Save settings
def save():
    data = [alder, florace, inv]
    PIK = 'data/combat_file.dat'
    with open(PIK, "wb") as f:
        pickle.dump(data, f)
    print ('Data Saved!')
    
def loadSet():
    global alder, florace, inv
    PIK = 'data/combat_file.dat'
    try:
        with open(PIK, "rb") as f:
            data = pickle.load(f)
            alder = data[0]
            florace = data[1]
            inv = data[2]
    except:
        print('Saved file not found!')
    print ('Data Loaded!')
    

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
                item['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.shield and i['type'] == Weapon2Type.shield):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == Weapon2Type.bow and i['type'] == Weapon2Type.bow):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
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
                item['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.healing and i['type'] == ItemType.healing):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.projectile and i['type'] == ItemType.projectile):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == ItemType.toss and i['type'] == ItemType.toss):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] += amount
        inv.append(item)

#Items Setter
def equip(p):
    equiping = True
    while (equiping == True):
        equipable = []
        print('\nEquip')
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
                        print(i['name'], 'equiped')
                        if(p.head['armId'] != '0'):
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
                        print(i['name'], 'equiped')
                        if(p.body['armId'] != '1'):
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
                        print(i['name'], 'equiped')
                        if(p.legs['armId'] != '1'):
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
        save()

#Open the inventory
def inventory():
    bag = True
    while(bag == True):
        #View the items in inventory
        print('\nInventory')
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
                    if (i['type'] != ItemType.food):
                        print('Name: ', i['name'], ' - Type: ', i['type'].name, ' - \nDescription: ', i['description'])
                    else:
                        print('Name: ', i['name'], ' - Type: ', i['type'].name, ' - \nStamina Recovered: ', i['recovers'])
                count += 1
        elif (i == '2'):
            print('1: Alder')
            print('2: Florace')
            i = input('Item set:')
            if (i == '1'):
                equip(alder)
            elif (i == '2'):
                equip(florace)
        elif (i == 'e'):
            print()
            bag = False
            
def equipment():
    manageEquip = True
    while (manageEquip == True):
        print('\n1: Items.')
        print('2: Inventory.')
        print('3: Equip.')
        print('e - Exit')
        i = input('Set: ')
        if (i == '1'):
            print('\nItem Sets')
            print('1: primary weaponry')
            print('2: secondary weaponry')
            print('3: health and stamina items')
            j = input('Item set:')
            if (j == '1'):
                print('\nDagger obtained')
                itemCount(weapons[2], 1)
                print('\nLeif obtained')
                itemCount(weapons[1], 1)
                print('\nSword obtained')
                itemCount(weapons[3], 1)
                print('\nSpear obtained')
                itemCount(weapons[4], 1)
                print('\nAxe obtained')
                itemCount(weapons[5], 1)
                print('\nClub obtained')
                itemCount(weapons[6], 1)
                print('\nStaff obtained')
                itemCount(weapons[7], 1)
                print('\nStaff obtained')
                itemCount(weapons[13], 1)
            elif (j == '2'):
                print('\nBow obtained')
                itemCount(weapons[8], 1)
                print('\nCrossbow obtained')
                itemCount(weapons[9], 1)
                print('\nSling obtained')
                itemCount(weapons[10], 1)
                print('\nShield obtained')
                itemCount(weapons[11], 1)
                print('\nWand obtained')
                itemCount(weapons[12], 1)
                print('\nArrows obtained')
                itemCount(projec[0], 5)
                print('\nNet obtained')
                itemCount(projec[1], 1)
                print('\nBolts obtained')
                itemCount(projec[2], 5)
                print('\nStones obtained')
                itemCount(projec[3], 5)
            elif (j == '3'):
                print('\nBlackberries obtained')
                itemCount(food[0], 5)
                print('\nBandage obtained')
                itemCount(items[0], 5)
            save()
        elif (i == '2'):
            inventory()
        elif (i == '3'):
            print('1: Alder')
            print('2: Florace')
            j = input('Item set:')
            if (j == '1'):
                equip(alder)
            elif (j == '2'):
                equip(florace)
        elif (i == 'e'):
            manageEquip = False

def setFoe():
    global enemy
    setting = True
    heroes = [alder, florace]
    enemy = [Null(), Null(), Null()]
    null = Null()
    while (setting == True):
        print('\nSet enemies')
        print('1: Enemy 1 -', enemy[0].name)
        print('2: Enemy 2 -', enemy[1].name)
        print('3: Enemy 3 -', enemy[2].name)
        print('4: Fight')
        print('e - exit')
        i = input('Select: ')
        if (i == '1'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
            j = input('Enemy: ')
            if (j == '1'):
                enemy[0] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[0] = enemyUnits.Wasp()
            elif (j == '3'):
                enemy[0] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[0] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[0] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[0] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[0] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[0] = enemyUnits.SwordMaster()
        elif (i == '2'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
            print('c - Blank')
            j = input('Enemy: ')
            if (j == 'c'):
                enemy[1] = enemyUnits.Null()
            elif (j == '1'):
                enemy[1] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[1] = enemyUnits.Wasp()
            elif (j == '3'):
                enemy[1] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[1] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[1] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[1] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[1] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[1] = enemyUnits.SwordMaster()
        elif (i == '3'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
            print('c - Blank')
            j = input('Enemy: ')
            if (j == 'c'):
                enemy[2] = enemyUnits.Null()
            elif (j == '1'):
                enemy[2] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[2] = enemyUnits.Wasp()
            elif (j == '3'):
                enemy[2] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[2] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[2] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[2] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[2] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[2] = enemyUnits.SwordMaster()
        elif (i == '4'):
            if(enemy[0].enId != null.enId):
                victory = False
                enemy[0].inId = '1'
                enemy[1].inId = '2'
                enemy[2].inId = '3'
                victory = battle(heroes, enemy)
                if (victory == True):
                    print('You won the fight!')
                else:
                    print('You lost the fight!')
                setting = False
            else:
                print('Please press "1" and select an enemy to fight.')
        elif (i == 'e'):
            setting = False
    
def win(e):
    ex = 0
    rewards = []
    count = 0
    print('\n')
    for i in e:
        ex += i.Exp
        count += 1
    if (alder.active == True):
        alder.cExp += ex
        print('Alder gained ', ex, ' experience.')
        levelUP(alder)
    if (florace.active == True):
        florace.cExp += ex
        print('Florace gained ', ex, ' experience.')
        levelUP(florace)
    for i in e:
        if (len(i.drop) > 0):
            print(i.name,' dropped ', i.drop[0]['item']['name'], ' x', i.drop[0]['quantity'])
            itemCount(i.drop[0]['item'], i.drop[0]['quantity'])
    save()

def death():
    for i in alder.abilities:
        i['active'] = False
        i['inEffect'] = 0
    alder.health = alder.maxHealth
    alder.stamina = alder.maxHealth
    florace.health = florace.maxHealth
    florace.stamina = florace.maxHealth
    print('\nAlder was slain.')
    i = input()
    dostuff = False

def hunger(p):
    if(p.stamina <= 0):
        p.health -= 1
        print(p.name,'needs to eat!')
    if(p.stamina < 0):
        p.stamina = 0



def enemyFlee(e):
    print(e.name, ' fled!')

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
            p.cStatus = CombatStatus.RAttacking
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
                print(p.aliment['outRange'])
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

#Check if special effect are still active and deactivate them it they are not.
def inEffect(p, e):
    for i in alder.abilities:
        if(i['active'] == True):
            i['inEffect'] -= 1
            if (i['inEffect'] <= 0):
                i['active'] = False
                print(alder.name,"'s ", i['name'], ' has worn off.')
    for i in p.manver:
        for en in e:
            if (i['spId'] == '1' and (p.aliment['outRange'] == 'True' or en.aliment['outRange'] == 'True')):
                advencable = False
                if (en.aliment['outRange'] == 'False'):
                    advancable = False
                else:
                    advancable = True
                if (advancable == True):
                    j = i + 1
                    i['active'] = True
                    j['active'] = False
                    print(i, j)
            elif (i['spId'] == '2' and (p.aliment['outRange'] == 'False')):
                j = i - 1
                i['active'] = True
                j['active'] = False


def magic(p, t, e, spell):
    hit = random.randrange(0,100)
    damage = spell['damage']
    if (p.weapon1['type'] == Weapon1Type.staff):
        boost = damage / 20
        if (boost < 1):
            boost = 1
        damage += round(boost)
    count = 1
    if (spell['type'] == SpecialType2.offence):
        for i in e:
            print(count, ') ', i.name)
            count += 1
    elif (spell['type'] == SpecialType2.support):
        for i in t:
            if (i.pId != p.pId):
                print(count, ') ', i.name)
                count += 1
    if (hit < spell['effectivness']):
        if (spell['type'] == SpecialType2.offence):
            target = input('Cast on:')
            if (spell['attackType'] == AttackType.single):
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
        if (spell['type'] == SpecialType2.support):
            target = input('Cast on:')
            if (spell['attackType'] == AttackType.single):
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
        if (spell['type'] == SpecialType2.enhance):
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
        elif(offensive['specialType'] == SpecialType1.spell):
            magic(p, h, e, offensive)
            print('\n', p.name, ' uses ', offensive['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':'magic', 'Spell':offensive['name']})
    elif ((sp == "3" or sp == "support") and support['spId'] != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= support['cost']
        if(offensive['specialType'] == SpecialType1.manuver):
            manuver(p,e,support)
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':support['name']})
        elif(offensive['specialType'] == SpecialType1.spell):
            magic(p, h, e, support)
            print('\n', p.name, ' uses ', support['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':'magic', 'Spell':support['name']})
    if ((sp == "4" or sp == "enhance") and enhance['spId'] != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= enhance['cost']
        if(enhance['specialType'] == SpecialType1.manuver):
            manuver(p,e,enhance)
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':enhance['name']})
        elif(enhance['specialType'] == SpecialType1.spell):
            magic(p, h, e, enhance)
            print('\n', p.name, ' uses ', offensive['name'],'.')
            r.append({'Id': p.pId, 'Who':p.name, 'Type': p.type, 'Status':p.cStatus, 'SpecialType':'magic', 'Spell':enhance['name']})

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
                                alder.cStatus = CombatStatus.Using
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
                    r.append({'Id': i.pId, 'Who':p.name, 'Type': i.type, 'Status':p.cStatus, 'ItemType':i['type']})
                count +=1
            if u == 'e':
                using = False
            use.clear()
#Combat order
def fightOrder(e):
    return e.speed()
#Enemy Priorities
#Attacks the enemy with the least health
def ePriority_weakness(heroes):
    heroes.sort(key=lambda x: x.health, reverse=False)
    for i in heroes:
        if (i.health > 0):
            return i
#Attacks the enemy that dealt the most damge
def ePriority_threat(heroes, record):
    attacks = []
    for i in record:
        if (i['Type'] == 'playable' and i['Status'] == CombatStatus.Attacking):
            attacks.append(i)
    attacks.sort(key=lambda x: x['Damage'], reverse=True)
    for i in attacks:
        for j in heroes:
            if (i['Id'] == j.pId):
                if (j.health > 0):
                    return j
    if (len(attacks) == 0):
        return ePriority_weakness(heroes)
#Attacks the last enemy to attack it
def ePriority_retaliation(heroes, e, record):
    attacks = []
    for i in record:
        if (i['Type'] == 'playable' and i['Status'] == CombatStatus.Attacking and
            i['Hit'].inId == e.inId):
                attacks.append(i)
    for i in attacks:
        for j in heroes:
            if (i['Id'] == j.pId):
                if (j.health > 0):
                    return j  
    if (len(attacks) == 0):
        return ePriority_weakness(heroes)
#Attacks Alder if he is active in combat
def ePriority_Alder(heroes):
    for i in heroes:
        if (i.health > 0):
            if (i.pId == '1'):
                return i
            elif (i.pId == '2'):
                return i
            else:
                return ePriority_weakness(heroes)

#Combat interface
def battle(h, e):
    os.system('clear')
    global alder, florace
    heroes = []
    enemys = []
    record = []
    for i in h:
        if (i.active == True):
            heroes.append(i)
    for i in e:
        if i.enId != '0':
            enemys.append(i)
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
        #print(combatants)
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
                    #record.append({'Who':i.name, 'Status':'defeated'})
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
                    for i in record:
                        print(i)
                    return True
                if (i.type == 'playable' and i.health > 0):
                    #Automatic special
                    automatic = i.special_auto()
                    if(automatic['spId'] != '0'):
                        if(automatic['specialType'] == SpecialType1.manuver):
                            manuver(i,e,automatic)
                            print('\n',automatic['name'],'is active.')
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'SpecialType':SpecialType1.manuver, 'Manuver':automatic['name']})
                        elif(automatic['specialType'] == SpecialType1.spell):
                            magic(i, h, e, automatic)
                            print('\n',automatic['name'],'is active.')
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'SpecialType':'magic', 'Spell':automatic['name']})
                    inEffect(i, enemys)
                    i.cStatus = CombatStatus.Normal
                    while(i.cStatus == CombatStatus.Normal):
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
                            #if (alder.cStatus == CombatStatus.Blocking and impact > 0):
                                #shield -= impact
                for j in reversed(enemys):
                    if (j.cStatus == CombatStatus.Escaping):
                        enemys.remove(j)
                        if (len(enemys) == 0):
                            fighting = False
                            return True
        count += 1

def unit():
    units = True
    while(units == True):
        print('\n1: Print stats.')
        print('2: Add experience')
        print('3: Recover')
        print('4: Reset')
        print('e - Exit')
        a = input('Action: ')
        if (a == '1'):
            alder.stats()
            florace.stats()
        elif (a == '2'):
            a = input('Action: ')
            if (a == '1'):
                gainExperience(alder)
                levelUP(alder)
            elif (a == '2'):
                gainExperience(florace)
                levelUP(florace)
        elif (a == '3'):
            alder.health = alder.maxHealth
            alder.stamina = alder.maxStamina
            florace.health = florace.maxHealth
            florace.stamina = florace.maxStamina
        elif (a == '4'):
            alder.maxHealth = 100
            alder.health = alder.maxHealth
            alder.maxStamina = 100
            alder.stamina = alder.maxStamina
            alder.cLvl = 1
            alder.cExp = 0
            alder.cNext = 30
            alder.skillPoints = 0
            alder.baseAttack = 10
            alder.baseDefence = 10
            alder.baseAccuracy = 5
            alder.baseSpeed = 10
            alder.baseEvasion = 5
            alder.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
            alder.cStatus = CombatStatus.Normal
            alder.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                              {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                              {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                              {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                              {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                              {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                              {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                              ]
            
            florace.maxHealth = 150
            florace.health = florace.maxHealth
            florace.maxStamina = 80
            florace.stamina = florace.maxStamina
            florace.cLvl = 1
            florace.cExp = 0
            florace.cNext = 30
            florace.skillPoints = 0
            florace.baseAttack = 6
            florace.baseDefence = 14
            florace.baseAccuracy = 10
            florace.baseSpeed = 11
            florace.baseEvasion = 4
            florace.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
            florace.cStatus = CombatStatus.Normal
            florace.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                              {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                              {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                              {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                              {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                              {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                              {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                              ]
        elif (a == 'e'):
            units = False
def active():
    loadSet()
    dostuff = True
    while(dostuff == True):
        print('\n1: Player stats.')
        print('2: Set equipment.')
        print('3: Fight')
        a = input('Action: ')
        if (a == '1'):
            unit()
        elif (a == '2'):
            equipment()
        elif (a == '3'):
            setFoe()
active()
