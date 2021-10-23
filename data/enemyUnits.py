import random
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
#Reward Items
food = [{'itemId' : '1', 'name' : 'Blackberry', 'type' : ItemType.food,
          'recovers' : 3, 'count' : 0},
        {'itemId' : '2', 'name' : 'Dried Fruit', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0},
        {'itemId' : '3', 'name' : 'Hazelnut', 'type' : ItemType.food,
          'recovers' : 3, 'count' : 0},
        {'itemId' : '4', 'name' : 'Mushroom', 'type' : ItemType.food,
          'recovers' : 5, 'count' : 0, 'priority': 1},
        {'itemId' : '5', 'name' : 'Raw Bug Meat', 'type' : ItemType.food,
          'recovers' : 10, 'count' : 0}
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
class Cricket:
    def __init__(self):
        self.enId = '1'
        self.inId = '0'
        self.name = 'Cricket'
        self.maxHealth = 20
        self.health = self.maxHealth
        self.type = 'bug'
        self.Exp = 10
        self.drop = [{'item' : food[4], 'quantity':2}]
        self.baseAttack = 0
        self.baseDefence = 8
        self.baseAccuracy = 90
        self.baseSpeed = 10
        self.baseEvasion = 25
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':''}
        self.strat = 'Prey'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'Big grasshoppers with long antenna. Can jump a fair distance.'
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

class Hornet:
    def __init__(self):
        self.enId = '2'
        self.inId = '0'
        self.name = 'Hornet'
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
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'More hostile than usual this year. In the air they are annoying to hit but they are easy to kill.'
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

class Dummy:
    def __init__(self):
        self.enId = '3'
        self.inId = '0'
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
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
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
class Wall:
    def __init__(self):
        self.enId = '4'
        self.inId = '0'
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
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
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
    property
    def message(self, rd):
        return None
    property
    def action(self, e, p, r):
        self.cStatus = CombatStatus.Normal
        print(self.name, ' did not attack!')
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
        return [0, self.cStatus]
    
class Gowl_Rabbit:
    def __init__(self):
        self.enId = '5'
        self.inId = '0'
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
        self.weapon1 = {'type':Weapon1Type.spear}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'A Gowls Captain. There'"'"'s a reason for that. Well equiped and fast as rabbits are.'
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

class YoungCrow:
    def __init__(self):
        self.enId = '6'
        self.inId = '0'
        self.name = 'Young Crow'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.type = 'bird'
        self.Exp = 10
        self.drop = []
        self.baseAttack = 5
        self.baseDefence = 5
        self.baseAccuracy = 90
        self.baseSpeed = 40
        self.baseEvasion = 45
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':ItemType.projectile, 'name' : 'nuts', 'qnt' : 2}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':True, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'Likes to throw things at people.'
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

class ShieldMaster:
    def __init__(self):
        self.enId = '7'
        self.inId = '0'
        self.name = 'Shield Master'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.type = 'soldier'
        self.Exp = 100
        self.drop = []
        self.baseAttack = 5
        self.baseDefence = 5
        self.baseAccuracy = 90
        self.baseSpeed = 5
        self.baseEvasion = 45
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':Weapon2Type.shield, 'defence':20}
        self.strat = 'Defender'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'Overreliant on that shield'
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

class SwordMaster:
    def __init__(self):
        self.enId = '8'
        self.inId = '0'
        self.name = 'Sword Master'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.type = 'soldier'
        self.Exp = 100
        self.drop = []
        self.baseAttack = 30
        self.baseDefence = 10
        self.baseAccuracy = 80
        self.baseSpeed = 60
        self.baseEvasion = 25
        self.weapon1 = {'type':Weapon1Type.sword}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        self.cStatus = CombatStatus.Normal
        self.desc = 'Very impressed by his sword.'
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

class Null:
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
                    if (p.weapon2['type'] == Weapon2Type.shield):
                        if (p.shield > 0):
                            print(p.name,'blocked!')
                            impact -= p.shield
                            if (impact < 0):
                                impact = 0
                            p.shield -= im
                elif((p.cStatus == CombatStatus.Attacking or CombatStatus.Parried) and p.weapon1['type'] == Weapon1Type.sword):
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
