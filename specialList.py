import sqlite3
import spells
import manuvers
from data import game_database
from data import typeSpf
#item = ItemClasses
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

spl = spells
mnv = manuvers

# connecting to database
connection = sqlite3.connect("waw.db")
# cursor
crsr = connection.cursor()
db = game_database.DB(connection, crsr)

#manuvers = [mnv.Manuver_Enhance('1','Advence', 0,10,100, 'Move in range.'),
#           mnv.Manuver_Enhance('2','Retreat', 0,10,100, 'Move out of range.')
#           ]
manuvers = []
for i in db.GetManuverByType(crsr, SpecialType2.enhance):
    manuvers.append(mnv.Manuver_Enhance(*(i)))
#spells = [spl.Nature_Offence('1','Poison nettles', AttackType.single, 1, 10, 100, 'Poisons an opponent'),
#          spl.Nature_Offence('2','Grow mushrooms', AttackType.single, 0, 10, 100, 'Grow mushrooms on your enemy to hinder them.'),
#          spl.Nature_Enhance('3','Grow mushrooms', 9, 0, 100, "Grow edable mushrooms for an ally to restore stamina."),
#          spl.Nature_Support('4','Grow mushrooms', AttackType.single, 9, 0, 100, 'Grow edable mushrooms for the caster to restore stamina.')
#          ]
spells = []
#print(db.GetSpellType(crsr, SpellType.Nature))
for i in db.GetSpellType(crsr, SpellType.Nature, SpecialType2.offence):
    spells.append(spl.Nature_Offence(*(i)))
for i in db.GetSpellType(crsr, SpellType.Nature, SpecialType2.enhance):
    spells.append(spl.Nature_Enhance(*(i)))
for i in db.GetSpellType(crsr, SpellType.Nature, SpecialType2.support):
    spells.append(spl.Nature_Support(*(i)))
    #if i in db.GetCombinations(crsr):
    #    spells.append(spl.Nature_Offence(*(i)))
    #for i in j:
   #     spells.append(spl.Nature_Enhance(*(i)))
   # for i in j:
    #    spells.append(spl.Nature_Support(*(i)))
for i in db.GetSpellType(crsr, SpellType.Blessing, None):
    spells.append(spl.Blessing(*(i)))
    
combinations = []
#[{'spell':spl.Nature_Offence('comb1','Poisonous mushrooms', AttackType.single, 9, 10, 100, 'Grow poisinous mushrooms on the enemy.'), 'components':['1', '2']}
        #]
for i in db.GetCombinations(crsr):
    Li=list(i)
    comp = (Li.pop(7), Li.pop(7))
    i = tuple(Li)
    combinations.append((spl.Nature_Offence(*(i)),comp))
