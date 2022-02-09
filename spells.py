from data import typeSpf
import spells
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
spl = spells



class Spell():
    def __init__(self, spId,name, spltype, spellType, attackType, damage, cost, effectivness, effect):
        self.spId = spId
        self.name = name
        self.spltype =spltype
        self.specialType = SpecialType1.spell
        self.spellType = spellType
        self.attackType = attackType
        self.damage = damage
        self.cost = cost
        self.effectivness = effectivness
        self.active = False
        self.inEffect = 0
        self.unlocked = False
        self.effect = effect
    #def getType():
        #return
    def findTargets(self, p, e):
        count = 1
        for i in e:
            if (i.type == 'playable'):
                if (i.pId != p.pId): 
                    e.remove(i)
            print(count, ') ', i.name)
            count += 1
        
    def getTarget(self, e):
        if (self.attackType == AttackType.single):
            target = input('Cast on:')
            count = 1
            for i in e:
                if (target == str(count)):
                    return i
                count +=1
    def combine(self, wth):
        combinations = [{'spell':spl.Nature_Offence('comb1','Poisonous mushrooms', AttackType.single, 9, 10, 100, 'Grow poisinous mushrooms on the enemy.'), 'components':['1', '2']}
          ]
        for i in combinations:
            if (i['components'][0] == self.spId and i['components'][1] == wth.spId):
                return i['spell']

class Nature(Spell):
    def __init__(self, spId,name, spltype, attackType, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, spltype, SpellType.Nature, attackType, damage, cost, effectivness, effect)

class Nature_Automatic(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.automatic, attackType, damage, cost, effectivness, effect)
        
class Nature_Offence(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.offence, attackType, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == '1'):
            i.aliment['poison'] = True
        elif (self.spId == '2'):
            i.aliment['fungus'] = True
        elif (self.spId == 'comb1'):
            i.aliment['poison'] = True
            i.aliment['fungus'] = True 
        if(self.damage > 0):
            i.health -= self.damage
            print(i.name, 'took', self.damage, 'from', self.name,'!')

class Nature_Enhance(Nature):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.enhance, AttackType.single, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == '3'):
            i.stamina += self.damage
        
class Nature_Support(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.support, attackType, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == '4'):
            i.stamina += self.damage
            if (i.stamina > i.maxStamina):
                i.stamina = i.maxStamina
class Blessing(Spell):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, SpecialType2.support, SpellType.Blessing, AttackType.single, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        print(i)
        if (self.spId == 'f1'):
            i.health += self.damage
            if (i.health > i.maxHealth):
                i.health = i.maxHealth       

class S_Shift(Spell):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, SpecialType2.enhance, SpellType.Shape_shifting, AttackType.single, damage, cost, effectivness, effect)

class Animation(Spell):
    def __init__(self, spId,name, spltype, attackType, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, spltype, SpellType.Nature, attackType, damage, cost, effectivness, effect)

class Illustion(Spell):
    def __init__(self, spId,name, spltype, attackType, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, spltype, SpellType.Nature, attackType, damage, cost, effectivness, effect)

class Curse(Spell):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, SpecialType2.offence, SpellType.Nature, attackType, damage, cost, effectivness, effect)
