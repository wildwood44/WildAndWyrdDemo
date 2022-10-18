import sqlite3
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

class DB():
    def __init__(self, connection, crsr):
        # connecting to database
        self.connection = sqlite3.connect("waw.db", isolation_level=None)
        # cursor
        self.crsr = connection.cursor()
    def CreateItemDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS items(ITEM_ID bigint PRIMARY KEY NOT NULL, NAME NOT NULL, ITEMTYPE NOT NULL, WEIGHT NOT NULL, RECOVERS NOT NULL, PRIORITY NOT NULL, DESCRIPTION)")
        crsr.execute("""INSERT INTO items VALUES(1001,'Blackberry','ItemType.food',1,5,1,'')""") 
        crsr.execute("""INSERT INTO items VALUES(1002,'Dried Fruit','ItemType.food',1,5,1,'')"""), 
        crsr.execute("""INSERT INTO items VALUES(1003,'Hazelnut','ItemType.food',1,5,1,'')"""), 
        crsr.execute("""INSERT INTO items VALUES(1004,'Mushroom','ItemType.food', 1,5,1,'')"""), 
        crsr.execute("""INSERT INTO items VALUES(1005,'Raw Bug Meat','ItemType.food',3,10,1,'')"""), 
        crsr.execute("""INSERT INTO items VALUES(1006,'Brown Bread','ItemType.food',3,50,1,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1007,'Bandage','ItemType.healing',1,10,2,'A cloth bandage to treat wounds')"""),
        crsr.execute("""INSERT INTO items VALUES(1008,'None','Weapon1Type.sword',0,0,0,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1009,'Lief','Weapon1Type.sword',5,500,3,'Legendary sword of the Scion.')"""),
        crsr.execute("""INSERT INTO items VALUES(1010,'Hunting Knife','Weapon1Type.dagger',1,5,3,'A knife used to hunt insects.')"""),
        crsr.execute("""INSERT INTO items VALUES(1011,'Relic sword','Weapon1Type.sword',3,10,3,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1012,'Relic Spear','Weapon1Type.spear',3,8,3, '')"""),
        crsr.execute("""INSERT INTO items VALUES(1013,'Relic Axe','Weapon1Type.axe',4,12,3, '')"""),
        crsr.execute("""INSERT INTO items VALUES(1014,'Old Club','Weapon1Type.mace',4,10,3,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1015,'Crooked Stick','Weapon1Type.staff',2,3,3,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1016,'Training Bow','Weapon2Type.bow',2,20,4,'A large bow made for practice.')"""),
        crsr.execute("""INSERT INTO items VALUES(1017,'Training Crossbow','Weapon2Type.crossbow',2,20,4,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1018,'Grass Sling','Weapon2Type.sling',2,20,4,'A sling made from grass; not very practical')"""),
        crsr.execute("""INSERT INTO items VALUES(1019,'Wooden Shield','Weapon2Type.shield',4,20,4,'A basic round wooden shield.')"""),
        crsr.execute("""INSERT INTO items VALUES(1020,'Poison wand','Weapon2Type.wand', 1,0,4,'A wand containing a weak poison')"""),
        crsr.execute("""INSERT INTO items VALUES(1021,'Mushroom staff','Weapon1Type.staff',2,3,3,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1022,'None','ArmourType.hat',0,0,0,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1023,'Old Tunic','ArmourType.shirt', 1,1,0,'An old shirt with holes in it.')"""),
        crsr.execute("""INSERT INTO items VALUES(1024,'Travelling Cloak','ArmourType.shirt',10,10,6,'A too large black cloak. Good for keeping ou of sight but heavy.')"""),
        crsr.execute("""INSERT INTO items VALUES(1025,'Worn Trousers','ArmourType.trousers',1,1,0,'An old pair of trousers long past their prime')"""),
        crsr.execute("""INSERT INTO items VALUES(1026,'Primitive Arrow','ProjectileType.arrow',1,10,8,'Arrows made from stone heads and twigs.')"""),
        crsr.execute("""INSERT INTO items VALUES(1027,'Rope Net','ProjectileType.toss',1,0,9, 'A rope net to catch your enemies.')"""),
        crsr.execute("""INSERT INTO items VALUES(1028,'Wooden Bolt','ProjectileType.bolt',1,10,8,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1029,'Softstone','ProjectileType.stone',1,10,8,'')"""),
        crsr.execute("""INSERT INTO items VALUES(1030,'Bramble leaves','ItemType.ingredient',1,0,10,'The leaves of a blackberry bush')""")
    def CreateManuverDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS manuvers(MANU_ID bigint PRIMARY KEY NOT NULL,NAME,SPECIALTYPE, ATTACKTYPE, DAMAGE, COST, EFFECTIVNESS, EFFECT)")
        crsr.execute("""INSERT INTO manuvers VALUES(101,'Advence','SpecialType2.enhance','AttackType.single', 0,10,100, 'Move in range.')"""),
        crsr.execute("""INSERT INTO manuvers VALUES(102,'Retreat','SpecialType2.enhance','AttackType.single', 0,10,100, 'Move out of range.')""")
    def CreateSpellDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS spells(SPELL_ID bigint PRIMARY KEY NOT NULL,NAME,SPECIALTYPE, SPELLTYPE, ATTACKTYPE, DAMAGE, COST, EFFECTIVNESS, EFFECT)")
        crsr.execute("""INSERT INTO spells VALUES(101,'Poison nettles','SpecialType2.offence','SpellType.Nature','AttackType.single',1, 10, 100,'Poisons an opponent')"""),
        crsr.execute("""INSERT INTO spells VALUES(102,'Grow mushrooms','SpecialType2.offence','SpellType.Nature','AttackType.single',0, 10, 100,'Grow mushrooms on your enemy to hinder them.')"""),
        crsr.execute("""INSERT INTO spells VALUES(103,'Grow mushrooms','SpecialType2.support','SpellType.Nature','AttackType.single',9, 0, 100,'Grow edable mushrooms for an ally to restore stamina.')"""),
        crsr.execute("""INSERT INTO spells VALUES(104,'Grow mushrooms','SpecialType2.enhance','SpellType.Nature','AttackType.single',9, 0, 100,'Grow edable mushrooms for the caster to restore stamina.')""")
        crsr.execute("""INSERT INTO spells VALUES(105,'Heal','SpecialType2.support','SpellType.Blessing','AttackType.single',100, 10, 100,'Heals an ally')""")
    def CreateCombineDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS spell_combinations(SPELL_ID bigint PRIMARY KEY NOT NULL,NAME,SPECIALTYPE, SPELLTYPE, ATTACKTYPE, DAMAGE, COST, EFFECTIVNESS, EFFECT)")
        crsr.execute("""INSERT INTO spell_combinations VALUES(201,'Poisonous mushrooms','SpecialType2.offence','SpellType.nature', 'AttackType.single', 9, 10, 100, 'Grow poisinous mushrooms on the enemy.')""")
    def CreateItemSpellDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS item_spells(ITEM_ID bigint NOT NULL, SPELL_ID bigint NOT NULL)")
        crsr.execute("""INSERT INTO item_spells VALUES(1020, 101)""")
        crsr.execute("""INSERT INTO item_spells VALUES(1021, 102)""")
        crsr.execute("""INSERT INTO item_spells VALUES(1021, 103)""")
        crsr.execute("""INSERT INTO item_spells VALUES(1021, 104)""")
    def CreateCombineSpellDB(self, crsr):
        crsr.execute("CREATE TABLE IF NOT EXISTS combine_spells(SPELL_ID bigint NOT NULL, SPELL_1 bigint NOT NULL, SPELL_2 bigint NOT NULL, SPELL_3 bigint)")
        crsr.execute("""INSERT INTO combine_spells VALUES(201, 101, 102,NULL)""")
    def DropItemDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS items");
    def DropSpellDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS spells");
    def DropManuverDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS manuvers");
    def DropItemSpellDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS item_spells");
    def DropCombineDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS spell_combinations");
    def DropCombineSpellDB(self, crsr):
        crsr.execute("DROP TABLE IF EXISTS combine_spells");
    def GetItems(self, crsr):
        row = crsr.execute("SELECT * FROM items ORDER BY priority")
        #print(crsr.fetchall())
        return row
    def GetByPriority(self, crsr, p):
        row = crsr.execute("SELECT * FROM items where priority = (?)", (p,))
        #print(crsr.fetchall())
        return crsr.fetchall()
    def GetItemByItemType(self, crsr, itemType):
        items = []
        #print(itemType)
        values = "*"
        joins = ""
        if(itemType == ItemType.food):
            values = "ITEM_ID, NAME, WEIGHT, RECOVERS"
        elif(itemType == ItemType.healing):
            values = "ITEM_ID, NAME, WEIGHT, RECOVERS, DESCRIPTION"
        elif(itemType == Weapon1Type.sword or itemType == Weapon1Type.dagger or itemType == Weapon1Type.spear or
             itemType == Weapon1Type.axe or itemType == Weapon1Type.mace or
             itemType == Weapon2Type.bow or itemType == Weapon2Type.crossbow or itemType == Weapon2Type.sling or itemType == Weapon2Type.shield or
             itemType == ArmourType.hat or itemType == ArmourType.shirt or itemType == ArmourType.trousers or
             itemType == ProjectileType.arrow or itemType == ProjectileType.bolt or itemType == ProjectileType.stone or
             itemType == Weapon1Type.staff or itemType == Weapon2Type.wand or
             itemType == ProjectileType.toss):
            values = "ITEM_ID, NAME, RECOVERS, WEIGHT, DESCRIPTION"
        #elif(itemType == Weapon1Type.staff or itemType == Weapon2Type.wand):
        #    values = "i.ITEM_ID, i.NAME, i.RECOVERS, i.WEIGHT, i.DESCRIPTION, s.SPELL_ID, s.NAME"
        #    joins = """INNER JOIN item_spells isp ON i.ITEM_ID = isp.ITEM_ID
        #            INNER JOIN spells s ON isp.SPELL_ID = s.SPELL_ID"""
        elif(itemType == ItemType.ingredient):
            values = "ITEM_ID, NAME, WEIGHT, DESCRIPTION"
        row = crsr.execute("SELECT "+values+" FROM items i "+joins+" where ITEMTYPE = '" + str(itemType) + "'").fetchall()
        #items = crsr.fetchall()
        #print(row)
        return row
    def GetManuverByType(self, crsr, specialType):
        row = crsr.execute("SELECT MANU_ID ,NAME, DAMAGE, COST, EFFECTIVNESS, EFFECT FROM manuvers where SPECIALTYPE = '" + str(specialType) + "'").fetchall()
        #print(row)
        return row
    def GetSpellType(self, crsr, spellType, specialType):
        spellValue = "SPELL_ID ,NAME, DAMAGE, COST, EFFECTIVNESS, EFFECT"
        specialValue = ""
        if(spellType == SpellType.Nature):
            if (specialType == SpecialType2.enhance):
                spellValue = "SPELL_ID ,NAME, DAMAGE, COST, EFFECTIVNESS, EFFECT"
            else:
                spellValue = "SPELL_ID ,NAME, ATTACKTYPE, DAMAGE, COST, EFFECTIVNESS, EFFECT"
            specialValue = "AND SPECIALTYPE = '" + str(specialType) + "'"
        row = crsr.execute("SELECT "+spellValue+" FROM spells where SPELLTYPE = '" + str(spellType) +"'"+ specialValue).fetchall()
        #print(row)
        return row
    def GetSpellByType(self, crsr, specialType):
        row = crsr.execute("SELECT SPELL_ID ,NAME, DAMAGE, COST, EFFECTIVNESS, EFFECT FROM spells where SPECIALTYPE = '" + str(specialType) + "'").fetchall()
        #print(row)
        return row
    def GetSpells(self, crsr, item_id):
        row = crsr.execute("SELECT s.SPELL_ID, s.NAME FROM items i INNER JOIN item_spells isp ON i.ITEM_ID = isp.ITEM_ID INNER JOIN spells s ON isp.SPELL_ID = s.SPELL_ID where i.ITEM_ID = '" + str(item_id) + "'").fetchall()
        #items = crsr.fetchall()
        #print("Spells", row)
        return row
    def GetCombinations(self, crsr):
        row = crsr.execute("SELECT i.SPELL_ID, i.NAME, i.ATTACKTYPE, i.DAMAGE, i.COST, i.EFFECTIVNESS, i.EFFECT, isp.SPELL_1, isp.SPELL_2 FROM spell_combinations i INNER JOIN combine_spells isp ON i.SPELL_ID = isp.SPELL_ID INNER JOIN spells s ON isp.SPELL_1 = s.SPELL_ID INNER JOIN spells s2 ON isp.SPELL_2 = s2.SPELL_ID").fetchall()
        #items = crsr.fetchall()
        #print(row)
        return row
        
#DB.DropItemDB(DB.crsr)
#CreateItemDB(crsr)
#GetItems(crsr)
#GetPrimaryWeapons(crsr, 3)
#GetByPriority(crsr, 3)
#GetItemByItemType(crsr, ItemType.healing)
#GetItemByItemType(crsr, ItemType.food)
#GetItemByItemType(crsr, Weapon1Type.sword)
#GetItemByItemType(crsr, ArmourType.shirt)
#GetItemByItemType(crsr, ItemType.projectile)
