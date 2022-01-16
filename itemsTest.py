import random
import ItemClasses
import inventory
import equipment
import playableChars
from data import typeSpf

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

#Set Classes
alder = playableChars.Alder()
item = ItemClasses
inv = inventory.Inventory()
eqp = equipment.Equipment()


#Items lists
weapons = [item.Sword('0','None',0,0,''),
           item.Sword('1','Lief',100,5,'Legendary sword of the Scion.'),
           item.Dagger('2','Hunting Knife',5,1,'A knife used to hunt insects.')
           ]

armors = [item.Hat('1','None',0,0,''),
          item.Shirt('1','Old Tunic',1,1,'An old shirt with holes in it.'),
          item.Shirt('2','Travelling Cloak',10,10,'A too large black cloak. Good for keeping ou of sight but heavy.'),
          item.Trousers('1','Worn Trousers',1,1,'An old pair of trousers long past their prime'),
          ]
#Food(Id, Name, Weight, Stamina recovered)
food = [item.Food('1','Blackberry',1,5),
        item.Food('2','Dried Fruit',1,5),
        item.Food('3','Hazelnut',1,5)
        ]
items = [item.Healing('1','Bandage',2,10,'A cloth bandage to treat wounds')
         ]
#Money and inventory
shill = 0
PKSwitch = [[True, True, True, True, True], True, True]

#Increment/Decrement Shillings
def shillings(m):
    global shill
    if (m < 0):
        m == 0
    shill += m
    print('Shillings: ', shill)

def itemLister(e):
    return e['priority']
        
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
                inv.shillings(coins)
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
            inv.addItem(food[0], 1)
            PKSwitch[1] = False
        elif (p == '3'):
            print('\nDagger obtained')
            inv.addItem(weapons[2], 1)
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
                inv.addItem(items[0], 1)
            else:
                print('\nYou don'"'"'t have enough shillings')
        elif (p == '2'):
            cost = 1
            if (shill >= cost):
                print('\nYou bought a Dried Fruit')
                shillings(-cost)
                inv.addItem(food[1], 1)
            else:
                print('\nYou don'"'"'t have enough shillings')
        elif (p == '3'):
            cost = 1
            if (shill >= cost):
                print('\nYou bought a Hazelnut')
                shillings(-cost)
                inv.addItem(food[2], 1)
            else:
                print('\nYou don'"'"'t have enough shillings')
        elif (p == '4'):
            cost = 8
            if (shill >= cost):
                print('\nYou bought a Traveling Cloak')
                shillings(-cost)
                inv.addItem(armors[2], 1)
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
        inv.printInventory(j, listItems)
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
            inv.appraise()
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
                        eqp.head(alder, i, inv)
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
                        eqp.body(alder, i, inv)
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
                        eqp.legs(alder, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '4'):
            count = 0
            for i in inv.itemList:
                if(i['item'].itemType == Weapon1Type.dagger):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - alder.weapon1.attack)
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.primeWeapon(alder, i, inv)
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
                        eqp.secondWeapon(alder, i, inv)
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
