import sqlite3
import ItemClasses
from data import game_database
from data import typeSpf
item = ItemClasses
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
connection = sqlite3.connect("waw.db", isolation_level=None)
# cursor
crsr = connection.cursor()
db = game_database.DB(connection, crsr)

weapons = []
for i in db.GetItemByItemType(crsr, Weapon1Type.sword):
    weapons.append(item.Sword(*(i)))
for i in db.GetItemByItemType(crsr, Weapon1Type.dagger):
    weapons.append(item.Dagger(*(i)))
for i in db.GetItemByItemType(crsr, Weapon1Type.spear):
    weapons.append(item.Spear(*(i)))
for i in db.GetItemByItemType(crsr, Weapon1Type.axe):
    weapons.append(item.Axe(*(i)))
for i in db.GetItemByItemType(crsr, Weapon1Type.mace):
    weapons.append(item.Mace(*(i)))
for i in db.GetItemByItemType(crsr, Weapon1Type.staff):
    item_id = i[0]
    weapons.append(item.Staff(*(i), db.GetSpells(crsr, item_id)))
for i in db.GetItemByItemType(crsr, Weapon2Type.bow):
    weapons.append(item.Bow(*(i)))
for i in db.GetItemByItemType(crsr, Weapon2Type.crossbow):
    weapons.append(item.Crossbow(*(i)))
for i in db.GetItemByItemType(crsr, Weapon2Type.sling):
    weapons.append(item.Sling(*(i)))
for i in db.GetItemByItemType(crsr, Weapon2Type.shield):
    weapons.append(item.Shield(*(i)))
for i in db.GetItemByItemType(crsr, Weapon2Type.wand):
    item_id = i[0]
    weapons.append(item.Wand(*(i), db.GetSpells(crsr, item_id)))
armours = []
for i in db.GetItemByItemType(crsr, ArmourType.hat):
    armours.append(item.Hat(*(i)))
for i in db.GetItemByItemType(crsr, ArmourType.shirt):
    armours.append(item.Shirt(*(i)))
for i in db.GetItemByItemType(crsr, ArmourType.trousers):
    armours.append(item.Trousers(*(i)))
food = []
for i in db.GetItemByItemType(crsr, ItemType.food):
    food.append(item.Food(*(i)))
projec = []
for i in db.GetItemByItemType(crsr, ProjectileType.arrow):
    projec.append(item.Arrow(*(i)))
for i in db.GetItemByItemType(crsr, ProjectileType.bolt):
    projec.append(item.Bolt(*(i)))
for i in db.GetItemByItemType(crsr, ProjectileType.stone):
    projec.append(item.Stone(*(i)))
for i in db.GetItemByItemType(crsr, ProjectileType.toss):
    projec.append(item.Toss(*(i)))
items = []
for i in db.GetItemByItemType(crsr, ItemType.healing):
    items.append(item.Healing(*(i)))
ingre = []
for i in db.GetItemByItemType(crsr, ItemType.ingredient):
    ingre.append(item.Ingredient(*(i)))
crsr.close()
connection.close()
