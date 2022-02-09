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

class Record():
    def __init__(self): 
        self.record = []
    def recordNoAct(self, pId, name, pType, status):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status})
    def recordAttack(self, pId, name, pType, status,hit,impact):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status, 'Hit': hit, 'Damage':impact})
    def recordBlock(self, pId, name, pType, status):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status})
    def recordManuver(self, pId, name, pType, status, mnvType, manuver):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status, 'SpecialType':mnvType, 'Manuver':manuver})
    def recordMagic(self, pId, name, pType, status, splType, spell):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status, 'SpecialType':splType, 'Spell':spell})
    def recordItem(self, pId ,iId, name, item, iType, status):
        self.record.append({'UserId':pId,'ItemId': iId, 'Who':name, 'Item':item, 'Type': iType, 'Status':status})
    def recordFlee (self, pId, name, pType, status):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status})
    def recordAliment (self, pId, name, pType, status,aliment,damage):
        self.record.append({'Id': pId, 'Who':name, 'Type': pType, 'Status':status, 'Aliment':aliment, 'Damage':damage})
    def playRecord(self):
        for i in self.record:
            print(i)
