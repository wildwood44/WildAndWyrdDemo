import random

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
#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'weapon', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0, 'priority': 3},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'weapon', 'description' : 'Legendary sword of the Scion.',
            'attack' : 100, 'weight' : 5, 'count' : 0, 'priority': 3},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'weapon', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0, 'priority': 3}
           ]

armors = [{'armId' : '1', 'name' : 'None', 'type' : 'hat', 'description' : '',
          'defence' : 0, 'weight' : 0, 'count' : 0, 'priority': 4},
          {'armId' : '1', 'name' : 'Old Tunic', 'type' : 'shirt', 'description' : 'An old shirt with holes in it.',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 5},
          {'armId' : '2', 'name' : 'Travelling Cloak', 'type' : 'shirt', 'description' : 'A too large black cloak. Good for keeping ou of sight but heavy.',
          'defence' : 10, 'weight' : 10, 'count' : 0, 'priority': 5},
          {'armId' : '1', 'name' : 'Worn Trousers', 'type' : 'trousers', 'description' : 'An old pair of trousers long past their prime',
          'defence' : 1, 'weight' : 1, 'count' : 0, 'priority': 6}
          ]
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : 'food',
          'recovers' : 5, 'count' : 0, 'priority': 1}
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0, 'priority': 2}
         ]
#Money and inventory
shill = 0
inv = []
invSorted = {'food', 'healing', 'weapon', 'hat', 'shirt', 'trousers'}
PKSwitch = [[True, True, True, True, True], True, True]
#Set Class
alder = Alder()
#Increment/Decrement Shillings
def shillings(m):
    global shill
    if (m < 0):
        m == 0
    shill += m
    print('Shillings: ', shill)

def itemLister(e):
    return e['priority']

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
    inv.sort(key=itemLister, reverse=False)
        
#Pickup item or money off the ground
#Ground item should disappear after picked up
def pickup(s):
    collect = True
    print('\nShillings: ', shill)
    while (collect == True):
        print('\nThere are items on the ground.')
        if(PKSwitch[0][0] == True or PKSwitch[0][1] == True or PKSwitch[0][2] == True or
           PKSwitch[0][3] == True or PKSwitch[0][4] == True):
            print('1: Shillings')
        if(PKSwitch[1] == True):
            print('2: Blackberry')
        if(PKSwitch[2] == True):
            print('3: Dagger')
        print('e - Exit')
        p = input('Pick up: ')
        if (p == '1'):
            if(PKSwitch[0][0] == True or PKSwitch[0][1] == True or PKSwitch[0][2] == True or
               PKSwitch[0][3] == True or PKSwitch[0][4] == True):
                coins = random.randrange(+3,+6)
                print('\n', coins,' shillings obtained')
                shillings(coins)
                if (PKSwitch[0][4] == False):
                    if (PKSwitch[0][3] == False):
                        if (PKSwitch[0][2] == False):
                            if (PKSwitch[0][1] == False):
                                PKSwitch[0][0] = False
                            PKSwitch[0][1] = False
                        PKSwitch[0][2] = False
                    PKSwitch[0][3] = False
                PKSwitch[0][4] = False
        elif (p == '2'):
            print('\nBlackberries obtained')
            itemCount(food[0], 1)
            PKSwitch[1] = False
        elif (p == '3'):
            print('\nDagger obtained')
            itemCount(weapons[2], 1)
            PKSwitch[2] = False
        elif (p == 'e'):
            print()
            collect = False

#The user should buy items from shop
#Shilling should be lost after purchase
def shop():
    shopping = True
    while(shopping == True):
        print('\nFeel free to brouse my wares.')
        print('1: Bandage ', 'Remaining: ', '5 Cost: 5')
        print('2: Dried Fruit' , 'Remaining: ', '5 Cost: 1')
        print('3: Hazel Nuts ', 'Remaining: ', '5 Cost: 1')
        print('4: Traveling Cloak', 'Remaining: ', '2 Cost: 8')
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
        elif (p == '4'):
            cost = 8
            if (shill >= cost):
                print('\nYou bought a Traveling Cloak')
                shillings(-cost)
                itemCount(armors[2], 1)
            else:
                print('\nYou don'"'"'t have enough shillings')
        elif (p == 'e'):
            print()
            shopping = False
#Open the inventory
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
        if (j == '' or j == 'weapons' or j == 'Weapons'):
            print('Weapons')
            for i in inv:
                if (i['type'] == 'weapon'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        if (j == '' or j == 'armour' or j == 'Armour'):
            print('Armour')
            for i in inv:
                if (i['type'] == 'hat' or i['type'] == 'shirt' or i['type'] == 'trousers'):
                    print(count, ') ', i['name'], ' x', i['count'])
                    count += 1
                    listItems.append(i)
        print('\n1: Appraise')
        print('2: Equip')
        print('e - Exit')
        i = input('Item: ')
        if (i == '' or i == 'food' or i == 'Food' or i == 'consumables' or i == 'Consumables' or i == 'healing' or i == 'Healing' or
            i == 'health' or i == 'Health' or i == 'weapons' or i == 'Weapons'  or i == 'armour' or i == 'Armour' or
            i == '1' or i == '2' or i == 'e'):
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
        if (j == '1' or j == '2'):
            j = ''
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

def active():
    dostuff = True
    while(dostuff == True):
        print('1: Alder Stats.')
        print('2: Pick up item.')
        print('3: Shop')
        print('4: Inventory')
        i = input('Action: ')
        if (i == '1'):
            alder.stats()
        elif (i == '2'):
            pickup(shill)
        elif (i == '3'):
            shop()
        elif (i == '4'):
            inventory()
active()
