import os
import random
import ItemClasses
import playableChars
import enemyUnits
import inventory
import equipment
import record
import spells
import manuvers
import stats
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
#inv = inventory.Inventory()
eqp = equipment.Equipment()
stat = stats.Statistics()

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

def fightOrder(e):
    return e.speed()

class Combatent(playableChars.Playable, enemyUnits.Enemy):
    def __init__(self):
        self.shield = 0
        self.aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False}
        self.cStatus = CombatStatus.Normal
        self.ammo = {'name': '', 'loaded' : False, 'damage' : 0}

class Combat():
    def __init__(self):   
        self.heroes = []
        self.enemys = []
        self.combatants = self.heroes + self.enemys
        self.winner = False
        self.count = 1
    property
    def setHeroes(self, i):
        if (i.active == True):
            self.heroes.append(i)
    property
    def setEnemies(self, i):
        if i.enId != '0':
            self.enemys.append(i)
        
    def win(self, p, e, inv):
        ex = 0
        rewards = []
        count = 0
        print('\n')
        for i in e:
            ex += i.Exp
            count += 1
        for i in p:            
            if (i.active == True):
                i.cExp += ex
                print(i.name, ' gained ', ex, ' experience.')
                stat.levelUP(i)
        #if (florace.active == True):
        #    florace.cExp += ex
        #    print('Florence gained ', ex, ' experience.')
        #    stat.levelUP(florace)
        for i in e:
            if (len(i.drop) > 0):
                print(i.name,' dropped ', i.drop[0]['item'].name, ' x', i.drop[0]['quantity'])
                inv.addItem(i.drop[0]['item'], i.drop[0]['quantity'])
        #save()

    def death(self, p):
        #for i in alder.abilities:
            #i['active'] = False
            #i['inEffect'] = 0
        for i in p:
            i.health = i.maxHealth
            i.stamina = i.maxStamina
        #alder.health = alder.maxHealth
        #alder.stamina = alder.maxHealth
        #florace.health = florace.maxHealth
        #florace.stamina = florace.maxHealth
        print('\nAlder was slain.')
        i = input()
        return p

    def hunger(self, p):
        if(p.stamina <= 0):
            p.health -= 1
            print(p.name,'needs to eat!')
        if(p.stamina < 0):
            p.stamina = 0


    def enemyFlee(self, e):
        print(e.name, ' fled!')
    
    #Attack Enemy
    def attack(self, p, e):
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
    def inEffect(self, p, e):
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
                elif (i.spId == '2' and (p.aliment['outRange'] == 'False')):
                    j = i - 1
                    i.active = True
                    j.active = False


    def magic(self, p, t, e, spell):
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
            
    def manuver(self, p, e, m):
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


    def special(self, p, h, e, r):
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
                self.manuver(p,e,manuvers[0])
                r.recordManuver(p.pId,p.name,p.type,p.cStatus, SpecialType1.manuver, manuvers[0].name)
            else:
                p.stamina -= manuvers[1].cost
                self.manuver(p,e,manuvers[1])
                r.recordManuver(p.pId, p.name, p.type, p.cStatus, SpecialType1.manuver, manuvers[1].name)
        elif ((sp == "2" or sp == "offence" or sp == "offensive") and offensive.spId != '0'):
            try:
                if(offensive.specialType == SpecialType1.manuver):
                    self.manuver(p,e,offensive)
                    r.recordManuver(p.pId, p.name, p.type, p.cStatus, offensive.specialType, offensive.name)
                elif(offensive.specialType == SpecialType1.spell):
                    print('\n', p.name, ' uses ', offensive.name,'.')
                    self.magic(p, h, e, offensive)
                    r.recordMagic(p.pId, p.name, p.type, p.cStatus, offensive.specialType, offensive.name)
                p.cStatus = CombatStatus.Specializing
                p.stamina -= support.cost
            except:
                p.cStatus = CombatStatus.Normal
        elif ((sp == "3" or sp == "support") and support.spId != '0'):
            try:
                if(support.specialType == SpecialType1.manuver):
                    self.manuver(p,e,support)
                    r.recordManuver(p.pId, p.name, p.type, p.cStatus, support.specialType, support.name)
                elif(support.specialType == SpecialType1.spell):
                    print('\n', p.name, ' uses ', support.name,'.')
                    self.magic(p, h, e, support)
                    r.recordMagic(p.pId, p.name, p.type, p.cStatus, support.specialType, support.name)
                p.cStatus = CombatStatus.Specializing
                p.stamina -= support.cost
            except:
                p.cStatus = CombatStatus.Normal
        if ((sp == "4" or sp == "enhance") and enhance.spId != '0'):
            try:
                if(enhance.specialType == SpecialType1.manuver):
                    self.manuver(p,e,enhance)
                    r.recordManuver(p.pId, p.name, p.type, p.cStatus, enhance.specialType, enhance.name)
                elif(enhance.specialType == SpecialType1.spell):
                    print('\n', p.name, ' uses ', enhance.name,'.')
                    self.magic(p, h, e, enhance)
                    r.recordMagic(p.pId, p.name, p.type, p.cStatus, enhance.specialType, enhance.name)
                p.cStatus = CombatStatus.Specializing
                p.stamina -= support.cost
            except:
                p.cStatus = CombatStatus.Normal

    #Use Item
    def item(self, p, e, r, inv):
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
    def fightOrder(self, e):
        return e.speed()

#Combat interface
class Battle():
    def __new__(self, h, e, inv):
        os.system('clear')
        global alder, florace
        com = Combat()
        shield = 0
        aliment = {'stun':False, 'poison':False, 'outRange':False, 'caught':False, 'fungus':False}
        cStatus = CombatStatus.Normal
        ammo = {'name': '', 'loaded' : False, 'damage' : 0}
        rcd = record.Record()
        for i in h:
            com.setHeroes(i)
        for i in e:
            com.setEnemies(i)
        com.combatants = com.heroes + com.enemys
        fighting = True
        winner = False
        count = 1
        for i in com.heroes:
            if (i.weapon2.itemType == Weapon2Type.shield):
                i.shield = i.weapon2['defence']
        while(fighting == True):
            for i in com.heroes:
                com.hunger(i)
            #Order combatents by fastest to slowest
            com.combatants.sort(key=fightOrder, reverse=True)
            for i in com.combatants:
                if (fighting == True):
                    #Win condition
                    if (com.enemys[0].health <= 0):
                        k = 0
                        for remaining in com.enemys:
                            if (remaining.health <= 0):
                                k += 1
                        if (k == len(com.enemys)):
                            winner = True
                    #Death Condition
                    if(i.health <= 0 and i.type == 'playable'):
                        k = 0
                        #record.append({'Who':i.name, 'Status':'defeated'})
                        for remaining in com.heroes:
                            if (remaining.health <= 0):
                                k += 1
                        if (k == len(com.heroes)):
                            com.death(com.heroes)
                            return False
                    #Win
                    elif(winner == True):
                        for j in alder.abilities:
                            j.active = False
                        fighting = False
                        com.win(com.heroes,com.enemys,inv)
                        #rcd.playRecord()
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
                                for j in com.enemys:
                                    if (j.health > 0):
                                        print(k, ': ', j.name)
                                        k += 1
                                target = input('Attack: ')
                                k = 1
                                for j in com.enemys:
                                    if (j.health > 0):
                                        if (target == str(k)):
                                            impact = com.attack(i, j)
                                            if (j.cStatus == CombatStatus.Blocking and impact > 0):
                                                j.weapon2['defence'] -= impact
                                            #print(i.pId, i.name, i.type, i.cStatus, j, impact)
                                            rcd.recordAttack(i.pId, i.name, i.type, i.cStatus, j, impact)
                                        k += 1
                            elif (j == '2' or j == 'block' or j == 'Block'):
                                i.cStatus = CombatStatus.Blocking
                                rcd.recordBlock(i.pId,i.name,i.type,i.cStatus)
                            elif (j == '3' or j == 'appraise' or j == 'Appraise'):
                                for j in com.enemys:
                                    print('\n',j.name, 'Health:', j.health,'/',j.maxHealth)
                                    print(j.desc)
                            elif (j == '4' or j == 'special' or j == 'Special'):
                                com.special(i, com.heroes, com.enemys, rcd)
                            elif (j == '5' or j == 'item' or j == 'Item'):
                                com.item(i, com.enemys, rcd, inv)
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
                                print(i.health)
                                try:
                                    impact = i.action(i, com.heroes, rcd)[0]
                                except:
                                    print()
                    for j in reversed(com.enemys):
                        if (j.cStatus == CombatStatus.Escaping):
                            com.enemys.remove(j)
                            if (len(com.enemys) == 0):
                                fighting = False
                                return True
            count += 1


