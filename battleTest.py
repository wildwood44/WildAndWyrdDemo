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
        self.baseAttack = 10
        self.baseDefence = 10
        self.baseAccuracy = 5
        self.baseSpeed = 10
        self.baseEvasion = 5
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
        self.weapon1 = weapons[0]
        self.weapon2 = 'None'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':True, 'effect':'Increases Evasion for five turns.'},
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
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2, '\n'
              )
#Enemy Units
class Cricket:
    def __init__(self):
        self.enId = '1'
        self.name = 'Cricket'
        self.maxHealth = 20
        self.health = self.maxHealth
        self.Exp = 10
        self.drop = [{'item' : food[3], 'quantity':2}]
        self.baseAttack = 0
        self.baseDefence = 8
        self.baseAccuracy = 90
        self.baseSpeed = 10
        self.baseEvasion = 25
        self.strat = 'Prey'
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
        self.Exp = 10
        self.drop = [{'item':food[3], 'quantity':1}]
        self.baseAttack = 5
        self.baseDefence = 5
        self.baseAccuracy = 90
        self.baseSpeed = 40
        self.baseEvasion = 45
        self.strat = 'Attacker'
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
        self.maxHealth = 100
        self.health = self.maxHealth
        self.Exp = 5
        self.drop = []
        self.baseAttack = 0
        self.baseDefence = 150
        self.baseAccuracy = 0
        self.baseSpeed = 0
        self.baseEvasion = 0
        self.strat = 'Attacker'
        self.cStatus = 'None'
        self.desc = 'Made from sticks and a sack. Made to fight.'
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
        self.enId = '4'
        self.name = 'Gowls Captain Clipgrea'
        self.maxHealth = 12000
        self.health = self.maxHealth
        self.Exp = 0
        self.drop = []
        self.baseAttack = 900
        self.baseDefence = 750
        self.baseAccuracy = 200
        self.baseSpeed = 1700
        self.baseEvasion = 1800
        self.strat = 'Attacker'
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

#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'weapon', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'weapon', 'description' : 'Legendary sword of the Scion.',
            'attack' : 500, 'weight' : 5, 'count' : 0},
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
          'recovers' : 3, 'count' : 0},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : 'food',
          'recovers' : 5, 'count' : 0},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : 'food',
          'recovers' : 3, 'count' : 0},
        {'itemId' : '4', 'name' : 'Raw Bug Meat', 'type' : 'food',
          'recovers' : 10, 'count' : 0}
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
            print('1: tutorial items set')
            j = input('Item set:')
            if (j == '1'):
                print('\nDagger obtained')
                itemCount(weapons[2], 1)
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
            print('4: Gowls Captain')
            j = input('Enemy: ')
            if (j == '1'):
                enemy[0] = Cricket()
            elif (j == '2'):
                enemy[0] = Wasp()
            elif (j == '3'):
                enemy[0] = Dummy()
            elif (j == '4'):
                enemy[0] = Gowl_Rabbit()
        elif (i == '2'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Gowls Captain')
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
                enemy[1] = Gowl_Rabbit()
        elif (i == '3'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Gowls Captain')
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
                enemy[2] = Gowl_Rabbit()
        elif (i == '4'):
            if(enemy[0].enId != null.enId):
                battle(enemy)
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
    for i in e:
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

def enemyFlee(e):
    print(e.name, ' fled!')

#Attack Enemy
def attack(p, e):
    target = p.accuracy() + 100 - e.evasion()
    hit = random.randrange(0,100)
    critical = random.randrange(0,100)
    alder.stamina -= 5
    if (hit < target):
        impact = random.randrange(p.attack() - 5, p.attack() + 5)
        if (critical >= 90):
            impact += 10
        impact = round(impact * (100/(100 + p.defence())))
        if (impact <= 0):
            impact = 1
        e.health -= impact
        print('\n',p.name,' attacked!')
        if(critical >= 90):
            print('Critical Hit!')
        print(e.name, ' took ', impact, ' damage!')
        if(e.health <= 0):
            print(e.name, ' defeated.')
    else:
        print('\n',p.name,' Missed')

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
def item(p):
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
        if (enemys[0].health <= 0):
            count = 0
            for i in enemys:
                if (i.health <= 0):
                    count += 1
            if (count == len(enemys)):
                winner = True
        #Death Condition
        if(alder.health <= 0):
            fighting = False
            death()
        #Win Condition
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
                    alder.cStatus = 'Using'
                    item(alder)
                elif (i == '6' or i == 'flee' or i == 'Flee'):
                    i = input('Are you sure you want to run?(y/n)')
                    if (i == 'y' or i == 'Y' or i == 'yes' or i == 'Yes'):
                        alder.cStatus = 'Escaping'
                        fighting = False
            for i in enemys:
                if(i.health > 0):
                    if(i.strat == 'Attacker'):
                        enemyAttack(i, alder, bck)
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
                else:
                    i.cStatus = 'None'
            count += 1
            alder.cStatus = 'None'
        
def active():
    dostuff = True
    while(dostuff == True):
        print('\n1: Player stats.')
        print('2: Set equipment.')
        print('3: Fight')
        action = input('Action: ')
        if (action == '1'):
            alder.stats()
            alder.health = alder.maxHealth
            alder.stamina = alder.maxStamina
        elif (action == '2'):
            equipment()
        elif (action == '3'):
            setFoe()
active()
