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

class Item():
    def __init__(self,name,itemType,weight,priority):
        self.name = name
        self.itemType = itemType
        self.priority = priority
        self.weight = weight
        
class Food(Item):
    def __init__(self,itemId,name,weight,recovers):
        Item.__init__(self,name,ItemType.food,weight,1)
        self.itemId = itemId
        self.recovers = recovers
    def __str__(self): 
        return self.name
    def __ref__(self):
        return "Name:% s Type:% s Recovers:% s " % (self.name, self.itemType.name, self.recovers)

class Healing(Item):
    def __init__(self,itemId,name,weight,recovers,description):
        Item.__init__(self,name,ItemType.healing,weight,2)
        self.itemId = itemId
        self.recovers = recovers
        self.description = description
    def __str__(self): 
        return self.name

class Weapons(Item):
    def __init__(self,wpId,name,attack,itemType,weight,priority,description):
        Item.__init__(self,name,itemType,weight,priority)
        self.attack = attack
        self.description = description
    def __str__(self): 
        return self.name

class Sword(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.sword,weight,3,description)
        self.wpId = wpId

class Dagger(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.dagger,weight,3,description)
        self.wpId = wpId

class Spear(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.spear,weight,3,description)
        self.wpId = wpId

class Axe(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.axe,weight,3,description)
        self.wpId = wpId

class Mace(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.mace,weight,3,description)
        self.wpId = wpId

class Staff(Weapons):
    def __init__(self,wpId,name,attack,weight,spId,spells,description):
        Weapons.__init__(self,wpId,name,attack,Weapon1Type.staff,weight,3,description)
        self.wpId = wpId
        self.spId = spId
        self.spells = spells

class Bow(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon2Type.bow,weight,4,description)
        priority = 4
        itemType = Weapon2Type.bow
        self.wpId = wpId

class Crossbow(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon2Type.crossbow,weight,4,description)
        self.wpId = wpId

class Sling(Weapons):
    def __init__(self,wpId,name,attack,weight,description):
        Weapons.__init__(self,wpId,name,attack,Weapon2Type.sling,weight,4,description)
        self.wpId = wpId

class Shield(Weapons):
    def __init__(self,wpId,name,defence,weight,description):
        Weapons.__init__(self,wpId,name,0,Weapon2Type.shield,weight,4,description)
        self.wpId = wpId
        self.defence = defence

class Wand(Weapons):
    def __init__(self,wpId,name,weight,spId,spells,description):
        Weapons.__init__(self,wpId,name,0,Weapon2Type.wand,weight,4,description)
        self.wpId = wpId
        self.spId = spId
        self.spells = spells
        
class Armours(Item):
    def __init__(self,armId,name,defence,itemType,weight,priority,description):
        Item.__init__(self,name,itemType,weight,priority)
        self.defence = defence
        self.description = description
    def __str__(self): 
        return self.name

class Hat(Armours):
    def __init__(self,armId,name,defence,weight,description):
        Armours.__init__(self,armId,name,defence,ArmourType.hat,weight,5,description)
        self.armId = armId

class Shirt(Armours):
    def __init__(self,armId,name,defence,weight,description):
        Armours.__init__(self,armId,name,defence,ArmourType.shirt,weight,6,description)
        self.armId = armId

class Trousers(Armours):
    def __init__(self,armId,name,defence,weight,description):
        Armours.__init__(self,armId,name,defence,ArmourType.trousers,weight,7,description)
        self.armId = armId
        
class Projectile(Item):
    def __init__(self,itemId,name,damage,itemType,weight,priority,description):
        Item.__init__(self,name,itemType,weight,priority)
        self.defence = defence
        self.description = description
    def __str__(self): 
        return self.name

class Ammo(Projectile):
    def __init__(self,itemId,name,damage,itemType,weight,weapon,description):
        Projectile.__init__(self,itemId,name,damage,ItemType.projectile,weight,8,description)
        self.itemId = itemId
        self.weapon = weapon

class Arrow(Ammo):
    def __init__(self,itemId,name,damage,itemType,weight,description):
        Ammo.__init__(self,itemId,name,damage,itemType,weight,Weapon2Type.bow,description)

class Bolt(Ammo):
    def __init__(self,itemId,name,damage,itemType,weight,description):
        Ammo.__init__(self,itemId,name,damage,itemType,weight,Weapon2Type.crossbow,description)

class Stone(Ammo):
    def __init__(self,itemId,name,damage,itemType,weight,description):
        Ammo.__init__(self,itemId,name,damage,itemType,weight,Weapon2Type.sling,description)

class Toss(Projectile):
    def __init__(self,itemId,name,damage,itemType,weight,description):
        Projectile.__init__(self,itemId,name,damage,ItemType.toss,weight,9,description)
        self.itemId = itemId

class Ingredient(Item):
    def __init__(self,itemId,name,itemType,weight,description):
        Item.__init__(self,name,ItemType.ingredient,weight,10)
        self.itemId = itemId
    def __str__(self): 
        return self.name

def printItem():
    blackberry = Food('1','Blackberry',1,5)
    print(blackberry)

#printItem()
