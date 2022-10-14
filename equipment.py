import ItemClasses
import inventory
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

#Set classes
inv = inventory.Inventory()

class Equipment():
    def getHat(self, p, inv,equipable):
        count = 0
        for i in inv.itemList:
            if(i['item'].itemType == ArmourType.hat):
                count +=1
                equipable.append(i)
                print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.head.defence)
        return count
    def getShirt(self, p, inv,equipable):
        count = 0
        for i in inv.itemList:
            if(i['item'].itemType == ArmourType.shirt):
                count +=1
                equipable.append(i)
                print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.body.defence)
        return count
    def getTrousers(self, p, inv,equipable):
        count = 0
        for i in inv.itemList:
            if(i['item'].itemType == ArmourType.trousers):
                count +=1
                equipable.append(i)
                print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.legs.defence)
        return count
    def getPrimeWeapon(self, p, inv,equipable):
        count = 0
        for i in inv.itemList:
            if(i['item'].itemType == Weapon1Type.sword or i['item'].itemType == Weapon1Type.dagger or i['item'].itemType == Weapon1Type.spear or
               i['item'].itemType == Weapon1Type.axe or i['item'].itemType == Weapon1Type.mace or i['item'].itemType == Weapon1Type.staff):
                count +=1
                equipable.append(i)
                
                if(i['item'].itemType == Weapon1Type.staff and len(i['item'].spells) != 0):
                    print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon1.attack, '- Spells: ', list(zip(*i['item'].spells))[1])
                else:
                    print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon1.attack)
        return count
    def getSecondWeapon(self, p, inv,equipable):
        count = 0
        for i in inv.itemList:
            if(i['item'].itemType == Weapon2Type.bow or i['item'].itemType == Weapon2Type.crossbow or i['item'].itemType == Weapon2Type.sling or
                i['item'].itemType == Weapon2Type.shield or i['item'].itemType == Weapon2Type.wand):
                count +=1
                equipable.append(i)
                if(i['item'].itemType == Weapon2Type.bow):
                    if (p.weapon2.itemType == Weapon2Type.bow or p.weapon2.itemType == Weapon2Type.crossbow or p.weapon2.itemType == Weapon2Type.sling):
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon2.attack)
                    else:
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack)
                elif(i['item'].itemType == Weapon2Type.crossbow):
                    if (p.weapon2.itemType == Weapon2Type.bow or p.weapon2.itemType == Weapon2Type.crossbow or p.weapon2.itemType == Weapon2Type.sling):
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon2.attack)
                    else:
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack)
                elif(i['item'].itemType == Weapon2Type.sling):
                    if (p.weapon2.itemType == Weapon2Type.bow or p.weapon2.itemType == Weapon2Type.crossbow or p.weapon2.itemType == Weapon2Type.sling):
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon2.attack)
                    else:
                        print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack)
                elif(i['item'].itemType == Weapon2Type.shield):
                    if (p.weapon2.itemType == Weapon2Type.shield):
                        print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - p.weapon2['defence'])
                    else:
                        print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence)
                elif(i['item'].itemType == Weapon2Type.wand):
                    print(count, ': ', i['item'].name, '- Spells: ', list(zip(*i['item'].spells))[1])
                    for j in p.spells:
                        if (j['spId'] == i.wpId):
                            j['unlocked'] = True
        return count
    def setEquipment(self,count,equipable):
        if(count != 0):
            count = 1
            eq = input('Equip item: ')
            for i in equipable:
                if (eq == str(count)):
                    return i
                count +=1
        else:
            print('You have nothing to equip.')
            return None
        equipable.clear()
    def head(self,p,i,inv):
        if (i != None):
            print(i['item'].name, 'equiped')
            if(p.head.armId != '0'):
                inv.addItem(p.head,1)
            p.head = i['item']
            inv['count'] -= 1
            if(inv['count'] <= 0):
                inv.removeItem(i)
    def body(self,p,i,inv):
        if (i != None):
            print(i['item'].name, 'equiped')
            if(p.body.armId != 1):
                inv.addItem(p.body,1)
            p.body = i['item']
            i['count'] -= 1
            print(i['count'])
            if(i['count'] <= 0):
                inv.removeItem(i)
    def legs(self,p,i,inv):
        if (i != None):
            print(i['item'].name, 'equiped')
            if(p.legs.armId != 1):
                inv.addItem(p.legs,1)
            p.legs = i['item']
            i['count'] -= 1
            if(i['count'] <= 0):
                inv.removeItem(i)
    def primeWeapon(self,p,i,inv):
        if (i != None ):
            print(i['item'].name, 'equiped')
            if(p.weapon1.wpId != 1008):
                inv.addItem(p.weapon1,1)
            p.weapon1 = i['item']
            i['count'] -= 1
            if(i['count'] <= 0):
                inv.removeItem(i)
    def secondWeapon(self,p,i,inv):
        if (i != None):
            print(i['item'].name, 'equiped')
            if(p.weapon2.wpId != 1008):
                inv.addItem(p.weapon2,1)
            p.weapon2 = i['item']
            i['count'] -= 1
            if(i['count'] <= 0):
                inv.removeItem(i)
