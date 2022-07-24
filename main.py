import os
import pickle
import random
import examineMode
import talkingMode
import moving
import ItemClasses
import inventory
import equipment
import dialog
import combat
import objective
import quest
from data import typeSpf
import playableChars
import enemyUnits
#Loop
menu_active = True
game_active = False
game_over = False
tutorial1 = True
chapter1 = False
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

#Set Class
#party = [playableChars.Alder()]
#alder = party[0]
item = ItemClasses
com = combat
eqp = equipment.Equipment()
obj = objective.Objective()
qst = quest

#Items lists
weapons = [item.Sword('0','None',0,0,''),
           item.Sword('1','Lief',500,5,'Legendary sword of the Scion.'),
           item.Dagger('2','Hunting Knife',5,1,'A knife used to hunt insects.'),
           item.Bow('1','Training Bow', 20,2, 'A large bow made for practice.'),
           item.Shield('1','Wooden Shield', 20,4,'A basic round wooden shield.')
           ]

armours = [item.Hat('1','None',0,0,''),
           item.Shirt('1','Old Tunic', 1,1,'An old shirt with holes in it.'),
           item.Shirt('2', 'Travelling Cloak', 10,10,'A too large black cloak. Good for keeping ou of sight but heavy.'),
           item.Trousers('1','Worn Trousers', 1,1,'An old pair of trousers long past their prime')
           ]
food = [item.Food('1','Blackberry',1,5),
        item.Food('2','Dried Fruit',1,5),
        item.Food('3','Hazelnut',1,5),
        item.Food('4', 'Mushroom', 1,5),
        item.Food('5', 'Raw Bug Meat',3,10),
        item.Food('6', 'Brown Bread',3,50)
        ]
items = [{'itemId' : '1', 'name' : 'Bandage', 'type' : ItemType.healing, 'description' : 'A cloth bandage to treat wounds',
          'heals' : 10, 'count' : 0, 'priority': 2}
         ]
projec = [{'itemId' : '1', 'name' : 'Primitive Arrow', 'type' : ItemType.projectile, 'description' : 'Arrows made from readily available materials.',
           'weapon' : Weapon2Type.bow, 'damage' : 10, 'count' : 0, 'priority': 8},
          {'itemId' : '2', 'name' : 'Rope Net', 'type' : ItemType.toss,  'description' : 'A rope net to catch your enemies.',
           'weapon' : 'none', 'damage' : 0, 'count' : 0, 'priority': 9}
          ]
ingre = [{'ingId' : '1', 'name' : 'Bramble leaves', 'type' : ItemType.ingredient, 'description' : 'The leaves of a blackberry bush',
          'count' : 0, 'priority': 10}
         ]
#Inventory
shill = 0
inv = inventory.Inventory()
#Universal Specials
manuvers = [{'spId':'1','name':'Advence', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move towards out of ranged opponents or move in range.'},
           {'spId':'2','name':'Retreat', 'type':SpecialType2.enhance, 'specialType':SpecialType1.manuver, 'damage' : 0, 'cost':10, 'effectivness':100, 'active':False, 'unlocked':True, 'effect':'Move out of range.'}
           ]
spells = []
combinations = []
#Location
locations = [{"locId" : "1", "name" : "Cottage Kitchen"},
             {"locId" : "2", "name" : "Cottage Living Room"},
             {"locId" : "3", "name" : "Cottage Clearing"},
             {"locId" : "4", "name" : "Cottage Shed"},
             {"locId" : "5", "name" : "Alder's Room"},
             {"locId" : "6", "name" : "Forest Clearing"},
             {"locId" : "7", "name" : "???"}
             ]
location = '1'
#Interactable characters
actor = [{'actorId' : '1', 'name' : 'Florence', 'species' : 'human', 'title' : 'Witches apprentis'},
         {'actorId' : '2', 'name' : 'Kyla', 'species' : 'human', 'title' : 'Woodland witch'},
         {'actorId' : '3', 'name' : 'Thay', 'species' : 'hedgehog', 'title' : 'Wandering herbalist'},
         {'actorId' : '4', 'name' : 'Trissie', 'species' : 'squirrel', 'title' : 'Path finder'},
         {'actorId' : '5', 'name' : 'Jeb', 'species' : 'weasel', 'title' : 'Merchant'},
         {'actorId' : '6', 'name' : '???', 'species' : 'mouse', 'title' : '???'}
         ]
class Party():
    def __init__(self):
        self.alder = playableChars.Alder()
    def listParty(self):
        return [self.alder]
party = Party()
alder = party.alder
        
class Story():
    def __init__(self, chapter, part, tutorComp):
        #Story Switches
        self.chapter = '0'
        self.part = '1'
        self.tutorComp = False
        self.switch = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.tutorialSwitch = [True, True, True, True, True, True, True]
        self.c2Switch = [True, True, True, True, True, True]
        self.c3Switch = [True, True, True, True, True, True, True]
        self.branchSwitch = ['0']
        self.PKSwitch = [True, True, True, True, True, True]

        #Quests
        self.mQuests = [qst.Quest('1','Florence','Bug hunt',['Collect two pieces of bug meat'],'',0,
                    'collect', [food[4]],2)
                   ]
        self.sQuests = [qst.Quest('1','Kyla','Servants work', ['Clean fireplace:', 'Scrub caldron:', 'Grind bramble leaves in mortar:'], 'none', 0,
                    'action', [False, False, False], 1),
                   qst.Quest('2','Florence','Provisions', ['Collect food x'], food[5], 1,
                    'action', [False], 1),
                   qst.Quest('3','Kyla','Packing up', ['Take books from bookshelf:', 'Break down wall', 'Take pots from the shed:'], 'shillings', 2,
                    'action', [False, False, False], 1)
                   ]
story = Story('0', '1', False)

def cont():
    con = input()
    if (con == 'skip'):
        return

#Save and Load Content
PIK = 'demo.dat'
data = [location, story, inv]

class Null:
    def __init__(self):
        self.enId = '0'
        self.name = 'Null'
#Boost Stats
def stBoost(p, sb):
    if(sb['stat'] == 'h' and sb['active']):
        p.maxHealth += sb['boost']
        p.health += sb['boost']
    elif(sb['stat'] == 's' and sb['active']):
        p.maxStamina += sb['boost']
        p.stamina += sb['boost']
    elif(sb['stat'] == 'at' and sb['active']):
        p.baseAttack += sb['boost']
    elif(sb['stat'] == 'df' and sb['active']):
        p.baseDefence += sb['boost']
    elif(sb['stat'] == 'ac' and sb['active']):
        p.baseAccuracy += sb['boost']
    elif(sb['stat'] == 'sp' and sb['active']):
        p.baseSpeed += sb['boost']
    elif(sb['stat'] == 'ev' and sb['active']):
        p.baseEvasion += sb['boost']
#Print Skill Tree
def skillTree(p):
    print('\nSkills')
    print('Skill Points: ', p.skillPoints)
    print('You can spend skill points on a stat boost or a character skill.')
    print('1: Stat Boosts')
    print('2: Special Skills')
    skill = input('Skill Type: ')
    if (skill == '1'):
        print('\nStat Boosts')
        print('Skill Points: ', p.skillPoints)
        count = 1
        temp = False
        for i in p.statBoost:
            if (i['No'] == '1' and i['active'] == False):
                print(count,': ', i['name'], ' stat increaced by ', i['boost'])
                count += 1
            elif (i['No'] == '2' and i['active'] == False and temp == True):
                print(count,': ', i['name'], '  stat increaced by  ', i['boost'])
                count += 1
            elif (i['No'] == '3' and i['active'] == False and temp == True):
                print(count,': ', i['name'], '  stat increaced by  ', i['boost'])
                count += 1
            if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                temp = True
            else:
                temp = False
        sb = input('Boost: ')
        count = 1
        for i in p.statBoost:
            if (i['No'] == '1' and i['active'] == False):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            elif (i['No'] == '2' and i['active'] == False and temp == True):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            elif (i['No'] == '3' and i['active'] == False and temp == True):
                if(sb == str(count)):
                    if (p.skillPoints > 0):
                        i['active'] = True
                        stBoost(p,i)
                        print(i['name'],'has been unlocked!')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
            if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                temp = True
            else:
                temp = False
    elif (skill == '2'):
        print('\nSpecial Skills')
        print('Skill Points: ', p.skillPoints)
        count = 1
        for i in p.abilities:
            if (i['unlocked'] == False):   
                print(count,': ', i['name'], ' - ', i['effect'])
                count += 1
        sa = input('Boost: ')
        count = 1
        for i in p.abilities:
            if (i['unlocked'] == False):
                if(sa == str(count)):
                    if (p.skillPoints > 0):
                        i['unlocked'] = True
                        print(i['name'], 'has been unlocked')
                        p.skillPoints -= 1
                    else:
                        print('You do not have enough skill points.')
                count += 1
    
#The item should be equipped
#If the item is not starting clothing then it should be return to the inventory
#Only items of speciec type can be equipped
def equip(p):
    equiping = True
    while (equiping == True):
        equipable = []
        print('\nEquip what')
        print('1: Head')
        print('2: Body')
        print('3: Legs')
        print('4: Main Weapon')
        print('5: Secondary Weapon')
        print('e - Exit')
        i = input('Action: ')
        if (i == '1'):
            count = eqp.getHat(p,inv,equipable)
            eqp.head(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '2'):
            count = eqp.getShirt(p,inv,equipable)
            eqp.body(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '3'):
            count = eqp.getTrousers(p,inv,equipable)
            eqp.legs(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '4'):
            count = eqp.getPrimeWeapon(p,inv,equipable)
            eqp.primeWeapon(p, eqp.setEquipment(count,equipable), inv)
        elif (i == '5'):
            count = eqp.getSecondWeapon(p,inv,equipable)
            eqp.secondWeapon(p, eqp.setEquipment(count,equipable), inv)
        elif (i == 'e'):
            equiping = False
            
#If character dies
def death():
    global game_active
    loss = inv.shill / 10
    if (round(loss) <= 0):
        loss = 1
    inv.shillings(-loss)
    print('\nAlder was slain.')
    cont()
    game_active = False
#Hunder
def hunger(inCombat):
    if(party.alder.stamina <= 0):
        party.alder.health -= 1
        if (party.alder.health <= 0):
            if(inCombat != True):
                death()
        else:
            print('You need to eat!')    
    if(party.alder.stamina < 0):
        party.alder.stamina = 0

#Yes or no answers
def yn(yesNo):
    while(yesNo != 'y' or yesNo != 'Y' or yesNo != 'yes' or yesNo != 'Yes' or
          yesNo != 'n' or yesNo != 'N' or yesNo != 'no' or yesNo != 'No'):
        if (yesNo == 'y' or yesNo == 'Y' or yesNo == 'yes' or yesNo == 'Yes'):
            return True
        elif (yesNo == 'n' or yesNo == 'N' or yesNo == 'no' or yesNo == 'No'):
            return False
        else:
            yesNo = input('"yes" or "no" responses only!: ')

#Save the game
def save(location, story):
    data = [location, story, tutorComp, inv, party]
    i = input('Save in file "1", "2" or "3":')
    if (i == '1'):
        PIK = 'data/file1.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')
    elif (i == '2'):
        PIK = 'data/file2.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')
    elif (i == '3'):
        PIK = 'data/file3.dat'
        with open(PIK, "wb") as f:
            #print(data)
            pickle.dump(data, f)
        print ('Game Saved!')

def inventory():
    listItems = []
    bag = True
    j = ''
    while(bag == True):
        #View the items in inventory
        #The same items should be counted to keep the list clear
        #Items should be in a order based on the item type
        #Input should allow the list to be narrowed down or print all items
        inv.printInventory(j, listItems)
        print('\n1: Appraise')
        print('2: Use')
        print('3: Equip')
        print('e - Exit')
        i = input('Item: ')
        if (i == '' or i == 'food' or i == 'Food' or i == 'consumables' or i == 'Consumables' or i == 'healing' or i == 'Healing' or
            i == 'health' or i == 'Health' or i == 'weapons' or i == 'Weapons'  or i == 'armour' or i == 'Armour' or
            i == 'projectiles' or i == 'Projectiles' or i == 'ingredients' or i == 'Ingredients' or
            i == '1' or i == '2' or i == '3' or i == 'e'):
            j = i
        #Appraise items in inventory
        if (j == '1'):
            appraise = input('\nItem number: ')
            count = 1
            for i in listItems:
                inv.appraise();
        elif (j == '2'):
            inv.useItem(alder)
        elif (j == '3'):
            equip(alder)
        elif (j == 'e'):
            bag = False
        if (j == '1' or j == '2' or j == '3'):
            j = ''
    
#Achive objectives
def achive():
    for q in story.mQuests:
        q.questProgress(inv)
        #if(q['accepted'] == True and q['submitted'] != True):
        #    if (q['questId'] == '1'):
        #        amount = 0
        #        for i in inv.itemList:
        #            if (i['item'].itemType == ItemType.food):
        #                if (i['item'].itemId == q['required']['itemId']):
        #                    amount += i['count']
        #        if (amount >= 2):
        #            q['completed'] = True
        #        else:
        #            q['completed'] = False
    for q in story.sQuests:
        q.questProgress(inv)
            # #if(q['accepted'] == True and q['submitted'] != True):
            #if (q['type'] == 'action'):
            #    count = 0
            #    for i in q['required']:
            #        if (i == True):
            #            count += 1
            #    if (count == len(q['required'])):
            #        q['completed'] = True
            #if (q['type'] == 'collect'):
            #    count = 0
            #    for i in q['required']:
            #        for j in inv.itemList:
            #            if(i['type'] == j['item'].itemType):
            #                if(i['itemId'] == j['item'].itemId):
            #                    if (j['count'] == q['qnt'][count]):
            #                        q['completed'] = True
            #        count += 1
def helper():
    print("\nCommand: e, examine, Examine - Allows Alder to investigate his surroundings. Examinating further may reveal an item you can pickup.")
    print("Command: m, move, Move - Move to the next area.")
    print("Command: t, talk, Talk - Talk to a character.")
    print("Command: z, stats, Stats - Print the statistics of the playable characters.")
    print("Command: o, objective, Objective - Print the main and side quests.")
    print("Command: i, items, Items - View inventory.")
    print("Command: x, equip, Equip - Equip item.")
    print("Command: k, skill, Skill - Unlock Skill.")
    print("Command: s, save, Save - Save the game.")
    print("Command: 1, 2, etc - When you have a list of options.")    
    print("Command: y, Y, yes, Yes or, n, N, no, No - (y/n) statments.")
    print("(!) - Quest available")
    print("Command: q, quit, Quit - Exit to the main menu")

def helper2():
    print("Command: 1, attack, Attack - Deal damage to an opponent using a primary weapon.")
    print("Command: 2, defence, Defence - Absorb damage from an incoming attack.")
    print("Command: 3, appraise, Appraise - Get details on enemies.")
    print("Command: 4, special, Special - Use a special skill.")
    print("Command: 5, item, Item - Use an item from inventory.")
    print("Command: 6, flee, Flee - Escape the battle.")
    print("Food: Items used to recover stamina.")
    print("Medicine: Items used to heal or remove a status condition.")
    print("Ranged Weapons: To use a ranged weapon select a supported projectile from items then on the next turn attack to fire.")
    print("Throwing Items: Items such as nets can be thrown ")
    print("Order of combat: Fastest combatant.")

def free(story):
    global game_active, game_over, location
    hunger(False)
    achive()
    if (game_over == True):
        game_active = False
    elif (game_active == True):
        print('\nInteract')
        if(story.tutorialSwitch[0] == True):
            print("You will need to have a quick look around. Type "'"examine" or "e"'" to explore the room Alder is currently in, then type in an 'object' from that room. If you are having trouble with what to do, check the "'"objectives"("o")'"")
        elif(story.tutorialSwitch[1] == True):
            print('Alder needs to go outside. He will have to "move"("m") through the living room and then outside.')
        elif(story.tutorialSwitch[2] == True):
            print('While we wait for Thay, let'"'"'s "talk"("t") to Florence.')
        elif(story.tutorialSwitch[3] == True):
            print('Some dialogs can unlock new ones. Let'"'"'s talk to Thay now.')
        elif(story.tutorialSwitch[4] == True):
            print('Alder will need the knife which is somewhere in the shed. Examine the area to find and pick up the knife and "equip"("x") the knife from your "items"("i") inventory as main weapon.')
        elif(story.tutorialSwitch[5] == True):
            print('Leave the cottage grounds and examine the area to find an opponent to fight. There will be six options available for each turn. Type "h2", "help2" or "Help2" for more details.')
        elif(story.tutorialSwitch[6] == True):
            print('Return to the cottage and sleep to bring an end to the day and the tutorial.')
        print("Health: ", party.alder.health, '/', party.alder.maxHealth, "| Stamina: ", party.alder.stamina, '/', party.alder.maxStamina)
        print("Type command: h, help, Help - For help.")
        action = input('Enter Command: ')
        if (action == 'e' or action == 'examine' or action == 'Examine'):
            #examine(location)
            examineMode.examine(game_over, party, location, story, inv)
        elif (action == 't' or action == 'talk' or action == 'Talk'):
            talkingMode.talk(game_over, party, location, story, inv)
        elif (action == 'm' or action == 'move' or action == 'Move'):
            location = moving.move(game_over, party, location, story, inv)
        elif (action == 'z' or action == 'stats' or action == 'Stats:'):
            party.alder.stats()
        elif (action == 'o' or action == 'objective' or action == 'Objective'):
            obj.printObjective(story, inv, party)
        elif (action == 'i' or action == 'items' or action == 'Items'):
            if (location != '7'):
                inventory()
            else:
                print('Alder did not have anything with him.')
        elif (action == 'x' or action == 'equip' or action == 'Equip'):
            if (location != '7'):
                equip(party.alder)
            else:
                print('Alder did not have anything with him.')
        elif (action == 'k' or action == 'skill' or action == 'Skill'):
            skillTree(party.alder)
        elif (action == 'h' or action == 'help' or action == 'Help'):
            helper()
        elif (action == 'h2' or action == 'help2' or action == 'Help2'):
            helper2()
        elif (action == 's' or action == 'save' or action == 'Save'):
            save(location, story)
        elif (action == 'q' or action == 'quit' or action == 'Quit'):
            print ("Are you sure you wan to quit to menu y/n")
            q = input('Enter Command: ')
            if (q == 'y' or q == 'Y' or q == 'yes' or q == 'Yes'):
                game_active = False

def game():
    global story, shill, location
    print('Chapter: ', story.chapter)
    print('The game will now begin. Press enter to print the next line.')
    print("You may skip the dialogue by typing 'skip' then pressing enter.")
    while (game_active == True):
        if (tutorComp == False):
            tutorial1 = True
        if (story.chapter == '0'):
            prologue = True
            dialog.cutscene(story, '0')
            prologue = False
            story.chapter = '1'
        if (story.chapter == '1'):
            if (story.switch[0] == True):
                dialog.cutscene(story, '0')
                story.switch[0] = False
            elif (story.switch[1] == True and story.part == '2'):
                dialog.cutscene(story, '1')
                story.switch[1] = False
            elif (story.switch[2] == True and story.part == '2'):
                dialog.cutscene(story, '2')
                story.switch[2] = False
            elif (story.switch[3] == True and story.part == '3'):
                dialog.cutscene(story, '3')
                story.mQuests[0].accepted = True
                story.switch[3] = False
            elif (story.switch[4] == True and story.part == '4'):
                dialog.cutscene(story, '4')
                story.switch[4] = False
            if (game_active == True):
                free(story)
        if (story.chapter == '2'):
            if (story.switch[5] == True and story.part == '1'):
                dialog.cutscene(story, '5')
                location = '3'
                story.switch[5] = False
            elif (story.switch[6] == True and story.part == '2'):
                dialog.cutscene(story, '6')
                story.switch[6] = False
                story.c2Switch[0] = False
            elif (story.switch[7] == True and story.part == '3'):
                dialog.cutscene(story, '7')
                location = '7'
                story.switch[7] = False
            elif (story.switch[8] == True and story.part == '4'):
                dialog.cutscene(story, '8')
                story.c2Switch[3] = False
                story.switch[8] = False
            elif (story.switch[9] == True and story.part == '5'):
                dialog.cutscene(story, '9')
                story.chapter = '3'
                story.part = '1'
                story.switch[9] = False
                story.switch[10] = True
                story.part = '1'
            elif (game_active == True):
                free(story)
        if (story.chapter == '3'):
            author = False
            if (story.switch[10] == True and story.part == '1'):
                location = '5'
                dialog.cutscene(story, '10')
                story.switch[10] = False
            elif (story.switch[11] == True and story.part == '2'):
                dialog.cutscene(story, '11')
                story.c3Switch[2] = False
                story.switch[11] = False
            elif (story.switch[12] == True and story.part == '3'):
                dialog.cutscene(story, '12')
                story.c3Switch[3] = False
                story.switch[12] = False
            elif (story.switch[13] == True and story.part == '3'):
                dialog.cutscene(story, '13')
                print('10 shillings obtained!\n')
                inv.shill += 10
                story.c3Switch[4] = False
                story.switch[13] = False
            elif (story.switch[14] == True and story.part == '4'):
                dialog.cutscene(story, '14')
                story.c3Switch[5] = False
                story.switch[14] = False
            elif (story.switch[15] == True and story.part == '4'):
                dialog.cutscene(story, '15')
                author = True
                story.switch[15] = False
            while (author == True):
                print('James Stockwell:')
                print('"Thank you for playing the demo for the Wild and Wyrd. Please let me know if there are any errors or grammer mistakes. Please support me if you want to see more of Alder'"'"'s story."')
                cont()
            if (game_active == True):
                free(story)
    

def loadGame():
    global game_active, location, story, shill, tutorComp, inv,party
    PIK = ''
    op = input('Open save file "1", "2" or "3": ')
    if (op == '1'):
        PIK = 'data/file1.dat'
    elif (op == '2'):
        PIK = 'data/file2.dat'
    elif (op == '3'):
        PIK = 'data/file3.dat'
    try:
        with open(PIK, "rb") as f:
            data = pickle.load(f)
            location = data[0]
            story = data[1]
            tutorComp = data[2]
            inv = data[3]
            party = data[4]
            alder = party.alder
            game_active = True
    except:
        print('Saved file not found!')

def menu():
    global menu_active, chapter, part, chapter1, tutorComp, game_active, game_over, switch, tutorialSwitch, c2Switch, c3Switch, shill, inv, PKSwitch, location
    while (menu_active == True):
        print('Wild and Wyrd')
        print('n - New Game')
        print('l - Load')
        print('s - Settings')
        print('q - Quit')
        action = input('Enter Command: ')
        if (action == 'n'):
            game_active = True
            tutorial1 = True
            tutorComp = False
            chapter1 = False
            location = '1'
            chapter = '0'
            part = '1'
            #inv = []
            #inv.shill = 0
            for i in story.PKSwitch:
                i = True
            #Story Switches
            for i in story.switch:
                i = False
            story.switch[0] = True
            for i in story.tutorialSwitch:
                i = True
            for i in story.c2Switch:
                i = True
            for i in story.c3Switch:
                i = True
            for i in story.branchSwitch:
                i = '0'
            for i in story.mQuests:
                i.accepted = False
                i.completed = False
                i.submitted = False
            for i in story.sQuests:
                i.accepted = False
                i.completed = False
                i.submitted = False
            #Alder Stats
            alder.maxHealth = 60
            alder.health = alder.maxHealth
            alder.maxStamina = 60
            alder.stamina = alder.maxStamina
            alder.cLvl = 1
            alder.cExp = 0
            alder.baseAttack = 10
            alder.baseDefence = 10
            alder.baseSpeed = 5
            alder.baseEvasion = 5
            alder.head = armours[0]
            alder.body = armours[1]
            alder.legs = armours[3]
            alder.weapon1 = weapons[0]
            alder.weapon2 = weapons[0]
            #Start Game
            game()
        elif (action == 'l'):
            loadGame()
            if (game_active == True):
                game_over = False
                #Start Game
                game()
        elif (action == 'q'):
            menu_active = False
menu()
quit()
