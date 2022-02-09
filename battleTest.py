import os
import random
import pickle
import playableChars
import enemyUnits
import ItemClasses
import inventory
import equipment
import record
import spells
import manuvers
import combat
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


#Set playable characters
alder = playableChars.Alder()
florace = playableChars.Florace()
item = ItemClasses
spl = spells
mnv = manuvers
inv = inventory.Inventory()
eqp = equipment.Equipment()
#com = combat.Combat()

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
weapons = [item.Sword('0','None',0,0,''),
           item.Sword('1','Lief',500,5,'Legendary sword of the Scion.'),
           item.Dagger('2','Hunting Knife',5,1,'A knife used to hunt insects.'),
           item.Sword('3','Relic Sword', 10,3, '',),
           item.Spear('4','Relic Spear',8,3, ''),
           item.Axe('5','Relic Axe', 12,4, ''),
           item.Mace('6','Old Club', 10,4,''),
           item.Staff('7','Crooked Stick', 3,2, ['0'],[''],''),
           item.Bow('1','Training Bow', 20,2, 'A large bow made for practise.'),
           item.Crossbow('1','Training Crossbow', 20,2, ''),
           item.Sling('1','Grass Sling', 20,2, 'A sling made from grass; not very practical'),
           item.Shield('1','Wooden Shield', 20,4,'A basic round wooden shield.'),
           item.Wand('1','Poison wand', 1, '1', 'Poison Nettle', 'A wand containing a weak poison'),
           item.Staff('8', 'Mushroom staff',  3,2, ['2', '3', '4'],['Grow mushrooms','Grow mushrooms','Grow mushrooms'],'')
           ]

armours = [item.Hat('1','None',0,0,''),
           item.Shirt('1','Old Tunic', 1,1,'An old shirt with holes in it.'),
           item.Shirt('2', 'Travelling Cloak', 10,10,'A too large black cloak. Good for keeping ou of sight but heavy.'),
           item.Trousers('1','Worn Trousers', 1,1,'An old pair of trousers long past their prime')
          ]
food = [item.Food('1','Blackberry', 1,3),
        item.Food('2','Dried Fruit', 1,5),
        item.Food('3','Hazelnut', 1,3),
        item.Food('4','Raw Bug Meat', 3,10)
        ]
projec = [item.Arrow('1','Primitive Arrow', 10,1,'Arrows made from stone heads and twigs.'),
          item.Toss('2','Rope Net', 0,1, 'A rope net to catch your enemies.'),
          item.Bolt('3','Wooden Bolt', 10,1,''),
          item.Stone('4','Softstone', 10,1,'')
          ]
items = [item.Healing('1', 'Bandage', 10,1, 'A cloth bandage to treat wounds')
         ]
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
            count = 0
            for i in inv.itemList:
                if(i['item'].itemType == ArmourType.hat):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.head.defence)
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.head(p, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '2'):
            count = 0
            for i in inv.itemList:
                if(i['item'].itemType == ArmourType.shirt):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.body.defence)
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.body(p, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '3'):
            count = 0
            for i in inv.itemList:
                if(i['item'].itemType == ArmourType.trousers):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['item'].name, '- Defence: +', i['item'].defence - alder.legs.defence)
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.legs(p, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '4'):
            count = 0
            for i in inv.itemList:
                if(i['item'].itemType == Weapon1Type.sword or i['item'].itemType == Weapon1Type.dagger or i['item'].itemType == Weapon1Type.spear or
                   i['item'].itemType == Weapon1Type.axe or i['item'].itemType == Weapon1Type.mace or i['item'].itemType == Weapon1Type.staff):
                    count +=1
                    equipable.append(i)
                    print(count, ': ', i['item'].name, '- Attack: +', i['item'].attack - p.weapon1.attack)
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.primeWeapon(p, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
        elif (i == '5'):
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
                        print(count, ': ', i['item'].name, '- Spell: ', i['item'].spells)
                        for j in p.spells:
                            if (j['spId'] == i.wpId):
                                j['unlocked'] = True
            if(count != 0):
                count = 1
                eq = input('Equip item: ')
                for i in equipable:
                    if (eq == str(count)):
                        eqp.secondWeapon(p, i, inv)
                    count +=1
            else:
                print('You have nothing to equip.')
            equipable.clear()
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
                print('\nDagger obtained')
                inv.addItem(weapons[2], 1)
                print('\nLeif obtained')
                inv.addItem(weapons[1], 1)
                print('\nSword obtained')
                inv.addItem(weapons[3], 1)
                print('\nSpear obtained')
                inv.addItem(weapons[4], 1)
                print('\nAxe obtained')
                inv.addItem(weapons[5], 1)
                print('\nClub obtained')
                inv.addItem(weapons[6], 1)
                print('\nStaff obtained')
                inv.addItem(weapons[7], 1)
                print('\nStaff obtained')
                inv.addItem(weapons[13], 1)
            elif (j == '2'):
                print('\nBow obtained')
                inv.addItem(weapons[8], 1)
                print('\nCrossbow obtained')
                inv.addItem(weapons[9], 1)
                print('\nSling obtained')
                inv.addItem(weapons[10], 1)
                print('\nShield obtained')
                inv.addItem(weapons[11], 1)
                print('\nWand obtained')
                inv.addItem(weapons[12], 1)
                print('\nArrows obtained')
                inv.addItem(projec[0], 5)
                print('\nNet obtained')
                inv.addItem(projec[1], 1)
                print('\nBolts obtained')
                inv.addItem(projec[2], 5)
                print('\nStones obtained')
                inv.addItem(projec[3], 5)
            elif (j == '3'):
                print('\nBlackberries obtained')
                inv.addItem(food[0], 5)
                print('\nBandage obtained')
                inv.addItem(items[0], 5)
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
            print(i.name,' dropped ', i.drop[0]['item'].name, ' x', i.drop[0]['quantity'])
            inv.addItem(i.drop[0]['item'], i.drop[0]['quantity'])
    save()

def death():
    for i in alder.abilities:
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


def enemyFlee(e):
    print(e.name, ' fled!')

#Attack Enemy
def attack(p, e):
    numOfAtk = 1
    impact = 0
    if (p.weapon1.itemType == Weapon1Type.dagger):
        numOfAtk += 1
    target = p.accuracy() + 100 - e.evasion()
    hit = random.randrange(0,100)
    critical = random.randrange(0,100)
    p.stamina -= 5
    while(numOfAtk > 0):
        if (p.ammo['loaded'] == True):
            p.cStatus = CombatStatus.RAttacking
            if (hit < target):
                impact = random.randrange(p.attackRanged() - 3, p.attackRanged() + 3)
                impact += p.ammo['damage']
                if (critical >= 90):
                    impact += 10
                impact = round(impact * (100/(100 + e.defence())))
                im = impact
                if (e.cStatus == CombatStatus.Blocking):
                    impact = round(impact/10)
                    if (impact <= 0):
                        impact = 1
                    im = impact
                    if (e.weapon2.itemType == Weapon2Type.shield):
                        if (e.weapon2.defence > 0):
                            print('Attack blocked!')
                            impact -= e.weapon2.defence
                            if (impact < 0):
                                impact = 0
                print('\n',p.name,' fired a', p.ammo['name'], '!')
                if(critical >= 90):
                    print('Critical Hit!')
                    if (p.weapon2.itemType == Weapon2Type.sling):
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
            p.cStatus = CombatStatus.Attacking
            if ((e.aliment['outRange'] != True or (e.aliment['outRange'] == True and p.weapon1['type'] == Weapon1Type.spear)) and
                (p.aliment['outRange'] != True or (p.aliment['outRange'] == True and p.weapon1['type'] == Weapon1Type.spear)) and
                (e.aliment['outRange'] != True and p.aliment['outRange'] != True)):
                print(p.aliment['outRange'])
                if (hit < target):
                    impact = random.randrange(p.attack() - 5, p.attack() + 5)
                    if(p.weapon1.wpId != '0'):
                        if (critical >= 90):
                            impact += 10
                        impact = round(impact * (100/(100 + e.defence())))
                        im = impact
                        if (impact <= 0):
                            impact = 1
                        if (e.cStatus == CombatStatus.Blocking):
                            impact = round(impact/10)
                            if (impact <= 0):
                                impact = 1
                            im = impact
                            if (e.weapon2.defence > 0):
                                if (p.weapon1.itemType == Weapon1Type.axe):
                                    print('Shield repealed!')
                                    e.cStatus = CombatStatus.Normal
                                else:
                                    print('Attack blocked!')
                                    impact -= e.weapon2.defence
                                if (impact < 0):
                                    impact = 0
                        e.health -= impact
                        if (p.cStatus == CombatStatus.Countered):
                            print('\n',p.name,' countered!')
                        else:
                            print('\n',p.name,' attacked!')
                        if(critical >= 90):
                            print('Critical Hit!')
                            if (p.weapon1.itemType == Weapon1Type.mace):
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
    for i in alder.abilities:
        if(i.active == True):
            i.inEffect -= 1
            if (i.inEffect <= 0):
                i.active = False
                print(alder.name,"'s ", i['name'], ' has worn off.')
    for i in p.manver:
        for en in e:
            if (i.spId == '1' and (p.aliment['outRange'] == 'True' or en.aliment['outRange'] == 'True')):
                advencable = False
                if (en.aliment['outRange'] == 'False'):
                    advancable = False
                else:
                    advancable = True
                if (advancable == True):
                    j = i + 1
                    i.active = True
                    j.active = False
                    print(i, j)
            elif (i.spId == '2' and (p.aliment['outRange'] == 'False')):
                j = i - 1
                i.active = True
                j.active = False


def magic(p, t, e, spell):
    hit = random.randrange(0,100)
    damage = spell.damage
    if (p.weapon1.itemType == Weapon1Type.staff):
        boost = damage / 20
        if (boost < 1):
            boost = 1
        damage += round(boost)
    count = 1
    if (spell.spltype == SpecialType2.offence):
        spell.findTargets(p, e)
    elif (spell.spltype == SpecialType2.support):
        spell.findTargets(p, t)
    if (hit < spell.effectivness):
        if (spell.spltype == SpecialType2.offence):
            spell.cast(spell.getTarget(e))
        if (spell.spltype == SpecialType2.support):
            spell.cast(spell.getTarget(t))
        if (spell.spltype == SpecialType2.enhance):
            spell.cast(p)
    else:
        print('The spell missed!')
        
def manuver(p, e, m):
    if (m.specialType == SpecialType1.manuver):
        if (m.spId == '1'):
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
        if (m.spId == '2'):
            if (p.aliment['outRange'] == False):
                p.aliment['outRange'] = True
                print(p.name,'retreated to the rear!')
            else:
                print(p.name,'is too far away!')


def special(p, h, e, r):
    print('\nSpecial Ability')
    if(p.aliment['outRange'] == True):
        print(' 1 Position) Advance - 10 Stamina')
    else:
        print(' 1 Position) Retreat - 10 Stamina')
    offensive = p.special_off()
    support = p.special_sup()
    enhance = p.special_enc()
    print(' 2 Offensive) ',offensive.name, ' - ', offensive.effect, ' - ', offensive.cost, ' stamina\n',
          '3 Support) ',support.name, ' - ', support.effect, ' - ', support.cost, ' stamina\n',
          '4 Enhance) ',enhance.name, ' - ', enhance.effect, ' - ', enhance.cost, ' stamina')
    sp = input('Use: ')
    if (sp == "1" or sp == "advance" or sp == "retreat"):
        p.cStatus = CombatStatus.Specializing
        if(p.aliment['outRange'] == True):
            p.stamina -= manuvers[0].cost
            manuver(p,e,manuvers[0])
            r.recordManuver(p.pId,p.name,p.type,p.cStatus, SpecialType1.manuver, manuvers[0].name)
        else:
            p.stamina -= manuvers[1].cost
            manuver(p,e,manuvers[1])
            r.recordManuver(p.pId, p.name, p.type, p.cStatus, SpecialType1.manuver, manuvers[1].name)
    elif ((sp == "2" or sp == "offence" or sp == "offensive") and offensive.spId != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= offensive.cost
        if(offensive.specialType == SpecialType1.manuver):
            manuver(p,e,offensive)
            r.recordManuver(p.pId, p.name, p.type, p.cStatus, offensive.specialType, offensive.name)
        elif(offensive.specialType == SpecialType1.spell):
            print('\n', p.name, ' uses ', offensive.name,'.')
            magic(p, h, e, offensive)
            r.recordMagic(p.pId, p.name, p.type, p.cStatus, offensive.specialType, offensive.name)
    elif ((sp == "3" or sp == "support") and support.spId != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= support.cost
        if(support.specialType == SpecialType1.manuver):
            manuver(p,e,support)
            r.recordManuver(p.pId, p.name, p.type, p.cStatus, support.specialType, support.name)
        elif(support.specialType == SpecialType1.spell):
            print('\n', p.name, ' uses ', support.name,'.')
            magic(p, h, e, support)
            r.recordMagic(p.pId, p.name, p.type, p.cStatus, support.specialType, support.name)
    if ((sp == "4" or sp == "enhance") and enhance.spId != '0'):
        p.cStatus = CombatStatus.Specializing
        p.stamina -= enhance.cost
        if(enhance.specialType == SpecialType1.manuver):
            manuver(p,e,enhance)
            r.recordManuver(p.pId, p.name, p.type, p.cStatus, enhance.specialType, enhance.name)
        elif(enhance.specialType == SpecialType1.spell):
            print('\n', p.name, ' uses ', enhance.name,'.')
            magic(p, h, e, enhance)
            r.recordMagic(p.pId, p.name, p.type, p.cStatus, enhance.specialType, enhance.name)

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
            for i in inv.itemList:
                if(i['item'].itemType == ItemType.healing):
                    print(count, ': ', i['item'].name, ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'food' or y == 'Food' or
            y == 'consumables' or y == 'Consumables'):
            print('Food')
            for i in inv.itemList:
                if(i['item'].itemType == ItemType.food):
                    print(count, ': ', i['item'].name, ' x', i['count'])
                    use.append(i)
                    count += 1
        if (y == '' or y == 'projectiles' or y == 'Projectiles'):
            print('Projectiles')
            for i in inv.itemList:
                if(i['item'].itemType == ItemType.projectile or i['item'].itemType == ItemType.toss):
                    print(count, ': ', i['item'].name, ' x', i['count'])
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
                    if (i['item'].itemType == ItemType.healing):
                        p.health += i['item'].recovers
                        print(p.name, ' recoved ', i['item'].recovers, ' health')
                        if (p.health > p.maxHealth):
                            p.health = p.maxHealth
                        p.cStatus = CombatStatus.Using
                        using = False
                    elif (i['item'].itemType == ItemType.food):
                        p.stamina += i['item'].recovers
                        print(p.name, ' recoved ', i['item'].recovers, ' stamina')
                        if (p.stamina > p.maxStamina):
                            p.stamina = p.maxStamina
                        p.cStatus = CombatStatus.Using
                        using = False
                    elif (i['item'].itemType == ItemType.projectile):
                        print(u, count)
                        if (i['item'].weapon == Weapon2Type.bow):
                            if(p.weapon2.itemType == Weapon2Type.bow):
                                print('\nArrow loaded!')
                                p.ammo['name'] = i['item'].name
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['item'].damage
                                alder.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Bow required!')
                                using = False
                        elif (i['item'].weapon == Weapon2Type.crossbow):
                            if(p.weapon2.itemType == Weapon2Type.crossbow):
                                print('\nBolt loaded!')
                                p.ammo['name'] = i['item'].name
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['item'].damage
                                p.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Crossbow required!')
                                using = False
                        elif (i['item'].weapon == Weapon2Type.sling):
                            if(p.weapon2.itemType == Weapon2Type.sling):
                                print('\nStone loaded!')
                                p.ammo['name'] = i['item'].name
                                p.ammo['loaded'] = True
                                p.ammo['damage'] = i['item'].damage
                                p.cStatus = CombatStatus.Using
                                using = False
                            else:
                                print('Sling required!')
                                using = False
                    elif (i['item'].itemType == ItemType.toss):
                        count = 1
                        for j in e:
                            print(count, ': ', j.name)
                            count += 1
                        count = 1
                        target = input('Throw at: ')
                        for j in e:
                            if (target == str(count)):
                                print('\n',p.name,'threw ', i['item'].name)
                                j.aliment['caught'] = True 
                                p.cStatus = CombatStatus.Using
                                using = False
                            count += 1
                    i['count'] -= 1
                    if(i['count'] <= 0):
                        inv.itemList.remove(i)
                    r.recordItem(p.pId, i['item'].itemId, p.name, i['item'].name, i['item'].itemType,p.cStatus)
                count +=1
            if u == 'e':
                using = False
            use.clear()
#Combat order
def fightOrder(e):
    return e.speed()

#Combat interface
def battle(h, e):
    os.system('clear')
    global alder, florace
    heroes = []
    enemys = []
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
