import ItemClasses
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


item = ItemClasses
def itemLister(e):
    return e['item'].priority

class Inventory():
    def __init__(self):
        self.shill = 0
        self.listSize = 0
        self.itemList = []
    def addItem(self, item, qnt):
        inInv = False
        for i in self.itemList:
            if (item.itemType == Weapon1Type.sword and i['item'].itemType == Weapon1Type.sword or
                item.itemType == Weapon1Type.dagger and i['item'].itemType == Weapon1Type.dagger or
                item.itemType == Weapon1Type.spear and i['item'].itemType == Weapon1Type.spear or
                item.itemType == Weapon1Type.axe and i['item'].itemType == Weapon1Type.axe or
                item.itemType == Weapon1Type.mace and i['item'].itemType == Weapon1Type.mace or
                item.itemType == Weapon1Type.staff and i['item'].itemType == Weapon1Type.staff):
                if (i['item'].wpId == item.wpId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.shield and i['item'].itemType == Weapon2Type.shield):
                if (i['item'].wpId == item.wpId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.bow and i['item'].itemType == Weapon2Type.bow):
                if (i['item'].wpId == item.wpId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.crossbow and i['item'].itemType == Weapon2Type.crossbow):
                if (i['item'].wpId == item.wpId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.sling and i['item'].itemType == Weapon2Type.sling):
                if (i['item'].wpId == item.wpId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.shield and i['item'].itemType == Weapon2Type.shield):
                if (i['item'].wpId == item.wpId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == Weapon2Type.wand and i['item'].itemType == Weapon2Type.wand):
                if (i['item'].wpId == item.wpId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == ArmourType.hat and i['item'].itemType == ArmourType.hat):
                if (i['item'].armId == item.armId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == ArmourType.shirt and i['item'].itemType == ArmourType.shirt):
                if (i['item'].armId == item.armId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == ArmourType.trousers and i['item'].itemType == ArmourType.trousers):
                if (i['item'].armId == item.armId):
                    item['count'] += qnt
                    inInv = True
            elif (item.itemType == ItemType.food and i['item'].itemType == ItemType.food):
                if (i['item'].itemId == item.itemId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == ItemType.healing and i['item'].itemType == ItemType.healing):
                if (i['item'].itemId == item.itemId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == ItemType.projectile and i['item'].itemType == ItemType.projectile):
                if (i['item'].itemId == item.itemId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == ItemType.toss and i['item'].itemType == ItemType.toss):
                if (i['itemId'] == item.itemId):
                    i['count'] += qnt
                    inInv = True
            elif (item.itemType == ItemType.ingredient and i['item'].itemType == ItemType.ingredient):
                if (i['item'].ingId == item.ingId):
                    i['count'] += qnt
                    inInv = True
        if (inInv == False):
            self.itemList.append({'item':item, 'count':qnt})
        self.itemList.sort(key=itemLister, reverse=False)
    def removeItem(self, item):
        for i in self.itemList:
            if(i['count'] <= 0):
                self.itemList.remove(i)
    def useItem(self,p):
        use = []
        count = 1
        print('\nBag Items')
        for i in itemList:
            if(i['item'].itemType == ItemType.healing or i['item'].itemType == ItemType.food):
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
                    if (i['item'].itemType == ItemType.healing):
                        p.health += i['heals']
                        print(p.name, ' recoved ', i['heals'], ' health')
                        if (p.health > p.maxHealth):
                            p.health = p.maxHealth
                    elif (i['item'].itemType == ItemType.food):
                        p.stamina += i['recovers']
                        print(p.name, ' recoved ', i['recovers'], ' stamina')
                        if (p.stamina > p.maxStamina):
                            p.stamina = p.maxStamina
                    i['count'] -= 1
                    if(i['count'] <= 0):
                        inv.remove(i)
                count +=1
            use.clear()
    def printInventory(self, Itype, listItems):
        #View the items in inventory
        #The same items should be counted to keep the list clear
        #Items should be in a order based on the item type
        #Input should allow the list to be narrowed down or print all items
        print('\nInventory')
        print('Shillings: ', self.shill)
        itemNum = 1
        listItems.clear()
        if (Itype == '' or Itype == 'food' or Itype == 'Food' or
            Itype == 'consumables' or Itype == 'Consumables'):
            print('Food')
            for i in self.itemList:
                if (i['item'].itemType == ItemType.food):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
        if (Itype == '' or Itype == 'healing' or Itype == 'Healing' or
            Itype == 'health' or Itype == 'Health'):
            print('Healing')
            for i in self.itemList:
                if (i['item'].itemType == ItemType.healing):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
        if (Itype == '' or Itype == 'weapons' or Itype == 'Weapons'):
            print('Weapons')
            for i in self.itemList:
                if (i['item'].itemType == Weapon1Type.sword or i['item'].itemType == Weapon1Type.dagger or i['item'].itemType == Weapon1Type.spear or
                   i['item'].itemType == Weapon1Type.axe or i['item'].itemType == Weapon1Type.mace or i['item'].itemType == Weapon1Type.staff or
                    i['item'].itemType == Weapon2Type.bow or i['item'].itemType == Weapon2Type.shield or i['item'].itemType == Weapon2Type.crossbow or
                    i['item'].itemType == Weapon2Type.sling or i['item'].itemType == Weapon2Type.wand):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
        if (Itype == '' or Itype == 'armour' or Itype == 'Armour'):
            print('Armour')
            for i in self.itemList:
                if (i['item'].itemType == ArmourType.hat or i['item'].itemType == ArmourType.shirt or i['item'].itemType == ArmourType.trousers):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
        if (Itype == '' or Itype == 'projectiles' or Itype == 'Projectiles'):
            print('Projectiles')
            for i in self.itemList:
                if (i['item'].itemType == ItemType.projectile or i['item'].itemType == ItemType.toss):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
        if (Itype == '' or Itype == 'ingredients' or Itype == 'Ingredients'):
            print('Ingredients')
            for i in self.itemList:
                if (i['item'].itemType == 'ingre'):
                    print(itemNum,') ',i['item'], 'x',i['count'])
                    itemNum += 1
                    listItems.append(i)
                
    def appraise(self):
        appraise = input('\nItem number: ')
        itemNum = 1
        for i in self.itemList:
            if (appraise == str(itemNum)):
                print('Name: ',i['item'], i['count'])
                if (i['item'].itemType != ItemType.food):
                    print('Name: ', i['item'],' - Type: ',i['item'].itemType,' - \nDescription: ',i['item'].description)
                else:
                    print('Name: ', i['item'],' - Type: ',i['item'].itemType,' - \nStamina Recovered: ',i['item'].recovers)
            itemNum += 1
    def shillings(self, incre):
        #Increment/Decrement Shillings
        global shill
        if (incre < 0):
            incre == 0
        self.shill += incre
        if (self.shill < 0):
            self.shill = 0
        print('Shillings: ', self.shill)
