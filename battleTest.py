import os
import random
import pickle
#Character Base Stats
class Alder:
    def __init__(self):
        self.pId = '1'
        self.active = True
        self.name = 'Alder'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStamina = 100
        self.stamina = self.maxStamina
        self.type = 'playable'
        self.cLvl = 1
        self.cExp = 0
        self.cNext = 30
        self.skillPoints = 0
        self.baseAttack = 10
        self.baseDefence = 10
        self.baseAccuracy = 5
        self.baseSpeed = 10
        self.baseEvasion = 5
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
        self.weapon1 = weapons[0]
        self.weapon2 = weapons[0]
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'None'
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':True, 'effect':'Increases Evasion for five turns.'},
                        {'spId':'2','name':'Master archer', 'cost':10, 'active':False, 'inEffect':0, 'unlocked':False, 'effect':'Grants a critical for the next arrow fired within the next four turns.'}
                        ]
        self.manver = [{'mvId':'1','name':'Advence', 'type':'manuver', 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
                       {'mvId':'2','name':'Retreat', 'type':'manuver', 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
                       ]
        self.spells = [{'spId':'1','name':'Poison nettles', 'type':'Nature', 'attackType' : 'single', 'damage' : 1, 'cost':10, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Poisons an opponent'}
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
    def attackRanged(self):
        attackRanged = self.baseAttack
        if (self.weapon2['wpId'] != '0' and self.weapon2['type'] == 'bow'):
            attackRanged += self.weapon2['attack']
        else:
            attackRanged += 0
        return attackRanged
    property
    def defence(self):
        defence = self.baseDefence
        if (self.head['type'] == 'hat'):
            defence += self.head['defence']
        if (self.body['type'] == 'shirt'):
            defence += self.body['defence']
        if (self.legs['type'] == 'trousers'):
            defence += self.legs['defence']
        if (self.weapon2['type'] == 'shield'):
            defence += self.weapon2['defence']
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
    property
    def spell(self):
        if (self.weapon2['type'] == 'wand'):
            if(self.weapon2['spId'] == '1'):
                return self.spells[0]['unlocked'] == True
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nAccuracy: ', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2['name'], '\n'
              )
class Florace:
    def __init__(self):
        self.pId = '2'
        self.active = True
        self.name = 'Florace'
        self.maxHealth = 150
        self.health = self.maxHealth
        self.maxStamina = 150
        self.stamina = self.maxStamina
        self.type = 'playable'
        self.cLvl = 1
        self.cExp = 0
        self.cNext = 30
        self.skillPoints = 0
        self.baseAttack = 6
        self.baseDefence = 14
        self.baseAccuracy = 10
        self.baseSpeed = 11
        self.baseEvasion = 4
        self.head = armors[0]
        self.body = armors[1]
        self.legs = armors[3]
        self.weapon1 = weapons[0]
        self.weapon2 = weapons[0]
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'None'
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        self.special = [
                        ]
        self.manver = [{'mvId':'1','name':'Advence', 'type':'manuver', 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
                       {'mvId':'2','name':'Retreat', 'type':'manuver', 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
                       ]
        self.spells = [{'spId':'1','name':'Poison nettles', 'type':'Nature', 'attackType' : 'single', 'damage' : 1, 'cost':10, 'effectivness':100, 'active':False, 'inEffect':0,'unlocked':False, 'effect':'Poisons an opponent'}
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
    def attackRanged(self):
        attackRanged = self.baseAttack
        if (self.weapon2['wpId'] != '0' and self.weapon2['type'] == 'bow'):
            attackRanged += self.weapon2['attack']
        else:
            attackRanged += 0
        return attackRanged
    property
    def defence(self):
        defence = self.baseDefence
        if (self.head['type'] == 'hat'):
            defence += self.head['defence']
        if (self.body['type'] == 'shirt'):
            defence += self.body['defence']
        if (self.legs['type'] == 'trousers'):
            defence += self.legs['defence']
        if (self.weapon2['type'] == 'shield'):
            defence += self.weapon2['defence']
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
    def spell(self):
        if (self.weapon2['type'] == 'wand'):
            if(self.weapon2['spId'] == '1'):
                return self.spells[0]['unlocked'] == True
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nAccuracy: ', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2['name'], '\n'
              )
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
        self.drop = [{'item' : food[3], 'quantity':2}]
        self.baseAttack = 0
        self.baseDefence = 8
        self.baseAccuracy = 90
        self.baseSpeed = 10
        self.baseEvasion = 25
        self.weapon1 = {'type':''}
        self.weapon2 = {'type':''}
        self.strat = 'Prey'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
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
    property
    def action(self, e, p, s, r):
        if(self.health < self.maxHealth):
            self.cStatus = 'Escaping'
            print(self.name, ' fled!')
            r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
            return [0, self.cStatus]
        else:
            self.cStatus = 'None'
            print(self.name, ' stood wary.')
            r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus})
            return [0, self.cStatus]

class Wasp:
    def __init__(self):
        self.enId = '2'
        self.inId = '0'
        self.name = 'Wasp'
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
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
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
    property
    def action(self, e, p, s, r):
        self.cStatus = 'Attacking'
        target = ePriority_retaliation(p, e, r)
        impact = enemyAttack(e, target, s)
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
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'None'
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
    def action(self, e, p, s, r):
        self.cStatus = 'None'
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
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'None'
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
    def action(self, e, p, s, r):
        self.cStatus = 'None'
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
        self.weapon1 = {'type':'spear'}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
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
    property
    def action(self, e, p, s, r):
        self.cStatus = 'Attacking'
        target = ePriority_Alder(p)
        impact = enemyAttack(e, target, s)
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
        self.weapon2 = {'type':'projectile', 'name' : 'nuts', 'qnt' : 2}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':True, 'caught':False}
        self.cStatus = 'None'
        self.desc = 'Likes to throw things at people.'
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
    def action(self, e, p, s, r):
        self.cStatus = 'Attacking'
        target = ePriority_weakness(p)
        impact = enemyAttack(e, target, s)
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
        self.weapon2 = {'type':'shield', 'defence':20}
        self.strat = 'Defender'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'Blocking'
        self.desc = 'Overreliant on that shield'
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
    def action(self, e, p, s, r):
        if(self.cStatus == 'None'):
            print(self.name, 'struggled to pick up his shield')
        elif(self.weapon2['defence'] > 0):
            self.cStatus = 'Blocking'
            print(self.name, 'raised his shield!')
        else:
            self.cStatus = 'Blocking'
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
        self.weapon1 = {'type':'sword'}
        self.weapon2 = {'type':''}
        self.strat = 'Attacker'
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = 'None'
        self.desc = 'Very impressed by his sword.'
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
    def action(self, e, p, s, r):
        self.cStatus = 'Attacking'
        target = ePriority_threat(p, r)
        impact = enemyAttack(e, target, s)
        r.append({'Id': self.inId, 'Who':self.name, 'Type': self.type, 'Status' : self.cStatus, 'Hit': target, 'Damage':impact})
        return [impact, self.cStatus]

class Null:
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'

def gainExperience(p):
    experience = input('Increase experience by how much?: ')
    if (experience.isdigit()):
        e = int(experience)
        p.cExp += e
    else:
        print('Number values only!')
    
def levelUP(p):
    print(p.cNext, ' ', p.cExp)
    if(p.cExp >= p.cNext):
        while(p.cExp >= p.cNext and p.cLvl < 60):
            if(p.cLvl < 60):
                p.cLvl += 1
                p.maxHealth += 5
                p.maxStamina += 5
                p.health += 5
                p.stamina += 5
                p.baseAttack += 2
                p.baseDefence += 2
                p.baseAccuracy += 2
                p.baseSpeed += 2
                p.baseEvasion += 2
                p.skillPoints += 1
                print(p.name,' leveled up!')
                if(p.cLvl == 60):
                    print('Max Level')
                else:
                    if(p.cLvl < 5):
                        p.cNext = round(p.cNext*1.65)
                    elif(p.cLvl < 20):
                        p.cNext = round(p.cNext*1.55)
                    elif(p.cLvl < 30):
                        p.cNext = round(p.cNext*1.45)
                    elif(p.cLvl < 40):
                        p.cNext = round(p.cNext*1.35)
                    elif(p.cLvl < 50):
                        p.cNext = round(p.cNext*1.25)
                    elif(p.cLvl < 60):
                        p.cNext = round(p.cNext*1.15)
                    print(p.cNext)
                   

#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'sword', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'sword', 'description' : 'Legendary sword of the Scion.',
            'attack' : 500, 'weight' : 5, 'count' : 0},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'dagger', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0},
           {'wpId' : '3', 'name' : 'Relic Sword', 'type' : 'sword', 'description' : '',
            'attack' : 10, 'weight' : 3, 'count' : 0},
           {'wpId' : '4', 'name' : 'Relic Spear', 'type' : 'spear', 'description' : '',
            'attack' : 8, 'weight' : 3, 'count' : 0},
           {'wpId' : '5', 'name' : 'Relic Axe', 'type' : 'axe', 'description' : '',
            'attack' : 12, 'weight' : 3, 'count' : 0},
           {'wpId' : '6', 'name' : 'Old Club', 'type' : 'mace', 'description' : '',
            'attack' : 10, 'weight' : 4, 'count' : 0},
           {'wpId' : '7', 'name' : 'Crooked Stick', 'type' : 'staff', 'description' : '',
            'attack' : 3, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Bow', 'type' : 'bow', 'description' : 'A large bow made for practise.',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Training Crossbow', 'type' : 'crossbow', 'description' : '',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Grass Sling', 'type' : 'sling', 'description' : 'A sling made from grass; not very practical',
            'attack' : 20, 'weight' : 2, 'count' : 0},
           {'wpId' : '1', 'name' : 'Wooden Shield', 'type' : 'shield', 'description' : 'A basic round wooden shield.',
            'defence' : 20, 'weight' : 4, 'count' : 0},
           {'wpId' : '1', 'name' : 'Poison wand', 'type' : 'wand', 'description' : 'A wand containing a weak poison',
            'spell' : 'Poison Nettle', 'weight' : 1, 'count' : 0}
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
projec = [{'itemId' : '1', 'name' : 'Primitive Arrow', 'type' : 'projectile', 'description' : 'Arrows made from stone heads and twigs.',
           'weapon' : 'bow', 'damage' : 10, 'count' : 0},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : 'toss',  'description' : 'A rope net to catch your enemies.',
           'weapon' : 'none', 'damage' : 0, 'count' : 0},
          {'itemId' : '3', 'name' : 'Wooden Bolt', 'type' : 'projectile',  'description' : '',
           'weapon' : 'crossbow', 'damage' : 10, 'count' : 0},
          {'itemId' : '4', 'name' : 'Softstone', 'type' : 'projectile',  'description' : '',
           'weapon' : 'sling', 'damage' : 10, 'count' : 0}
          ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : 'healing', 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0}
         ]

#Inventory
inv = []
#Set Class
alder = Alder()
florace = Florace()

#Save settings
def save():
    data = [alder, florace, inv]
    PIK = 'data/combat_file.dat'
    with open(PIK, "wb") as f:
        pickle.dump(data, f)
    print ('Data Saved!')
    
def loadSet():
    global alder, florace, inv
    PIK = 'data/combat_file.dat'
    try:
        with open(PIK, "rb") as f:
            data = pickle.load(f)
            alder = data[0]
            florace = data[1]
            inv = data[2]
            print(florace)
    except:
        print('Saved file not found!')
    print ('Data Loaded!')
    

#Increment items
#Add a new item to the inventory if is is not already in there
def itemCount(item, amount):
    inInv = False
    for i in inv:
        if (item['type'] == 'sword' and i['type'] == 'sword' or
            item['type'] == 'dagger' and i['type'] == 'dagger' or
            item['type'] == 'spear' and i['type'] == 'spear' or
            item['type'] == 'axe' and i['type'] == 'axe' or
            item['type'] == 'mace' and i['type'] == 'mace' or
            item['type'] == 'staff' and i['type'] == 'staff'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'shield' and i['type'] == 'shield'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'bow' and i['type'] == 'bow'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'crossbow' and i['type'] == 'crossbow'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'sling' and i['type'] == 'sling'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'shield' and i['type'] == 'shield'):
            if (i['wpId'] == item['wpId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'wand' and i['type'] == 'wand'):
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
        elif (item['type'] == 'projectile' and i['type'] == 'projectile'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
        elif (item['type'] == 'toss' and i['type'] == 'toss'):
            if (i['itemId'] == item['itemId']):
                item['count'] += amount
                inInv = True
    if (inInv == False):
        item['count'] += amount
        inv.append(item)

#Items Setter
def equip(p):
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
                        if(p.head['armId'] != '0'):
                            inv.append(p.head)
                        p.head = i
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
                        if(p.body['armId'] != '1'):
                            inv.append(p.body)
                        p.body = i
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
                        if(p.legs['armId'] != '1'):
                            inv.append(p.legs)
                        p.legs = i
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
                if(i['type'] == 'sword' or i['type'] == 'dagger' or i['type'] == 'spear' or
                   i['type'] == 'axe' or i['type'] == 'mace' or i['type'] == 'staff'):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon1['attack'])
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(p.weapon1['wpId'] != '0'):
                            inv.append(p.weapon1)
                        p.weapon1 = i
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
                if(i['type'] == 'bow' or i['type'] == 'crossbow' or i['type'] == 'sling' or
                   i['type'] == 'shield' or i['type'] == 'wand'):
                    count +=1
                    equipable.append(i)
                    if(i['type'] == 'bow'):
                        if (p.weapon2['type'] == 'bow' or p.weapon2['type'] == 'crossbow' or p.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'crossbow'):
                        if (p.weapon2['type'] == 'bow' or p.weapon2['type'] == 'crossbow' or p.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'sling'):
                        if (p.weapon2['type'] == 'bow' or p.weapon2['type'] == 'crossbow' or p.weapon2['type'] == 'sling'):
                            print(count, ': ', i['name'], '- Attack: +', i['attack'] - p.weapon2['attack'])
                        else:
                            print(count, ': ', i['name'], '- Attack: +', i['attack'])
                    elif(i['type'] == 'shield'):
                        if (p.weapon2['type'] == 'shield'):
                            print(count, ': ', i['name'], '- Defence: +', i['defence'] - p.weapon2['defence'])
                        else:
                            print(count, ': ', i['name'], '- Defence: +', i['defence'])
                    elif(i['type'] == 'wand'):
                        print(count, ': ', i['name'], '- Spell: ', i['spell'])
                        for j in p.spells:
                            if (j['spId'] == i['wpId']):
                                j['unlocked'] = True
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        print(i['name'], 'equiped')
                        if(p.weapon2['wpId'] != '0'):
                            inv.append(p.weapon2)
                        p.weapon2 = i
                        i['count'] -= 1
                        if(i['count'] <= 0):
                            inv.remove(i)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == 'e'):
            equiping = False
        save()

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
            print('1: Alder')
            print('2: Florace')
            i = input('Item set:')
            if (i == '1'):
                equip(alder)
            elif (i == '2'):
                equip(florace)
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
            print('1: primary weaponry')
            print('2: secondary weaponry')
            print('3: health and stamina items')
            j = input('Item set:')
            if (j == '1'):
                print('\nDagger obtained')
                itemCount(weapons[2], 1)
                print('\nLeif obtained')
                itemCount(weapons[1], 1)
                print('\nSword obtained')
                itemCount(weapons[3], 1)
                print('\nSpear obtained')
                itemCount(weapons[4], 1)
                print('\nAxe obtained')
                itemCount(weapons[5], 1)
                print('\nClub obtained')
                itemCount(weapons[6], 1)
                print('\nStaff obtained')
                itemCount(weapons[7], 1)
            elif (j == '2'):
                print('\nBow obtained')
                itemCount(weapons[8], 1)
                print('\nCrossbow obtained')
                itemCount(weapons[9], 1)
                print('\nSling obtained')
                itemCount(weapons[10], 1)
                print('\nShield obtained')
                itemCount(weapons[11], 1)
                print('\nWand obtained')
                itemCount(weapons[12], 1)
                print('\nArrows obtained')
                itemCount(projec[0], 5)
                print('\nNet obtained')
                itemCount(projec[1], 1)
                print('\nBolts obtained')
                itemCount(projec[2], 5)
                print('\nStones obtained')
                itemCount(projec[3], 5)
            elif (j == '3'):
                print('\nBlackberries obtained')
                itemCount(food[0], 5)
                print('\nBandage obtained')
                itemCount(items[0], 5)
            save()
        elif (i == '2'):
            inventory()
        elif (i == '3'):
            print('1: Alder')
            print('2: Florace')
            j = input('Item set:')
            if (j == '1'):
                equip(alder)
            elif (j == '2'):
                equip(florace)
        elif (i == 'e'):
            manageEquip = False

def setFoe():
    global enemy
    setting = True
    heroes = [alder, florace]
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
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
            j = input('Enemy: ')
            if (j == '1'):
                enemy[0] = Cricket()
            elif (j == '2'):
                enemy[0] = Wasp()
            elif (j == '3'):
                enemy[0] = Dummy()
            elif (j == '4'):
                enemy[0] = Wall()
            elif (j == '5'):
                enemy[0] = Gowl_Rabbit()
            elif (j == '6'):
                enemy[0] = YoungCrow()
            elif (j == '7'):
                enemy[0] = ShieldMaster()
            elif (j == '8'):
                enemy[0] = SwordMaster()
        elif (i == '2'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
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
                enemy[1] = Wall()
            elif (j == '5'):
                enemy[1] = Gowl_Rabbit()
            elif (j == '6'):
                enemy[1] = YoungCrow()
            elif (j == '7'):
                enemy[1] = ShieldMaster()
            elif (j == '8'):
                enemy[1] = SwordMaster()
        elif (i == '3'):
            print('\nSelect Enemy')
            print('1: Cricket')
            print('2: Wasp')
            print('3: Dummy')
            print('4: Wall')
            print('5: Gowls Captain')
            print('6: Young Crow')
            print('7: Shield Master')
            print('8: Sword Master')
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
                enemy[2] = Wall()
            elif (j == '5'):
                enemy[2] = Gowl_Rabbit()
            elif (j == '6'):
                enemy[2] = YoungCrow()
            elif (j == '7'):
                enemy[2] = ShieldMaster()
            elif (j == '8'):
                enemy[2] = SwordMaster()
        elif (i == '4'):
            if(enemy[0].enId != null.enId):
                victory = False
                enemy[0].inId = '1'
                enemy[1].inId = '2'
                enemy[2].inId = '3'
                victory = battle(heroes, enemy)
                if (victory == True):
                    print('You won the fight!')
                else:
                    print('You lost the fight!')
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
    if (alder.active == True):
        alder.cExp += ex
        print('Alder gained ', ex, ' experience.')
        levelUP(alder)
    if (florace.active == True):
        florace.cExp += ex
        print('Florace gained ', ex, ' experience.')
        levelUP(florace)
    for i in e:
        if (len(i.drop) > 0):
            print(i.name,' dropped ', i.drop[0]['item']['name'], ' x', i.drop[0]['quantity'])
            itemCount(i.drop[0]['item'], i.drop[0]['quantity'])
    save()

def death():
    for i in alder.special:
        i['active'] = False
        i['inEffect'] = 0
    alder.health = alder.maxHealth
    alder.stamina = alder.maxHealth
    florace.health = florace.maxHealth
    florace.stamina = florace.maxHealth
    print('\nAlder was slain.')
    i = input()
    dostuff = False

def hunger(p):
    if(p.stamina <= 0):
        p.health -= 1
        print(p.name,'needs to eat!')
    if(p.stamina < 0):
        p.stamina = 0

def enemyAttack(e, p, b):
    if (e.attack() != 0):
        target = e.accuracy() + 100 - p.evasion()
        hit = random.randrange(0,100)
        critical = random.randrange(0,100)
        if ((e.aliment['outRange'] != True or (e.aliment['outRange'] == True and e.weapon1['type'] == 'spear')) and
            (p.aliment['outRange'] != True or (p.aliment['outRange'] == True and e.weapon1['type'] == 'spear')) and
            (e.aliment['outRange'] != True and p.aliment['outRange'] != True)):
            if (hit < target):
                impact = random.randrange(e.attack() - 5, e.attack() + 5)
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + p.defence())))
                im = impact
                if (p.cStatus == 'Blocking'):
                    impact = round(impact/10)
                    if (impact <= 0):
                        impact = 1
                    im = impact
                    if (p.weapon2['type'] == 'shield'):
                        if (p.shield > 0):
                            print(p.name,'blocked!')
                            impact -= p.shield
                            if (impact < 0):
                                impact = 0
                            p.shield -= im
                elif((p.cStatus == 'Attacking' or p.cStatus == 'Parried') and p.weapon1['type'] == 'sword'):
                    if(e.weapon1['type'] == 'sword' or e.weapon1['type'] == 'dagger' or
                       e.weapon1['type'] == 'spear' or e.weapon1['type'] == 'axe' or
                       e.weapon1['type'] == 'mace' or e.weapon1['type'] == 'staff'):
                        parry = random.randrange(0,100)
                        if (parry >= 20):
                            impact = 0
                            im = impact
                            p.cStatus = 'Countered'
                        elif (parry >= 5):
                            impact = 0
                            im = impact
                            p.cStatus = 'Parried'
                p.health -= impact
                print('\n',e.name,' attacked!')
                if(critical >= 90):
                    print('Critical Hit!')
                if (p.cStatus == 'Countered'):
                    print(p.name,'parried!')
                    attack(p,e)
                elif (p.cStatus == 'Parried'):
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

def enemyFlee(e):
    print(e.name, ' fled!')

#Attack Enemy
def attack(p, e):
    numOfAtk = 1
    impact = 0
    if (p.weapon1['type'] == 'dagger'):
        numOfAtk += 1
    target = p.accuracy() + 100 - e.evasion()
    hit = random.randrange(0,100)
    critical = random.randrange(0,100)
    p.stamina -= 5
    while(numOfAtk > 0):
        if (p.ammo['loaded'] == True):
            p.cStatus = 'RAttacking'
            if (hit < target):
                impact = random.randrange(p.attackRanged() - 3, p.attackRanged() + 3)
                impact += p.ammo['damage']
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + e.defence())))
                im = impact
                if (e.cStatus == 'Blocking'):
                    impact = round(impact/10)
                    if (impact <= 0):
                        impact = 1
                    im = impact
                    if (e.weapon2['type'] == 'shield'):
                        if (e.weapon2['defence'] > 0):
                            print('Attack blocked!')
                            impact -= e.weapon2['defence']
                            if (impact < 0):
                                impact = 0
                print('\n',p.name,' fired a', p.ammo['name'], '!')
                if(critical >= 90):
                    print('Critical Hit!')
                    if (p.weapon2['type'] == 'sling'):
                        e.aliment = 'Stun'
                e.health -= impact
                print(e.name, ' took ', impact, ' damage!')
                p.ammo['loaded'] = False
                if(e.health <= 0):
                    print(e.name, ' defeated.')
                return im
            else:
                print('\n',p.name,' Missed')
                return 0
        else:
            p.cStatus = 'Attacking'
            if ((e.aliment['outRange'] != True or (e.aliment['outRange'] == True and p.weapon1['type'] == 'spear')) and
                (p.aliment['outRange'] != True or (p.aliment['outRange'] == True and p.weapon1['type'] == 'spear')) and
                (e.aliment['outRange'] != True and p.aliment['outRange'] != True)):
                print(p.aliment['outRange'])
                if (hit < target):
                    impact = random.randrange(p.attack() - 5, p.attack() + 5)
                    if(p.weapon1['wpId'] != '0'):
                        if (critical >= 90):
                            impact += 10
                        impact = round(impact * (100/(100 + e.defence())))
                        im = impact
                        if (impact <= 0):
                            impact = 1
                        if (e.cStatus == 'Blocking'):
                            impact = round(impact/10)
                            if (impact <= 0):
                                impact = 1
                            im = impact
                            if (e.weapon2['defence'] > 0):
                                if (p.weapon1['type'] == 'axe'):
                                    print('Shield repealed!')
                                    e.cStatus = 'None'
                                else:
                                    print('Attack blocked!')
                                    impact -= e.weapon2['defence']
                                if (impact < 0):
                                    impact = 0
                        e.health -= impact
                        if (p.cStatus == 'Countered'):
                            print('\n',p.name,' countered!')
                        else:
                            print('\n',p.name,' attacked!')
                        if(critical >= 90):
                            print('Critical Hit!')
                            if (p.weapon1['type'] == 'mace'):
                                e.aliment['stun'] = True
                        print(e.name, ' took ', impact, ' damage!')
                        if(e.health <= 0):
                            print(e.name, ' defeated.')
                        return im
                    else:
                        print('\nBut',p.name, ' was unarmed')
                        return 0
                else:
                    print('\n',p.name,' Missed')
                    return 0
            else:
                print('\n', e.name, ' was out of range')
        numOfAtk -= 1
    if(e.health <= 0):
        print(e.name, ' defeated.')
    if (p.ammo['loaded'] == False):
        p.ammo['name'] = ''
        p.ammo['damage'] = 0

#Check if special effect are still active and deactivate them it they are not.
def inEffect(p, e):
    for i in alder.special:
        if(i['active'] == True):
            i['inEffect'] -= 1
            if (i['inEffect'] <= 0):
                i['active'] = False
                print(alder.name,"'s ", i['name'], ' has worn off.')
    for i in p.manver:
        for en in e:
            if (i['mvId'] == '1' and (p.aliment['outRange'] == 'True' or en.aliment['outRange'] == 'True')):
                advencable = False
                if (en.aliment['outRange'] == 'False'):
                    advancable = False
                else:
                    advancable = True
                if (advancable == True):
                    j = i + 1
                    i['active'] = True
                    j['active'] = False
                    print(i, j)
            elif (i['mvId'] == '2' and (p.aliment['outRange'] == 'False')):
                j = i - 1
                i['active'] = True
                j['active'] = False


def magic(p, e, spell):
    hit = random.randrange(0,100)
    damage = spell['damage']
    if (p.weapon1['type'] == 'staff'):
        boost = damage / 20
        if (boost < 1):
            boost = 1
        damage += round(boost)
    count = 1
    for i in e:
        print(count, ') ', i.name)
        count += 1
    target = input('Cast on:')
    if (hit < spell['effectivness']):
        if (spell['attackType'] == 'single'):
            count = 1
            for i in e:
                if (target == str(count)):
                    if (spell['spId'] == '1'):
                        i.aliment['poison'] = True
                count +=1
            i.health -= damage
            print(i.name, 'took', damage, 'from', spell['name'],'!')
    else:
        print('The spell missed!')
        
def manuver(p, e, m):
    if (m['type'] == 'manuver'):
        if (m['mvId'] == '1'):
            active = True
            for i in e:
                if(i.aliment['outRange'] == False):
                    active = False
            if (p.aliment['outRange'] == True):
                p.aliment['outRange'] = False
                print(p.name,'advanced closer!')
            elif (active == True):
                for i in e:
                    i.aliment['outRange'] = False
                print(p.name,'advanced closer!')
            else:
                print(p.name,'is too close!')
        if (m['mvId'] == '2'):
            if (p.aliment['outRange'] == False):
                p.aliment['outRange'] = True
                print(p.name,'retreated to the rear!')
            else:
                print(p.name,'is too far away!')
    
def special(p, e, r):
    print('\nSpecial Ability')
    count = 0
    for i in p.special:
        if (i['unlocked'] == True):
            count += 1
            print(count, ') ',i['name'], ' - ', i['cost'], ' stamina')
    print('Manuvers')
    for i in p.manver:
        if (i['unlocked'] == True):
            count += 1            
            print(count, ') ',i['name'], ' - ', i['cost'], ' stamina')                
    print('Spells')
    for i in p.spells:
        if (i['unlocked'] == True):
            count += 1
            print(count, ') ',i['name'], ' - ', i['cost'], ' stamina')
    if (count == 0):
        print('None')
    sp = input('Use: ')
    count2 = 0
    for i in p.special:
        if (i['unlocked'] == True):
            count2 += 1
            if (sp == str(count2)):
                p.cStatus = 'Specializing'
                i['active'] = True
                if (i['spId'] == '1'):
                    p.stamina -= i['cost']
                    i['inEffect'] = 6
                elif (i['spId'] == '2'):
                    p.stamina -= i['cost']
                    i['inEffect'] = 5
                print('\n', p.name, ' uses ', i['name'],'.')
                r.append({'Id': i.pId, 'Who':p.name, 'Type': i.type, 'Status':p.cStatus, 'SpecialType':'special', 'Special':i['name']})
    for i in p.manver:
        if (i['unlocked'] == True):
            count2 += 1
            if (sp == str(count2)):
                p.cStatus = 'Specializing'
                p.stamina -= i['cost']
                manuver(p,e,i)
                r.append({'Id': i.pId, 'Who':p.name, 'Type': i.type, 'Status':p.cStatus, 'SpecialType':'manuver', 'Manuver':i['name']})
    for i in p.spells:
        if (i['unlocked'] == True):
            count2 += 1
            if (sp == str(count2)):
                p.cStatus = 'Specializing'
                i['active'] = True
                p.stamina -= i['cost']
                magic(p, e, i)
                print('\n', p.name, ' uses ', i['name'],'.')
                r.append({'Id': i.pId, 'Who':p.name, 'Type': i.type, 'Status':p.cStatus, 'SpecialType':'magic', 'Spell':i['name']})

#Use Item
def item(p, e, r):
    use = []
    using = True
    y = ''
    while(using == True):
        print('\nBag Items')
        count = 1
        if (y == '' or y == 'healing' or y == 'Healing' or
            y == 'health' or y == 'Health'):
            print('Healing')
            for i in inv:
                if(i['type'] == 'healing'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'food' or y == 'Food' or
            y == 'consumables' or y == 'Consumables'):
            print('Food')
            for i in inv:
                if(i['type'] == 'food'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'projectiles' or y == 'Projectiles'):
            print('Projectiles')
            for i in inv:
                if(i['type'] == 'projectile' or i['type'] == 'toss'):
                    print(count, ': ', i['name'], ' x', i['count'])
                    use.append(i)
                    count += 1
        print('e - exit')
        if(count != 0):
            count = 1
            u = input('use item: ')
            if (u == '' or u == 'food' or u == 'Food' or u == 'consumables' or u == 'Consumables' or u == 'healing' or u == 'Healing' or
                u == 'health' or u == 'Health' or u == 'projectiles' or u == 'Projectiles' or u == 'e'):
                y = u
            for i in use:
                if (u == str(count)):
                    if (i['type'] == 'healing'):
                        p.health += i['heals']
                        print(p.name, ' recoved ', i['heals'], ' health')
                        if (p.health > p.maxHealth):
                            p.health = p.maxHealth
                        p.cStatus = 'Using'
                        using = False
                    elif (i['type'] == 'food'):
                        p.stamina += i['recovers']
                        print(p.name, ' recoved ', i['recovers'], ' stamina')
                        if (p.stamina > p.maxStamina):
                            p.stamina = p.maxStamina
                        p.cStatus = 'Using'
                        using = False
                    elif (i['type'] == 'projectile'):
                        print(u, count)
                        if (i['weapon'] == 'bow'):
                            if(p.weapon2['type'] == 'bow'):
                                print('\nArrow loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                alder.cStatus = 'Using'
                                using = False
                            else:
                                print('Bow required!')
                                using = False
                        elif (i['weapon'] == 'crossbow'):
                            if(p.weapon2['type'] == 'crossbow'):
                                print('\nBolt loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                p.cStatus = 'Using'
                                using = False
                            else:
                                print('Crossbow required!')
                                using = False
                        elif (i['weapon'] == 'sling'):
                            if(p.weapon2['type'] == 'sling'):
                                print('\nStone loaded!')
                                p.ammo['name'] = i['name']
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['damage']
                                p.cStatus = 'Using'
                                using = False
                            else:
                                print('Sling required!')
                                using = False
                    elif (i['type'] == 'toss'):
                        count = 1
                        for j in e:
                            print(count, ': ', j.name)
                            count += 1
                        count = 1
                        target = input('Throw at: ')
                        for j in e:
                            if (target == str(count)):
                                print('\n',p.name,'threw ', i['name'])
                                j.aliment['caught'] = True 
                                p.cStatus = 'Using'
                                using = False
                            count += 1
                    i['count'] -= 1
                    if(i['count'] <= 0):
                        inv.remove(i)
                    r.append({'Id': i.pId, 'Who':p.name, 'Type': i.type, 'Status':p.cStatus, 'ItemType':i['type']})
                count +=1
            if u == 'e':
                using = False
            use.clear()

def fightOrder(e):
    return e.speed()

def weakest(e):
    return e.health

def ePriority_weakness(heroes):
    heroes.sort(key=lambda x: x.health, reverse=False)
    for i in heroes:
        if (i.health > 0):
            return i

def ePriority_threat(heroes, record):
    attacks = []
    for i in record:
        if (i['Type'] == 'playable' and i['Status'] == 'Attacking'):
            attacks.append(i)
    attacks.sort(key=lambda x: x['Damage'], reverse=True)
    for i in attacks:
        for j in heroes:
            if (i['Id'] == j.pId):
                if (j.health > 0):
                    return j
    if (len(attacks) == 0):
        return ePriority_weakness(heroes)
    
def ePriority_retaliation(heroes, e, record):
    attacks = []
    for i in record:
        if (i['Type'] == 'playable' and i['Status'] == 'Attacking' and
            i['Hit'].inId == e.inId):
                attacks.append(i)
    for i in attacks:
        for j in heroes:
            if (i['Id'] == j.pId):
                if (j.health > 0):
                    return j
            
    if (len(attacks) == 0):
        return ePriority_weakness(heroes)

def ePriority_Alder(heroes):
    for i in heroes:
        if (i.health > 0):
            if (i.pId == '1'):
                return i
            elif (i.pId == '2'):
                return i
            else:
                return ePriority_weakness(heroes)

#Combat interface
def battle(h, e):
    os.system('clear')
    global alder, florace
    heroes = []
    enemys = []
    record = []
    for i in h:
        if (i.active == True):
            heroes.append(i)
    for i in e:
        if i.enId != '0':
            enemys.append(i)
    combatants = heroes + enemys
    fighting = True
    winner = False
    count = 1
    for i in heroes:
        if (i.weapon2['type'] == 'shield'):
            i.shield = i.weapon2['defence']
    shield = 0
    useShield = True
    while(fighting == True):
        for i in heroes:
            hunger(i)
        combatants.sort(key=fightOrder, reverse=True)
        #print(combatants)
        for i in combatants:
            if (fighting == True):
                #Win condition
                if (enemys[0].health <= 0):
                    k = 0
                    for remaining in enemys:
                        if (remaining.health <= 0):
                            k += 1
                    if (k == len(enemys)):
                        winner = True
                #Death Condition
                if(i.health <= 0 and i.type == 'playable'):
                    k = 0
                    #record.append({'Who':i.name, 'Status':'defeated'})
                    for remaining in heroes:
                        if (remaining.health <= 0):
                            k += 1
                    if (k == len(heroes)):
                        #fighting = False
                        death()
                        return False
                #Win
                elif(winner == True):
                    for j in alder.special:
                        j['active'] = False
                        j['inEffect'] = 0
                    fighting = False
                    win(enemys)
                    for i in record:
                        print(i)
                    return True
                if (i.type == 'playable' and i.health > 0):
                    inEffect(i, enemys)
                    i.cStatus = 'None'
                    while(i.cStatus == 'None'):
                        print('\n',i.name)
                        if (i.ammo['loaded'] == True):
                            print('Ranged weapon set!')
                        print("Health: ", i.health, '/', i.maxHealth, "| Stamina: ", i.stamina, '/', i.maxStamina)
                        print("1) Attack     3) Appraise     5) Item")
                        print("2) Block      4) Special      6) Flee")
                        j = input('Action: ')
                        if (j == '1' or j == 'attack' or j == 'Attack'):
                            print('\nEnemies')
                            k = 1
                            for j in enemys:
                                if (j.health > 0):
                                    print(k, ': ', j.name)
                                    k += 1
                            target = input('Attack: ')
                            k = 1
                            for j in enemys:
                                if (j.health > 0):
                                    if (target == str(k)):
                                        impact = attack(i, j)
                                        if (j.cStatus == 'Blocking' and impact > 0):
                                            j.weapon2['defence'] -= impact
                                        record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus, 'Hit': j, 'Damage':impact})
                                    k += 1
                        elif (j == '2' or j == 'block' or j == 'Block'):
                            i.cStatus = 'Blocking'
                            #if (i.weapon2['type'] == 'shield'):
                                #if (useShield == True):
                                    #useShield = False
                            record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus})
                        elif (j == '3' or j == 'appraise' or j == 'Appraise'):
                            for j in enemys:
                                print('\n',j.name, 'Health:', j.health,'/',j.maxHealth)
                                print(j.desc)
                        elif (j == '4' or j == 'special' or j == 'Special'):
                            special(i, enemys, record)
                        elif (j == '5' or j == 'item' or j == 'Item'):
                            item(i, enemys, record)
                        elif (j == '6' or j == 'flee' or j == 'Flee'):
                            j = input('Are you sure you want to run?(y/n)')
                            if (j == 'y' or j == 'Y' or j == 'yes' or j == 'Yes'):
                                i.cStatus = 'Escaping'
                                record.append({'Id': i.pId, 'Who':i.name, 'Type': i.type, 'Status':i.cStatus})
                                #fighting = False
                                return False
                else:
                    if(i.health > 0):
                        if (i.aliment['poison'] == True):
                            poison = i.maxHealth / 10
                            if (round(poison) < 0):
                                poison = 1
                            i.health -= round(poison)
                            print(i.name, 'took', round(poison), 'damage from poison!')
                            record.append({'Id': i.enId, 'Who':i.name, 'Type': i.type, 'Aliment':'poison', 'Damage':round(poison)})
                        if (i.aliment['caught'] == True):
                            escape = random.randrange(0, 100)
                            if (i.type == 'bug'):
                                if (escape >= 95):
                                    print('The',i.name, 'escaped the net!')
                                    i.aliment['caught'] = False
                                else:
                                    print('The', i.name,' is tangled in a net!')
                            elif (i.type == 'soldier'):
                                if (escape >= 30):
                                    print(i.name, 'escaped the net!')
                                    i.aliment['caught'] = False
                                else:
                                    print(i.name,' is tangled in a net!')
                            record.append({'Id': i.enId, 'Who':i.name, 'Type': i.type, 'Aliment':'caught', 'Caught':i.aliment['caught']})
                        elif (i.aliment['stun'] == True):
                            print(i.name, 'was stunned!')
                            i.aliment['stun'] = False
                        else:
                            impact = i.action(i, heroes, shield, record)[0]
                            if (alder.cStatus == 'Blocking' and impact > 0):
                                shield -= impact
                for j in reversed(enemys):
                    if (j.cStatus == 'Escaping'):
                        enemys.remove(j)
                        if (len(enemys) == 0):
                            fighting = False
                            return True
        count += 1

def unit():
    units = True
    while(units == True):
        print('\n1: Print stats.')
        print('2: Add experience')
        print('3: Recover')
        print('4: Reset')
        print('e - Exit')
        a = input('Action: ')
        if (a == '1'):
            alder.stats()
            florace.stats()
        elif (a == '2'):
            a = input('Action: ')
            if (a == '1'):
                gainExperience(alder)
                levelUP(alder)
            elif (a == '2'):
                gainExperience(florace)
                levelUP(florace)
        elif (a == '3'):
            alder.health = alder.maxHealth
            alder.stamina = alder.maxStamina
            florace.health = florace.maxHealth
            florace.stamina = florace.maxStamina
        elif (a == '4'):
            alder.maxHealth = 100
            alder.health = alder.maxHealth
            alder.maxStamina = 100
            alder.stamina = alder.maxStamina
            alder.cLvl = 1
            alder.cExp = 0
            alder.cNext = 30
            alder.skillPoints = 0
            alder.baseAttack = 10
            alder.baseDefence = 10
            alder.baseAccuracy = 5
            alder.baseSpeed = 10
            alder.baseEvasion = 5
            alder.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
            alder.cStatus = 'None'
            alder.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                              {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                              {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                              {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                              {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                              {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                              {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                              ]
            
            florace.maxHealth = 150
            florace.health = florace.maxHealth
            florace.maxStamina = 80
            florace.stamina = florace.maxStamina
            florace.cLvl = 1
            florace.cExp = 0
            florace.cNext = 30
            florace.skillPoints = 0
            florace.baseAttack = 6
            florace.baseDefence = 14
            florace.baseAccuracy = 10
            florace.baseSpeed = 11
            florace.baseEvasion = 4
            florace.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
            florace.cStatus = 'None'
            florace.statBoost = [{'No':'1', 'name':'Health 1', 'active':False, 'boost':10, 'stat' : 'h'}, {'No':'2', 'name':'Health 2', 'active':False, 'boost':50, 'stat' : 'h'}, {'No':'3', 'name':'Health 3', 'active':False, 'boost':300, 'stat' : 'h'},
                              {'No':'1', 'name':'Stamina 1', 'active':False, 'boost':10, 'stat' : 's'}, {'No':'2', 'name':'Stamina 2', 'active':False, 'boost':50, 'stat' : 's'}, {'No':'3', 'name':'Stamina 3', 'active':False, 'boost':300, 'stat' : 's'},
                              {'No':'1', 'name':'Attack 1', 'active':False, 'boost':5, 'stat' : 'at'}, {'No':'2', 'name':'Attack 2', 'active':False, 'boost':10, 'stat' : 'at'}, {'No':'3', 'name':'Attack 3', 'active':False, 'boost':50, 'stat' : 'at'},
                              {'No':'1', 'name':'Defence 1', 'active':False, 'boost':5, 'stat' : 'df'}, {'No':'2', 'name':'Defence 2', 'active':False, 'boost':10, 'stat' : 'df'}, {'No':'3', 'name':'Defence 3', 'active':False, 'boost':50, 'stat' : 'df'},
                              {'No':'1', 'name':'Accuracy 1', 'active':False, 'boost':5, 'stat' : 'ac'}, {'No':'2', 'name':'Accuracy 2', 'active':False, 'boost':10, 'stat' : 'ac'}, {'No':'3', 'name':'Accuracy 3', 'active':False, 'boost':50, 'stat' : 'ac'},
                              {'No':'1', 'name':'Speed 1', 'active':False, 'boost':5, 'stat' : 'sp'}, {'No':'2', 'name':'Speed 2', 'active':False, 'boost':10, 'stat' : 'sp'}, {'No':'3', 'name':'Speed 3', 'active':False, 'boost':50, 'stat' : 'sp'},
                              {'No':'1', 'name':'Evasion 1', 'active':False, 'boost':5, 'stat' : 'ev'}, {'No':'2', 'name':'Evasion 2', 'active':False, 'boost':10, 'stat' : 'ev'}, {'No':'3', 'name':'Evasion 3', 'active':False, 'boost':50, 'stat' : 'ev'},
                              ]
        elif (a == 'e'):
            units = False
def active():
    loadSet()
    dostuff = True
    while(dostuff == True):
        print('\n1: Player stats.')
        print('2: Set equipment.')
        print('3: Fight')
        a = input('Action: ')
        if (a == '1'):
            unit()
        elif (a == '2'):
            equipment()
        elif (a == '3'):
            setFoe()
active()
