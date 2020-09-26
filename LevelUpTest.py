#Character Base Stats
class Alder:
    def __init__(self):
        self.pId = '1'
        self.name = 'Alder'
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStamina = 100
        self.stamina = self.maxStamina
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
        self.weapon2 = 'None'
        self.aliment = 'None'
        self.cStatus = 'None'
        self.statBoost = {'health1':False, 'health2':False, 'health3':False, 'stamina1':False, 'stamina2':False, 'stamina3':False, 'attack1':False, 'attack2':False, 'attack3':False,
                          'defence1':False, 'defence2':False, 'defence3':False, 'accuracy1':False, 'accuracy2':False, 'accuracy3':False, 'speed1':False, 'speed2':False, 'speed3':False,
                          'evasion1':False, 'evasion2':False, 'evasion3':False
                          }
        self.special = [{'spId':'1','name':'Steps of heroes', 'cost':10, 'active':False, 'inEffect':0,'unlocked':True, 'effect':'Increases Evasion for five turns.'},
                        {'spId':'2','name':'Master archer', 'cost':10, 'active':False, 'inEffect':0, 'unlocked':False, 'effect':'Grants a critical for the next arrow fired within the next four turns.'}
                        ]
    property
    def attack(self):
        attack = self.baseAttack
        if (self.weapon1['wpId'] != '0'):
            attack += self.weapon1['attack']
        else:
            attack += 0
        if (self.statBoost['attack1'] == True):
            attack += 5
        if (self.statBoost['attack2'] == True):
            attack += 10
        if (self.statBoost['attack3'] == True):
            attack += 50
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
        if (self.statBoost['defence1'] == True):
            defence += 5
        if (self.statBoost['defence2'] == True):
            defence += 10
        if (self.statBoost['defence3'] == True):
            defence += 50
        return defence
    property
    def accuracy(self):
        accuracy = self.baseAccuracy
        if (self.statBoost['accuracy1'] == True):
            accuracy += 5
        if (self.statBoost['accuracy2'] == True):
            accuracy += 10
        if (self.statBoost['accuracy3'] == True):
            accuracy += 50
        return accuracy
    property
    def speed(self):
        speed = self.baseSpeed
        if (self.statBoost['speed1'] == True):
            speed += 5
        if (self.statBoost['speed2'] == True):
            speed += 10
        if (self.statBoost['speed3'] == True):
            speed += 50
        return speed
    property
    def evasion(self):
        evasion = self.baseEvasion
        if (self.special[0]['active'] == True):
            evasion *= 2 
        return evasion
    def stats(self):
        print('\nName: ', self.name, '- Lvl: ', self.cLvl, 'Exp: ', self.cExp,
              '\nHealth: ', self.health, '/', self.maxHealth, '| Stamina: ', self.stamina, '/', self.maxStamina,
              '\nAttack: ', self.attack(), '(', self.baseAttack,'+',self.weapon1['attack'], ')',
              '| Defence: ', self.defence(), '(', self.baseDefence,'+',self.head['defence'] + self.body['defence'] + self.legs['defence'], ')',
              '| \nAccuracy: ', self.accuracy(), '(', self.baseAccuracy,'+', 0, ')',
              '| Speed: ', self.speed(), '(', self.baseSpeed,'+', 0, ')',
              '| Evasion: ', self.evasion(), '(', self.baseEvasion,'+', 0, ')',
              '\nHead:', self.head['name'], '\nBody:', self.body['name'], '\nLegs:', self.legs['name'],
              '\nMain Weapon: ', self.weapon1['name'], '\nSecondary Weapon: ', self.weapon2,'\n'
              '\nSkill Points', self.skillPoints,'\n'
              )

#Items lists
weapons = [{'wpId' : '0', 'name' : 'None', 'type' : 'weapon', 'description' : '',
            'attack' : 0, 'weight' : 0, 'count' : 0},
           {'wpId' : '1', 'name' : 'Lief', 'type' : 'weapon', 'description' : 'Legendary sword of the Scion.',
            'attack' : 500, 'weight' : 5, 'count' : 0},
           {'wpId' : '2', 'name' : 'Hunting Knife', 'type' : 'weapon', 'description' : 'A knife used to hunt insects.',
            'attack' : 5, 'weight' : 1, 'count' : 0}
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

def gainExperience():
    experience = input('Increase experience by how mush?: ')
    e = int(experience)
    #if isinstance(experience, int):
    alder.cExp += e
    print(e)

def levelUP():
    print(alder.cNext, ' ', alder.cExp)
    if(alder.cExp >= alder.cNext):
        while(alder.cExp >= alder.cNext):
            alder.cLvl += 1
            print('Alder leveled up!')
            alder.cNext = round(alder.cNext*1.65)
            print(alder.cNext)

#Set Class
alder = Alder()

def skillTree(p):
    print('\nSkills')
    print('Skill Points: ', alder.skillPoints)
    print('1: Stat Boosts')
    print('2: Special Skills')
    skill = input('Skill Type: ')
    if (skill == '1'):
        print('\nStat Boosts')
        count = 1
        if (p.statBoost['health1'] == False):   
            print(count,': Health + 10')
            count += 1
        elif (p.statBoost['health2'] == False):   
            print(count,': Health + 50')
            count += 1
        elif (p.statBoost['health3'] == False):   
            print(count,': Health + 300')
            count += 1
        if (p.statBoost['stamina1'] == False):   
            print(count,': Stamina + 10')
            count += 1
        elif (p.statBoost['stamina2'] == False):   
            print(count,': Stamina + 50')
            count += 1
        elif (p.statBoost['stamina3'] == False):   
            print(count,': Stamina + 300')
            count += 1
        if (p.statBoost['attack1'] == False):
            print(count,': Attack + 5')
            count += 1
        elif (p.statBoost['attack2'] == False):   
            print(count,': Attack + 10')
            count += 1
        elif (p.statBoost['attack3'] == False):   
            print(count,': Attack + 50')
            count += 1
        if (p.statBoost['defence1'] == False):   
            print(count,': Defence + 5')
            count += 1
        elif (p.statBoost['defence2'] == False):   
            print(count,': Defence + 10')
            count += 1
        elif (p.statBoost['defence3'] == False):   
            print(count,': Defence + 50')
            count += 1
        if (p.statBoost['accuracy1'] == False):   
            print(count,': Accuracy + 5')
            count += 1
        elif (p.statBoost['accuracy2'] == False):   
            print(count,': Accuracy + 10')
            count += 1
        elif (p.statBoost['accuracy3'] == False):   
            print(count,': Accuracy + 50')
            count += 1
        if (p.statBoost['speed1'] == False):   
            print(count,': Speed + 5')
            count += 1
        elif (p.statBoost['speed2'] == False):   
            print(count,': Speed + 10')
            count += 1
        elif (p.statBoost['speed3'] == False):   
            print(count,': Speed + 50')
            count += 1
        if (p.statBoost['evasion1'] == False):   
            print(count,': evasion + 5')
            count += 1
        elif (p.statBoost['evasion2'] == False):   
            print(count,': evasion + 10')
            count += 1
        elif (p.statBoost['evasion3'] == False):   
            print(count,': evasion + 50')
            count += 1
    elif (skill == '2'):
        print('\nSpecial Skills')
    
def active():
    dostuff = True
    while(dostuff == True):
        print('\n1: Player stats.')
        print('2: Increase experience.')
        print('3: Unlock Skills.')
        action = input('Action: ')
        if (action == '1'):
            alder.stats()
        elif (action == '2'):
            gainExperience()
            levelUP()
        elif (action == '3'):
            skillTree(alder)
active()
