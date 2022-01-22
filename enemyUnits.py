import random
import ItemClasses
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
#Set classes
item = ItemClasses
#Reward Items
food = [item.Food('1','Blackberry', 1,3),
        item.Food('2','Dried Fruit', 1,5),
        item.Food('3','Hazelnut', 1,3),
        item.Food('4','Mushroom',1,5),
        item.Food('5','Raw Bug Meat',3,10)
        ]
#Inventory order
def itemLister(e):
    return e['priority']
###Enemy Priorities
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
#Enemy Units
class Enemy:
    def __init__(self,enId,name,maxHealth,enType,Exp,drop,
                 baseAttack, baseDefence, baseAccuracy, baseSpeed, baseEvasion,
                 weapon1,weapon2,strat,desc):
        self.enId = enId
        self.inId = '0'
        self.name = name
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.type = enType
        self.Exp = Exp
        self.drop = drop
        self.baseAttack = baseAttack
        self.baseDefence = baseDefence
        self.baseAccuracy = baseAccuracy
        self.baseSpeed = baseSpeed
        self.baseEvasion = baseEvasion
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.strat = strat
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = desc
    property
    def attack(self):
        attack = self.baseAttack
        if (self.aliment['fungus'] == True):
            attack = attack/2
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
    
class Cricket(Enemy):
    def __init__(self):
        Enemy.__init__(self,'1','Cricket',20,'bug',10,[{'item' : food[4], 'quantity':2}],
                0, 8, 90, 10, 23,{'type':''},{'type':''},'Prey',
                'Big grasshoppers with long antenna. Can jump a fair distance.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        if (rd == 1):
            say = '\nUse the command "3" or "appraise" to examine enemy health and information.'
        elif (rd == 2):
            say = '\nTo reduce damage from a incoming attack use command "2" or "block"'
        elif (rd == 3):
            say = '\nTo deal damage to the opponent use command "1" or "attack".'
        else:
            say = ''
        return say
    property
    def action(self, e, p, r):
        if(self.health < self.maxHealth):
            self.cStatus = CombatStatus.Escaping
            print(self.name, ' fled!')
            r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
            return [0, self.cStatus]
        else:
            self.cStatus = CombatStatus.Normal
            print(self.name, ' stood wary.')
            r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
            return [0, self.cStatus]

class Hornet(Enemy):
    def __init__(self):
        Enemy.__init__(self,'2','Hornet',19,'bug',10,[{'item' : food[4], 'quantity':1}],
                5, 5, 90, 40, 45,{'type':''},{'type':''},'Attacker',
                'More hostile than usual this year. In the air they are annoying to hit but they are easy to kill.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Attacking
        target = ePriority_retaliation(p, e, r)
        impact = enemyAttack(e, target, target.shield)
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status':self.cStatus, 'Hit': target, 'Damage':impact})
        return [impact, self.cStatus]

class Dummy(Enemy):
    def __init__(self):
        Enemy.__init__(self,'3','Dummy',24,'puppet',5,[],
                0, 150, 0, 0, 0,{'type':''},{'type':''},'Attacker',
                'Durable but falling apart.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        say = '\nTo use a ranged weapon like the bow select a supported projectile from items, then on the next turn attack to fire.'
        return say
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Normal
        print(self.name, ' did not attack!')
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
        return [0, self.cStatus]
class Wall(Enemy):
    def __init__(self):
        Enemy.__init__(self,'4','Wall',200,'puzzle',5,[],
                0, 400, 0, 0, 0,{'type':''},{'type':''},'Attacker',
                'The wall between the living room and the shed.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Normal
        print(self.name, ' did not attack!')
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
        return [0, self.cStatus]
    
class Gowl_Rabbit(Enemy):
    def __init__(self):
        Enemy.__init__(self,'5','Gowls Captain Clipgrea',12000,'soldier',0,[],
                900, 750, 200, 1700, 1800,{'type':Weapon1Type.spear},{'type':''},'Attacker',
                'A Gowls Captain. There'"'"'s a reason for that. Well equiped and fast as rabbits are.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Attacking
        target = ePriority_Alder(p)
        impact = enemyAttack(e, target, target.shield)
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status':self.cStatus, 'Hit': target, 'Damage':impact})
        return [impact, self.cStatus]

class YoungCrow(Enemy):
    def __init__(self):
        Enemy.__init__(self,'6','Young Crow',100,'bird',10,[],
                5, 5, 90, 40, 45,{'type':''},{'type':ItemType.projectile, 'name' : 'nuts', 'qnt' : 2},'Attacker',
                'Likes to throw things at people.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':True, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Attacking
        target = ePriority_weakness(p)
        impact = enemyAttack(e, target, target.shield)
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status':self.cStatus, 'Hit': target, 'Damage':impact})
        return [impact, self.cStatus]

class ShieldMaster(Enemy):
    def __init__(self):
        Enemy.__init__(self,'7','Shield Master',100,'soldier',100,[],
                5, 5, 90, 5, 45,{'type':''},{'type':Weapon2Type.shield, 'defence':20},'Defender',
                'Overreliant on that shield.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        if(self.cStatus == CombatStatus.Normal):
            print(self.name, 'struggled to pick up his shield')
        elif(self.weapon2['defence'] > 0):
            self.cStatus = CombatStatus.Blocking
            print(self.name, 'raised his shield!')
        else:
            self.cStatus = CombatStatus.Blocking
            print(self.name, 'braced himself')
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
        return [0, self.cStatus]

class SwordMaster(Enemy):
    def __init__(self):
        Enemy.__init__(self,'8','Sword Master',1000,'soldier',100,[],
                30, 10, 80, 60, 25,{'type':Weapon1Type.sword},{'type':''},'Attacker',
                'Very impressed by his sword.')
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Attacking
        target = ePriority_threat(p, r)
        impact = enemyAttack(e, target, target.shield)
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus, 'Hit': target, 'Damage':impact})
        return [impact, self.cStatus]

class Null(Enemy):
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'

def enemyAttack(e, p, b):
    if (e.attack() != 0):
        target = e.accuracy() + 100 - p.evasion()
        hit = random.randrange(0,100)
        critical = random.randrange(0,100)
        if ((e.aliment['outRange'] != True or (e.aliment['outRange'] == True and e.weapon1['type'] == Weapon1Type.spear)) and
            (p.aliment['outRange'] != True or (p.aliment['outRange'] == True and e.weapon1['type'] == Weapon1Type.spear)) and
            (e.aliment['outRange'] != True and p.aliment['outRange'] != True)):
            if (hit < target):
                impact = random.randrange(e.attack() - 5, e.attack() + 5)
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + p.defence())))
                im = impact
                if (p.cStatus == CombatStatus.Blocking):
                    impact = round(impact/10)
                    if (impact <= 0):
                        impact = 1
                    im = impact
                    if (p.weapon2.itemType == Weapon2Type.shield):
                        if (p.shield > 0):
                            print(p.name,'blocked!')
                            impact -= p.shield
                            if (impact < 0):
                                impact = 0
                            p.shield -= im
                elif((p.cStatus == CombatStatus.Attacking or CombatStatus.Parried) and p.weapon1.itemType== Weapon1Type.sword):
                    if(e.weapon1['type'] == Weapon1Type.sword or e.weapon1['type'] == Weapon1Type.dagger or
                       e.weapon1['type'] == Weapon1Type.spear or e.weapon1['type'] == Weapon1Type.axe or
                       e.weapon1['type'] == Weapon1Type.mace or e.weapon1['type'] == Weapon1Type.staff):
                        parry = random.randrange(0,100)
                        if (parry >= 20):
                            impact = 0
                            im = impact
                            pCombatStatus.Parried = CombatStatus.Countered
                        elif (parry >= 5):
                            impact = 0
                            im = impact
                            p.cStatus = CombatStatus.Parried
                p.health -= impact
                print('\n',e.name,' attacked!')
                if(critical >= 90):
                    print('Critical Hit!')
                if (p.cStatus == CombatStatus.Countered):
                    print(p.name,'parried!')
                    attack(p,e)
                elif (p.cStatus == CombatStatus.Parried):
                    print(p.name,'parried!')
                else:
                    print(p.name, 'took', impact, 'damage!')
                return im
            else:
                print('\n',e.name,' Missed!')
                return 0
        else:
            print('\n', p.name, ' was out of range')
            return 0
    else:
        print('\n',e.name, ' did not attack!')
        return 0
