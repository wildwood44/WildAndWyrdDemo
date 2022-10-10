import os
import random
import pickle
import sqlite3
from data import createDatabase
import playableChars
import enemyUnits
import inventory
import equipment
import record
import spells
import manuvers
import combat
import ItemClasses
import itemList
from data import game_database
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
ProjectileType = typeSpf.ProjectileType

# connecting to database
#connection = sqlite3.connect("waw.db")
# cursor
#crsr = connection.cursor()

#Set playable characters
alder = playableChars.Alder()
florace = playableChars.Florence()
item = ItemClasses
spl = spells
mnv = manuvers
inv = inventory.Inventory()
eqp = equipment.Equipment()
com = combat
#db = game_database.DB(connection, crsr)

class Combatent(playableChars.Playable, enemyUnits.Enemy):
    def __init__(self):
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = CombatStatus.Normal
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}  

#Enemy Units
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
items = itemList
#Universal Specials
manuvers = [mnv.Manuver_Enhance('1','Advence', 0,10,100, 'Move in range.'),
           mnv.Manuver_Enhance('2','Retreat', 0,10,100, 'Move out of range.')
           ]
spells = [spl.Nature_Offence('1','Poison nettles', AttackType.single, 1, 10, 100, 'Poisons an opponent'),
          spl.Nature_Offence('2','Grow mushrooms', AttackType.single, 0, 10, 100, 'Grow mushrooms on your enemy to hinder them.'),
          spl.Nature_Enhance('3','Grow mushrooms', 9, 0, 100, "Grow edable mushrooms for an ally to restore stamina."),
          spl.Nature_Support('4','Grow mushrooms', AttackType.single, 9, 0, 100, 'Grow edable mushrooms for the caster to restore stamina.')
          ]
combinations = [{'spell':spl.Nature_Offence('comb1','Poisonous mushrooms', AttackType.single, 9, 10, 100, 'Grow poisinous mushrooms on the enemy.'), 'components':['1', '2']}
          ]

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
    except:
        print('Saved file not found!')
    print ('Data Loaded!')

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
            count = eqp.getHat(p,inv,equipable)
            eqp.head(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '2'):
            count = eqp.getShirt(p,inv,equipable)
            eqp.body(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '3'):
            count = eqp.getTrousers(p,inv,equipable)
            eqp.legs(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '4'):
            count = eqp.getPrimeWeapon(p,inv,equipable)
            eqp.primeWeapon(p, eqp.setEquipment(count,equipable), inv)
            equipable.clear()
        elif (i == '5'):
            count = eqp.getSecondWeapon(p,inv,equipable)
            eqp.secondWeapon(p, eqp.setEquipment(count,equipable), inv)
        elif (i == 'e'):
            equiping = False
        save()

#Open the inventory
def inventory():
    listItems = []
    bag = True
    j = ''
    while(bag == True):
        #View the items in inventory
        print('\nInventory')
        count = 1
        inv.printInventory(j,listItems)
        print('\n1: Appraise')
        print('2: Equip')
        print('e - Exit')
        i = input('Action: ')
        #Appraise items in inventory
        if (i == '1'):
            inv.appraise()
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
        else:
            j = i
            
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
                print(items.weapons)
                print('\nDagger obtained')
                inv.addItem(items.weapons[3], 1)
                print('\nLeif obtained')
                inv.addItem(items.weapons[2], 1)
                print('\nSword obtained')
                inv.addItem(items.weapons[1], 1)
                print('\nSpear obtained')
                inv.addItem(items.weapons[4], 1)
                print('\nAxe obtained')
                inv.addItem(items.weapons[5], 1)
                print('\nClub obtained')
                inv.addItem(items.weapons[6], 1)
                print('\nStaff obtained')
                inv.addItem(items.weapons[7], 1)
                print('\nStaff obtained')
                inv.addItem(items.weapons[8], 1)
            elif (j == '2'):
                print('\nBow obtained')
                inv.addItem(items.weapons[9], 1)
                print('\nCrossbow obtained')
                inv.addItem(items.weapons[10], 1)
                print('\nSling obtained')
                inv.addItem(items.weapons[11], 1)
                print('\nShield obtained')
                inv.addItem(items.weapons[12], 1)
                print('\nWand obtained')
                inv.addItem(items.weapons[13], 1)
                print('\nArrows obtained')
                inv.addItem(items.projec[0], 5)
                print('\nNet obtained')
                inv.addItem(items.projec[1], 1)
                print('\nBolts obtained')
                inv.addItem(items.projec[2], 5)
                print('\nStones obtained')
                inv.addItem(items.projec[3], 5)
            elif (j == '3'):
                print('\nBlackberries obtained')
                inv.addItem(items.food[0], 5)
                print('\nBandage obtained')
                inv.addItem(items.items[0], 5)
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
                enemy[0] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[0] = enemyUnits.Hornet()
            elif (j == '3'):
                enemy[0] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[0] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[0] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[0] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[0] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[0] = enemyUnits.SwordMaster()
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
                enemy[1] = enemyUnits.Null()
            elif (j == '1'):
                enemy[1] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[1] = enemyUnits.Hornet()
            elif (j == '3'):
                enemy[1] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[1] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[1] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[1] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[1] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[1] = enemyUnits.SwordMaster()
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
                enemy[2] = enemyUnits.Null()
            elif (j == '1'):
                enemy[2] = enemyUnits.Cricket()
            elif (j == '2'):
                enemy[2] = enemyUnits.Hornet()
            elif (j == '3'):
                enemy[2] = enemyUnits.Dummy()
            elif (j == '4'):
                enemy[2] = enemyUnits.Wall()
            elif (j == '5'):
                enemy[2] = enemyUnits.Gowl_Rabbit()
            elif (j == '6'):
                enemy[2] = enemyUnits.YoungCrow()
            elif (j == '7'):
                enemy[2] = enemyUnits.ShieldMaster()
            elif (j == '8'):
                enemy[2] = enemyUnits.SwordMaster()
        elif (i == '4'):
            if(enemy[0].enId != null.enId):
                victory = False
                enemy[0].inId = '1'
                enemy[1].inId = '2'
                enemy[2].inId = '3'
                victory = com.Battle(heroes, enemy, inv)
                if (victory == True):
                    print('You won the fight!')
                    save()
                else:
                    print('You lost the fight!')
                setting = False
            else:
                print('Please press "1" and select an enemy to fight.')
        elif (i == 'e'):
            setting = False

#Combat interface
def battle(h, e):
    os.system('clear')
    global alder, florace
    heroes = []
    enemys = []
    shield = 0
    aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
    cStatus = CombatStatus.Normal
    ammo = {'name': '', 'loaded' : False, 'damage' : 0}
    rcd = record.Record()
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
        if (i.weapon2.itemType == Weapon2Type.shield):
            i.shield = i.weapon2['defence']
    while(fighting == True):
        for i in heroes:
            hunger(i)
        #Order combatents by fastest to slowest
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
                        death()
                        return False
                #Win
                elif(winner == True):
                    for j in alder.abilities:
                        j.active = False
                    fighting = False
                    win(enemys)
                    rcd.playRecord()
                    return True
                if (i.type == 'playable' and i.health > 0):
                    #Automatic special
                    automatic = i.special_auto()
                    if(automatic.spId != '0'):
                        i.cStatus = CombatStatus.Specializing
                        if(automatic.specialType == SpecialType1.manuver):       
                            automatic.auto_activate(i, automatic)
                            rcd.recordManuver(i.pId,i.name,i.type,i.cStatus,SpecialType1.manuver,automatic.name)
                        elif(automatic.specialType == SpecialType1.spell):
                            magic(i, h, e, automatic)
                            print('\n',automatic.name,'is active.')
                            rcd.recordMagic(i.pId,i.name,i.type,i.cStatus,SpecialType1.magic,automatic.name)
                    #inEffect(i, enemys)
                    i.cStatus = CombatStatus.Normal
                    while(i.cStatus == CombatStatus.Normal):
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
                                        if (j.cStatus == CombatStatus.Blocking and impact > 0):
                                            j.weapon2['defence'] -= impact
                                        #print(i.pId, i.name, i.type, i.cStatus, j, impact)
                                        rcd.recordAttack(i.pId, i.name, i.type, i.cStatus, j, impact)
                                    k += 1
                        elif (j == '2' or j == 'block' or j == 'Block'):
                            i.cStatus = CombatStatus.Blocking
                            rcd.recordBlock(i.pId,i.name,i.type,i.cStatus)
                        elif (j == '3' or j == 'appraise' or j == 'Appraise'):
                            for j in enemys:
                                print('\n',j.name, 'Health:', j.health,'/',j.maxHealth)
                                print(j.desc)
                        elif (j == '4' or j == 'special' or j == 'Special'):
                            special(i, heroes, enemys, rcd)
                        elif (j == '5' or j == 'item' or j == 'Item'):
                            item(i, enemys, rcd)
                        elif (j == '6' or j == 'flee' or j == 'Flee'):
                            j = input('Are you sure you want to run?(y/n)')
                            if (j == 'y' or j == 'Y' or j == 'yes' or j == 'Yes'):
                                i.cStatus = CombatStatus.Escaping
                                rcd.recordFlee(i.pId, i.name, i.type, i.cStatus)
                                return False
                else:
                    if(i.health > 0):
                        if (i.aliment['poison'] == True):
                            poison = i.maxHealth / 10
                            if (round(poison) < 0):
                                poison = 1
                            i.health -= round(poison)
                            print(i.name, 'took', round(poison), 'damage from poison!')
                            rcd.recordAliment(i.enId, i.name, i.cStatus, i.type, 'poison', round(poison))
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
                            rcd.recordAliment(i.enId, i.name, i.cStatus, i.type, 'caught', 0)
                        elif (i.aliment['stun'] == True):
                            print(i.name, 'was stunned!')
                            i.aliment['stun'] = False
                        else:
                            impact = i.action(i, heroes, rcd)[0]
                            #if (alder.cStatus == CombatStatus.Blocking and impact > 0):
                                #shield -= impact
                for j in reversed(enemys):
                    if (j.cStatus == CombatStatus.Escaping):
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
            alder.cStatus = CombatStatus.Normal
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
            florace.cStatus = CombatStatus.Normal
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
    alder.abilities[0].unlocked = True
    florace.abilities[0].unlocked = True
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
