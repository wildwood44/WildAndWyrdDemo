import sqlite3
from data import game_database

# Connecting to database
connection = sqlite3.connect("waw.db", isolation_level=None)
# Cursor
crsr = connection.cursor()

print("Loading", end="")

db = game_database.DB(connection, crsr)
# Create Items Database
db.DropItemDB(crsr)
db.DropSpellDB(crsr)
db.DropItemSpellDB(crsr)
db.DropManuverDB(crsr)
db.DropCombineDB(crsr)
db.DropCombineSpellDB(crsr)
print(".", end="")
db.CreateItemDB(crsr)
print(".", end="")
db.CreateSpellDB(crsr)
print(".", end="")
db.CreateItemSpellDB(crsr)
print(".", end="")
db.CreateManuverDB(crsr)
print(".", end="")
db.CreateCombineDB(crsr)
print(".", end="")
db.CreateCombineSpellDB(crsr)
print(".")

crsr.close()
connection.close()
