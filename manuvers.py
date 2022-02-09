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

class Manuver():
    def __init__(self, spId,name, spltype, attackType, damage, cost, effectivness, effect):
        self.spId = spId
        self.name = name
        self.spltype = spltype
        self.specialType = SpecialType1.manuver
        self.attackType = attackType
        self.damage = damage
        self.cost = cost
        self.effectivness = effectivness
        self.active = False
        self.unlocked = False
        self.effect = effect
    def getTarget(self, e):
        if (self.attackType == AttackType.single):
            target = input('Use on:')
            count = 1
            for i in e:
                if (target == str(count)):
                    return i              
                count +=1
class Manuver_Automatic(Manuver):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Manuver.__init__(self, spId,name, SpecialType2.automatic, attackType, damage, cost, effectivness, effect)
    def auto_activate(self,p, m):
        if (m.spId == 'a1'): 
            if (p.health < p.maxHealth/5):
                p.stamina -= m.cost
                m.active = True
                print('\n',m.name,'is active.')
    def auto_return(self, m, v):
        if (m.spId == 'a1'):
            if (m.active == True):
                v *= 2
                return v
class Manuver_Offence(Manuver):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Manuver.__init__(self, spId,name, SpecialType2.offence, attackType, damage, cost, effectivness, effect)
class Manuver_Enhance(Manuver):
    def __init__(self, spId,name, damage, cost, effectivness, effect):
        Manuver.__init__(self, spId,name, SpecialType2.enhance, AttackType.single, damage, cost, effectivness, effect)
    def use(p, e, m):
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
class Manuver_Support(Manuver):
    def __init__(self, spId,name, attackType, damage, cost, effectivness, effect):
        Manuver.__init__(self, spId,name, SpecialType2.support, attackType, damage, cost, effectivness, effect)
