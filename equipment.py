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
    def head(self,p,i,inv):
        print(i['item'].name, 'equiped')
        if(p.head.armId != '0'):
            inv.addItem(p.head,1)
        p.head = i['item']
        inv['count'] -= 1
        if(inv['count'] <= 0):
            inv.removeItem(i)
    def body(self,p,i,inv):
        print(i['item'].name, 'equiped')
        if(p.body.armId != '1'):
            inv.addItem(p.body,1)
        p.body = i['item']
        i['count'] -= 1
        print(i['count'])
        if(i['count'] <= 0):
            inv.removeItem(i)
    def legs(self,p,i,inv):
        print(i['item'].name, 'equiped')
        if(p.legs.armId != '1'):
            inv.addItem(p.legs,1)
        p.legs = i['item']
        i['count'] -= 1
        if(i['count'] <= 0):
            inv.removeItem(i)
    def primeWeapon(self,p,i,inv):
        print(i['item'].name, 'equiped')
        if(p.weapon1.wpId != '0'):
            inv.addItem(p.weapon1,1)
        p.weapon1 = i['item']
        i['count'] -= 1
        if(i['count'] <= 0):
            inv.removeItem(i)
    def secondWeapon(self,p,i,inv):
        print(i['item'].name, 'equiped')
        if(p.weapon2.wpId != '0'):
            inv.addItem(p.weapon2,1)
        p.weapon2 = i['item']
        i['count'] -= 1
        if(i['count'] <= 0):
            inv.removeItem(i)
