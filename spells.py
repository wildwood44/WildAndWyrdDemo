from data import typeSpf
import spells
import specialList
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
                if (i.pId == p.pId):
                    e.remove(i)
                    continue
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
    def combine(self, spell1, spell2):
        combinations = specialList.combinations
        for i in combinations:
            if (i[1][0] == spell1 and i[1][1] == spell2):
                return i[0].spId

class Nature(Spell):
    def __init__(self, spId,name, spltype, attackType, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, spltype, SpellType.Nature, attackType, damage, cost, effectivness, effect)

class Nature_Automatic(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.automatic, attackType, damage, cost, effectivness, effect)
        
class Nature_Offence(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.offence, attackType, damage, cost, effectivness, effect)
        if (type(self.attackType) == str):
            if (self.attackType == 'AttackType.single'):
                self.attackType = AttackType['single']
    property
    def cast(self, i):
        if (self.spId == 101):
            i.aliment['poison'] = True
        elif (self.spId == 102):
            i.aliment['fungus'] = True
        elif (self.spId == 201):
            i.aliment['poison'] = True
            i.aliment['fungus'] = True 
        else:
            raise Exception('Spell not recognised')
        if(self.damage > 0):
            i.health -= self.damage
            print(i.name, 'took', self.damage, 'from', self.name,'!')

class Nature_Enhance(Nature):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.enhance, AttackType.single, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == 104):
            i.stamina += self.damage
        else:
            raise Exception('Spell not recognised')
        
class Nature_Support(Nature):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Nature.__init__(self, spId,name, SpecialType2.support, attackType, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == 103):
            i.stamina += self.damage
            if (i.stamina > i.maxStamina):
                i.stamina = i.maxStamina
        else:
            raise Exception('Spell not recognised')
class Blessing(Spell):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Spell.__init__(self, spId,name, SpecialType2.support, SpellType.Blessing, AttackType.single, damage, cost, effectivness, effect)
    property
    def cast(self, i):
        if (self.spId == 105):
            i.health += self.damage
            if (i.health > i.maxHealth):
                i.health = i.maxHealth
        else:
            raise Exception('Spell not recognised')

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
