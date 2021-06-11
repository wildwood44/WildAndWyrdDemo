import os
import random
#Character Base Stats
class Alder:
    def __init__(self):
        self.pId = '1'
        self.name = 'Alder'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStamina = 100
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
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
        self.weapon1 = weapons[0]
        self.weapon2 = weapons[0]
        self.aliment = 'None'
        self.cStatus = 'None'
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':True, 'effect':'Increases Evasion for five turns.'},
                        {'spId':'2','name':'Master archer', 'cost':10, 'active':False, 'inEffect':0, 'unlocked':False, 'effect':'Grants a critical for the next arrow fired within the next four turns.'}
                        ]
        self.spells = [{'spId':'1','name':'Poison nettles', 'type':'Nature', 'attackType' : 'single', 'cost':10, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Poisons an opponent'}
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
    property
    def spell(self):
        if (self.weapon2['type'] == 'wand'):
            if(self.weapon2['spId'] == '1'):
                return self.spells[0]['unlocked'] == True
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nAccuracy: ', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2, '\n'
              )
#Enemy Units
class Cricket:
    def __init__(self):
        self.enId = '1'
        self.name = 'Cricket'
        self.maxHealth = 20
        self.health = self.maxHealth
        self.type = 'bug'
        self.Exp = 10
        self.drop = [{'item' : food[3], 'quantity':2}]
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

class Wasp:
    def __init__(self):
        self.enId = '2'
        self.name = 'Wasp'
        self.maxHealth = 10
        self.health = self.maxHealth
        self.type = 'bug'
        self.Exp = 10
        self.drop = [{'item':food[3], 'quantity':1}]
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
        self.type = 'puppet'
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
class Wall:
    def __init__(self):
        self.enId = '4'
        self.name = 'Wall'
        self.maxHealth = 500
        self.health = self.maxHealth
        self.type = 'Puzzle'
        self.Exp = 5
        self.drop = []
        self.baseAttack = 0
        self.baseDefence = 400
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
    
class Gowl_Rabbit:
    def __init__(self):
        self.enId = '5'
        self.name = 'Gowls Captain Clipgrea'
        self.maxHealth = 12000
        self.health = self.maxHealth
        self.type = 'soldier'
        self.Exp = 0
        self.drop = []
        self.baseAttack = 900
        self.baseDefence = 750
        self.baseAccuracy = 200
        self.baseSpeed = 1700
        self.baseEvasion = 1800
        self.strat = 'Attacker'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.desc = 'A Gowls Captain. There'"'"'s a reason for that. Well equiped and fast as rabbits are.'
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

class Null:
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'

def gainExperience():
    experience = input('Increase experience by how mush?: ')
    e = int(experience)
    #if isinstance(experience, int):
    alder.cExp += e
    print(e)
    
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
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'sword', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'sword', 'description' : 'Legendary sword of the Scion.',
            'attack' : 500, 'weight' : 5, 'count' : 0},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'dagger', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0},
           {'wpId' : '3', 'name' : 'Relic Sword', 'type' : 'sword', 'description' : '',
            'attack' : 5, 'weight' : 3, 'count' : 0},
           {'wpId' : '4', 'name' : 'Relic Spear', 'type' : 'spear', 'description' : '',
            'attack' : 5, 'weight' : 3, 'count' : 0},
           {'wpId' : '5', 'name' : 'Relic Axe', 'type' : 'axe', 'description' : '',
            'attack' : 5, 'weight' : 3, 'count' : 0},
           {'wpId' : '6', 'name' : 'Old Club', 'type' : 'mace', 'description' : '',
            'attack' : 5, 'weight' : 4, 'count' : 0},
           {'wpId' : '7', 'name' : 'Crooked Stick', 'type' : 'staff', 'description' : '',
            'attack' : 5, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : 'bow', 'description' : 'A large bow made for practise.',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Crossbow', 'type' : 'crossbow', 'description' : '',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Grass Sling', 'type' : 'sling', 'description' : 'A sling made from grass, not very practical',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Wooden Sheild', 'type' : 'sheild', 'description' : 'A basic round wooden sheild.',
            'defence' : 20, 'weight' : 4, 'count' : 0},
           {'wpId' : '1', 'name' : 'Poison wand', 'type' : 'wand', 'description' : 'A wand containing a weak poison',
            'spell' : 'Poison Nettle', 'weight' : 1, 'count' : 0}
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
          'recovers' : 3, 'count' : 0},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : 'food',
          'recovers' : 5, 'count' : 0},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : 'food',
          'recovers' : 3, 'count' : 0},
        {'itemId' : '4', 'name' : 'Raw Bug Meat', 'type' : 'food',
          'recovers' : 10, 'count' : 0}
        ]
projec = [{'itemId' : '1', 'name' : 'Primative Arrow', 'type' : 'projectile',
           'weapon' : 'bow', 'damage' : 10, 'count' : 0},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : 'toss',
           'weapon' : 'none', 'damage' : 0, 'count' : 0},
          {'itemId' : '3', 'name' : 'Wooden Bolt', 'type' : 'projectile',
           'weapon' : 'crossbow', 'damage' : 10, 'count' : 0},
          {'itemId' : '4', 'name' : 'Softstone', 'type' : 'projectile',
           'weapon' : 'sling', 'damage' : 10, 'count' : 0}
          ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0}
         ]

#Inventory
inv = []
#Set Class
alder = Alder()

#Increment items
#Add a new item to the inventory if is is not already in there
def itemCount(item, amount):
    inInv = False
    for i in inv:
        if (item['type'] == 'sword' and i['type'] == 'sword' or
            item['type'] == 'dagger' and i['type'] == 'dagger' or
            item['type'] == 'spear' and i['type'] == 'spear' or
            item['type'] == 'axe' and i['type'] == 'axe' or
            item['type'] == 'mace' and i['type'] == 'mace' or
            item['type'] == 'staff' and i['type'] == 'staff'):
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
        elif (item['type'] == 'crossbow' and i['type'] == 'crossbow'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'sling' and i['type'] == 'sling'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'sheild' and i['type'] == 'sheild'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'wand' and i['type'] == 'wand'):
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
    if (inInv == False):
        item['count'] += amount
        inv.append(item)

#Items Setter
def equip():
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
                if(i['type'] == 'sword' or i['type'] == 'dagger' or i['type'] == 'spear' or
                   i['type'] == 'axe' or i['type'] == 'mace' or i['type'] == 'staff'):
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
                if(i['type'] == 'bow' or i['type'] == 'crossbow' or i['type'] == 'sling' or
                   i['type'] == 'sheild' or i['type'] == 'wand'):
                    count +=1
                    equipable.append(i)
                    if(i['type'] == 'bow'):
                        if (alder.weapon2['type'] == 'bow' or alder.weapon2['type'] == 'crossbow' or alder.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'crossbow'):
                        if (alder.weapon2['type'] == 'bow' or alder.weapon2['type'] == 'crossbow' or alder.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'sling'):
                        if (alder.weapon2['type'] == 'bow' or alder.weapon2['type'] == 'crossbow' or alder.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - alder.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'sheild'):
                        if (alder.weapon2['type'] == 'sheild'):
                            print(count, ': ', i['name'], '- Defence: +', i['defence'] - alder.weapon2['defence'])
                        else:
                            print(count, ': ', i['name'], '- Defence: +', i['defence'])
                    elif(i['type'] == 'wand'):
                        print(count, ': ', i['name'], '- Spell: ', i['spell'])
                        for j in alder.spells:
                            if (j['spId'] == i['wpId']):
                                j['unlocked'] = True
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
            elif (j == '2'):
                print('\nBow obtained')
                itemCount(weapons[8], 1)
                print('\nCrossbow obtained')
                itemCount(weapons[9], 1)
                print('\nSling obtained')
                itemCount(weapons[10], 1)
                print('\nSheild obtained')
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
        elif (i == '2'):
            inventory()
        elif (i == '3'):
            equip()
        elif (i == 'e'):
            manageEquip = False

def setFoe():
    global enemy
    setting = True
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
            j = input('Enemy: ')
            if (j == '1'):
                enemy[0] = Cricket()
            elif (j == '2'):
                enemy[0] = Wasp()
            elif (j == '3'):
                enemy[0] = Dummy()
            elif (j == '4'):
                enemy[0] = Wall()
            elif (j == '5'):
                enemy[0] = Gowl_Rabbit()
        elif (i == '2'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('c - Blank')
            j = input('Enemy: ')
            if (j == 'c'):
                enemy[1] = Null()
            elif (j == '1'):
                enemy[1] = Cricket()
            elif (j == '2'):
                enemy[1] = Wasp()
            elif (j == '3'):
                enemy[1] = Dummy()
            elif (j == '4'):
                enemy[1] = Wall()
            elif (j == '5'):
                enemy[0] = Gowl_Rabbit()
        elif (i == '3'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('c - Blank')
            j = input('Enemy: ')
            if (j == 'c'):
                enemy[2] = Null()
            elif (j == '1'):
                enemy[2] = Cricket()
            elif (j == '2'):
                enemy[2] = Wasp()
            elif (j == '3'):
                enemy[2] = Dummy()
            elif (j == '4'):
                enemy[2] = Wall()
            elif (j == '5'):
                enemy[0] = Gowl_Rabbit()
        elif (i == '4'):
            if(enemy[0].enId != null.enId):
                victory = False
                victory = battle(enemy)
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
    alder.cExp += ex
    print('Alder gained ', ex, ' experience.')
    levelUP(alder)
    for i in e:
        if (len(i.drop) > 0):
            print(i.name,' dropped ', i.drop[0]['item']['name'], ' x', i.drop[0]['quantity'])
            itemCount(i.drop[0]['item'], i.drop[0]['quantity'])

def death():
    for i in alder.special:
        i['active'] = False
        i['inEffect'] = 0
    alder.health = alder.maxHealth
    alder.stamina = alder.maxHealth
    print('\nAlder was slain.')
    i = input()
    dostuff = False

def hunger():
    if(alder.stamina <= 0):
        alder.health -= 1
        print('You need to eat!')
    if(alder.stamina < 0):
        alder.stamina = 0

def battleOrder(speedList):
    n = len(speedList)
    for i in range(n - 1) :
        flag = 0
        for j in range(n - 1) :
            if (speedList[j] > speedList[j+1]):
                temp = speedList[j]
                speedList[j] = speedList[j+1]
                speedList[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return speedList

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
            im = impact
            if (p.cStatus == 'Blocking'):
                impact = round(impact/10)
                if (impact <= 0):
                    impact = 1
                im = impact
                if (b > 0):
                    print('Attack blocked!')
                    impact -= b
                    if (impact < 0):
                        impact = 0
            p.health -= impact
            print('\n',e.name,' attacked!')
            if(critical >= 90):
                print('Critical Hit!')
            print(p.name, ' took ', impact, ' damage!')
            return im
        else:
            print('\n',e.name,' Missed')
    else:
        print('\n',e.name, ' did not attack!')

def enemyFlee(e):
    print(e.name, ' fled!')

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

def magic(p, e, spell):
    hit = random.randrange(0,100)
    if (hit < spell['effectivness']):
        if (spell['attackType'] == 'single'):
            count = 1
            for i in e:
                print(count, ') ', i.name)
            target = input('Cast on:')
            count = 1
            for i in e:
                if (target == str(count)):
                    if (spell['spId'] == '1'):
                        i.aliment = 'Poison'
                count +=1
    
def special(p, e):
    print('\nSpecial Ability')
    count = 0
    for i in p.special:
        if (i['unlocked'] == True):
            count += 1
            print(count, ') ',i['name'], ' - ', i['cost'], ' stamina')
    print('Spells')
    for i in p.spells:
        if (i['unlocked'] == True):
            count += 1
            print(count, ') ',i['name'], ' - ', i['cost'], ' stamina')
    if (count == 0):
        print('None')
    sp = input('Use: ')
    count2 = 0
    for i in p.special:
        if (i['unlocked'] == True):
            count2 += 1
            if (sp == str(count2)):
               i['active'] = True
               if (i['spId'] == '1'):
                   p.stamina -= i['cost']
                   i['inEffect'] = 6
               elif (i['spId'] == '2'):
                   p.stamina -= i['cost']
                   i['inEffect'] = 5
               print('\n', p.name, ' uses ', i['name'],'.')
    for i in p.spells:
        if (i['unlocked'] == True):
            count2 += 1
            if (sp == str(count2)):
               i['active'] = True
               if (i['spId'] == '1'):
                   p.stamina -= i['cost']
                   magic(p, e, i)
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
                        print(u, count)
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
                        elif (i['weapon'] == 'crossbow'):
                            if(p.weapon2['type'] == 'crossbow'):
                                print('\nBolt loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                alder.cStatus = 'Using'
                                using = False
                            else:
                                print('Crossbow required!')
                                using = False
                        elif (i['weapon'] == 'sling'):
                            if(p.weapon2['type'] == 'sling'):
                                print('\nStone loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                alder.cStatus = 'Using'
                                using = False
                            else:
                                print('Sling required!')
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
    sheild = 0
    useSheild = True
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
            return False
        #Win
        elif(winner == True):
            for i in alder.special:
                i['active'] = False
                i['inEffect'] = 0
            fighting = False
            win(enemys)
            return True
        else:
            inEffect()
            for i in enemys:
                if(i.speed() > alder.speed() and count == 1 and i.health > 0):
                    enemyAttack(i, alder, sheild)
            while(alder.cStatus == 'None'):
                print('\n',alder.name)
                if (alder.ammo['loaded'] == True):
                    print('Ranged weapon set!')
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
                    if (alder.weapon2['type'] == 'sheild'):
                        if (useSheild == True):
                            sheild = alder.weapon2['defence']
                            useSheild = False
                    print(sheild)
                elif (i == '3' or i == 'appraise' or i == 'Appraise'):
                    for i in enemys:
                        print('\n',i.name, 'Health:', i.health,'/',i.maxHealth)
                        print(i.desc)
                elif (i == '4' or i == 'special' or i == 'Special'):
                    alder.cStatus = 'Specializing'
                    special(alder, enemys)
                elif (i == '5' or i == 'item' or i == 'Item'):
                    item(alder, enemys)
                elif (i == '6' or i == 'flee' or i == 'Flee'):
                    i = input('Are you sure you want to run?(y/n)')
                    if (i == 'y' or i == 'Y' or i == 'yes' or i == 'Yes'):
                        alder.cStatus = 'Escaping'
                        fighting = False
            for i in enemys:
                if (i.aliment == 'Poison'):
                    poison = i.maxHealth / 10
                    if (round(poison) < 0):
                        poison = 1
                    i.health -= round(poison)
                    print(i.name, 'took', poison, 'damage from poison!')
                if(i.health > 0):
                    if(i.strat == 'Attacker'):
                        print(alder.cStatus)
                        if (i.aliment != 'Caught'):
                            impact = enemyAttack(i, alder, sheild)
                            if (alder.cStatus == 'Blocking'):
                                sheild -= impact
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
                if (i.cStatus == 'Escaping'):
                    enemys.remove(i)
                    if (len(enemys) == 0):
                        fighting = False
                        return False
                else:
                    i.cStatus = 'None'
            count += 1
            alder.cStatus = 'None'

def unit():
    units = True
    while(units == True):
        print('\n1: Print stats.')
        print('2: Add experience')
        print('3: Recover')
        print('4: Reset')
        print('e - Exit')
        action = input('Action: ')
        if (action == '1'):
            alder.stats()
        elif (action == '2'):
            gainExperience()
            levelUP(alder)
        elif (action == '3'):
            alder.health = alder.maxHealth
            alder.stamina = alder.maxStamina
        elif (action == '4'):
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
            alder.head = armors[0]
            alder.body = armors[1]
            alder.legs = armors[3]
            alder.weapon1 = weapons[0]
            alder.weapon2 = weapons[0]
            alder.aliment = 'None'
            alder.cStatus = 'None'
            alder.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                              {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                              {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                              {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                              {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                              {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                              {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                              ]
            alder.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Doubles Evasion for five turns.'},
                            {'spId':'2','name':'Master archer', 'cost':10, 'active':False, 'inEffect':0, 'unlocked':False, 'effect':'Grants a critical for the next arrow fired within the next four turns.'}
                            ]
        elif (action == 'e'):
            units = False
def active():
    dostuff = True
    while(dostuff == True):
        print('\n1: Player stats.')
        print('2: Set equipment.')
        print('3: Fight')
        action = input('Action: ')
        if (action == '1'):
            unit()
        elif (action == '2'):
            equipment()
        elif (action == '3'):
            setFoe()
active()
