import ItemClasses
import inventory
import spells
import manuvers
from data import typeSpf
SpecialType1 = typeSpf.SpecialType1
SpecialType2 = typeSpf.SpecialType2
AttackType = typeSpf.AttackType
SpellType = typeSpf.SpellType
CombatStatus = typeSpf.CombatStatus
ArmourType = typeSpf.ArmourType
Weapon1Type = typeSpf.Weapon1Type
Weapon2Type = typeSpf.Weapon2Type
ItemType = typeSpf.ItemType
#Set classses
item = ItemClasses
spl = spells
mnv = manuvers
#Universal Specials
manuvers = [{'spId':'1','name':'Advence', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
           {'spId':'2','name':'Retreat', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
           ]
spells = [spl.Nature_Offence('1','Poison nettles', AttackType.single, 1, 10, 100, 'Poisons an opponent'),
          spl.Nature_Offence('2','Grow mushrooms', AttackType.single, 0, 10, 100, 'Grow mushrooms on your enemy to hinder them.'),
          spl.Nature_Enhance('3','Grow mushrooms', 9, 0, 100, "Grow edable mushrooms for an ally to restore stamina."),
          spl.Nature_Support('4','Grow mushrooms', AttackType.single, 9, 0, 100, 'Grow edable mushrooms for the caster to restore stamina.')
          ]
combinations = [{'spell':spl.Nature_Offence('comb1','Poisonous mushrooms', AttackType.single, 9, 10, 100, 'Grow poisinous mushrooms on the enemy.'), 'components':['1', '2']}
          ]
#Character Base Stats
class Playable():
    def __init__(self, pId, active, name, species, maxHealth, maxStamina, cLvl,
                 baseAttack, baseDefence, baseAccuracy, baseSpeed, baseEvasion,
                 head, body, legs, weapon1, weapon2, abilities):
        self.pId = pId
        self.active = active
        self.name = name
        self.species = species
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.maxStamina = maxStamina
        self.stamina = self.maxStamina
        self.type = 'playable'
        self.cLvl = cLvl
        self.cExp = 0
        self.cNext = 30
        self.skillPoints = 0
        self.baseAttack = baseAttack
        self.baseDefence = baseDefence
        self.baseAccuracy = baseAccuracy
        self.baseSpeed = baseSpeed
        self.baseEvasion = baseEvasion
        self.head = head
        self.body = body
        self.legs = legs
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = CombatStatus.Normal
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                          {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                          {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                          {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                          {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                          {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                          {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                          ]
        self.abilities = abilities
        self.manver = []
        self.spells = []
    property
    def attack(self):
        attack = self.baseAttack
        if (self.weapon1.wpId != '0'):
            attack += self.weapon1.attack
        else:
            attack += 0
        return attack
    property
    def attackRanged(self):
        attackRanged = self.baseAttack
        if (self.weapon2.wpId != '0' and self.weapon2 == Weapon2Type.bow):
            attackRanged += self.weapon2.attack
        else:
            attackRanged += 0
        return attackRanged
    property
    def defence(self):
        defence = self.baseDefence
        if (self.head.itemType == ArmourType.hat):
            defence += self.head.defence
        if (self.body.itemType == ArmourType.shirt):
            defence += self.body.defence
        if (self.legs.itemType == ArmourType.trousers):
            defence += self.legs.defence
        if (self.weapon2.itemType == Weapon2Type.shield):
            defence += self.weapon2.defence
        else:
            defence += 0
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
        if (self.special_auto().specialType == SpecialType1.manuver):
            print(self.special_auto().spId == 'a1', self.special_auto().active == True)
            if (self.special_auto().spId == 'a1' and self.special_auto().active == True):
                evasion *= 2
        return evasion
    property
    def special_auto(self):
        automatic = spl.Nature_Automatic('0','None',  AttackType.single,0,0,0,'')
        if (self.weapon2.itemType == Weapon2Type.wand):
            for i in spells:
                if(self.weapon2.spId == i.spId and i.spltype == SpecialType2.automatic):
                    if (self.weapon1.itemType == Weapon1Type.staff):
                        confirm = False
                        for j in spells:
                            for k in self.weapon1.spells:
                                if(k.spId == j.spId and j.spltype == SpecialType2.automatic):
                                    automatic = i.combine(j)
                                    confirm = True
                        if(confirm == False):
                            automatic = i
                    else:
                        automatic = i
        if (self.weapon1.itemType == Weapon1Type.staff and automatic.spId == '0'):
            for i in spells:
                for j in self.weapon1.spId:
                    if(j == i.spId and i.spltype == SpecialType2.automatic):
                        automatic = i
        if (automatic.spId == '0'):
            for i in self.abilities:
                if(i.unlocked == True and i.spltype == SpecialType2.automatic):
                    automatic = i
        return automatic
    property
    def special_off(self):
        offence = spl.Nature_Offence('0','None',AttackType.single, 0,0,0,'')
        if (self.weapon2.itemType == Weapon2Type.wand):
            for i in spells:
                if(self.weapon2.spId == i.spId and i.spltype == SpecialType2.offence):
                    if (self.weapon1.itemType == Weapon1Type.staff):
                        confirm = False
                        for j in spells:
                            for k in self.weapon1.spId:
                                if(k == j.spId and j.spltype == SpecialType2.offence):
                                    offence = i.combine(j)
                                    confirm = True
                        if(confirm == False):
                            offence = i
                    else:
                        offence = i
        if (self.weapon1.itemType == Weapon1Type.staff and offence.spId == '0'):
            for i in spells:
                for j in self.weapon1.spId:
                    if(j == i.spId and i.spltype == SpecialType2.offence):
                        offence = i
        if (offence.spId == '0'):
            for i in self.abilities:
                if(i.unlocked == True and i.spltype == SpecialType2.offence):
                    offence = i
        return offence
    property
    def special_sup(self):
        support = spl.Nature_Support('0','None', AttackType.single, 0,0,0,'')
        if (self.weapon2.itemType == Weapon2Type.wand):
            for i in spells:
                if(self.weapon2.spId == i.spId and i.spltype == SpecialType2.support):
                    if (self.weapon1.itemType == Weapon1Type.staff):
                        confirm = False
                        for j in spells:
                            for k in self.weapon1.spId:
                                if(k == j.spId and j.spltype == SpecialType2.support):
                                    support = i.combine(j)
                                    confirm = True
                        if(confirm == False):
                            support = i
                    else:
                        support = i
        if (self.weapon1.itemType == Weapon1Type.staff and support.spId == '0'):
            for i in spells:
                for j in self.weapon1.spId:
                    if(j == i.spId and i.spltype == SpecialType2.support):
                        support = i
        if (support.spId == '0'):
            for i in self.abilities:
                if(i.unlocked == True and i.spltype == SpecialType2.support):
                    support = i
        return support
    property
    def special_enc(self):
        enhance = spl.Nature_Enhance('0','None',0,0,0,'')
        if (self.weapon2.itemType == Weapon2Type.wand):
            for i in spells:
                if(self.weapon2.spId == i.spId and i.spltype == SpecialType2.enhance):
                    if (self.weapon1.itemType == Weapon1Type.staff):
                        confirm = False
                        for j in spells:
                            for k in self.weapon1.spId:
                                if(k == j.spId and j.spltype == SpecialType2.enhance):
                                    enhance = i.combine(j)
                                    confirm = True
                        if(confirm == False):
                            enhance = i
                    else:
                        enhance = i
        if (self.weapon1.itemType == Weapon1Type.staff and enhance.spId == '0'):
            for i in spells:
                for j in self.weapon1.spId:
                    if(j == i.spId and i.spltype == SpecialType2.enhance):
                        enhance = i
        if (enhance.spId == '0'):
            for i in self.abilities:
                print(i);
                if(i.unlocked == True and i.spltype == SpecialType2.enhance):
                    enhance = i
        return enhance
    def stats(self):
        print('\nStats: \nName:', self.name, '- Lvl:', self.cLvl, 'Exp:', self.cExp,
              '\nHealth:', self.health, '/', self.maxHealth, '| Stamina:', self.stamina, '/', self.maxStamina,
              '\nAttack:', self.attack(), '(', self.baseAttack,'+',self.weapon1.attack, ')',
              '| Defence:', self.defence(), '(', self.baseDefence,'+',self.head.defence + self.body.defence + self.legs.defence, ')',
              '| \nAccuracy:', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed:', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion:', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nEquipment: \nHead:', self.head.name, '\nBody:', self.body.name, '\nLegs:', self.legs.name,
              '\nMain Weapon:', self.weapon1.name, '\nSecondary Weapon:', self.weapon2.name,
              '\nSpecials: \nAutomatic:', self.special_auto().name, '\nOffensive:', self.special_off().name,
              '\nSupport:', self.special_sup().name, '\nEnhance:', self.special_enc().name,'\n'
              )
#Alder
class Alder(Playable):
    def __init__(self):
        Playable.__init__(self, '1', True, 'Alder', 'Human', 60, 60, 1, 10, 10, 5, 10, 5,
                item.Hat('0','None', 0, 0, ''),
                item.Shirt('0','Old Tunic', 1,1, 'An old shirt with holes in it.'),
                item.Trousers('0', 'Worn Trousers',1,1,'An old pair of trousers long past their prime'),
                item.Sword('0','None', 0,0, ''), item.Sword('0','None', 0,0, ''),
                [mnv.Manuver_Automatic('a1','Steps of heroes', AttackType.single, 0,10, 100, 'Doubles Evasion for five turns.')])
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = CombatStatus.Normal
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.manver = []
        self.spells = []
#Florace
class Florace(Playable):
    def __init__(self):
        Playable.__init__(self, '2', True, 'Florace', 'Human', 150, 150, 1, 6, 14, 10, 11, 4,
                item.Hat('0','None', 0, 0, ''),
                item.Shirt('0','Old Tunic', 1,1, 'An old shirt with holes in it.'),
                item.Trousers('0', 'Worn Trousers',1,1,'An old pair of trousers long past their prime'),
                item.Sword('0','None', 0,0, ''), item.Sword('0','None', 0,0, ''),
                [spl.Blessing('f1','Heal', 100,10, 100, 'Heals an ally')])
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.manver = []
        self.spells = []
