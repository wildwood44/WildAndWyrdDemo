import random
import itemList
import combat
import playableChars
import enemyUnits
import books
import shop
import dialog
from data import typeSpf
item = itemList
com = combat
shop = shop.Shop()
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
#Location
locations = [{"locId" : "1", "name" : "Cottage Kitchen"},
             {"locId" : "2", "name" : "Cottage Living Room"},
             {"locId" : "3", "name" : "Cottage Clearing"},
             {"locId" : "4", "name" : "Cottage Shed"},
             {"locId" : "5", "name" : "Alder's Room"},
             {"locId" : "6", "name" : "Forest Clearing"},
             {"locId" : "7", "name" : "???"}
             ]

def cont():
    con = input()
    if (con == 'skip'):
        return
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
#Recover health and stamina
def bed(party):
    party.alder.health = party.alder.maxHealth
    party.alder.stamina = party.alder.maxStamina

def examine(game_over, party, location, story, inv, gloss):
    alder = party.alder
    examining = True
    while (examining == True):
        print('\nExamine')
        print('Type "e" to end examining')
        for i in locations:
            if (location == i['locId']):
                print(i['name'])
        if (location == '1'):
            dialog.room(story, 'kitchen')
            e = input('Examine: ')
            if (e == 'cauldron' or e == 'Cauldron'):
                if (story.sQuests[0].accepted == True and story.sQuests[0].required[1] == False):
                    dialog.examine(story, 'cauldron', '1')
                    story.sQuests[0].required[1] = True
                    examining = False
                else:
                    dialog.examine(story, 'cauldron')
                gloss.constructs[0].unlock()
            elif (e == 'pots' or e == 'Pots'):
                dialog.examine(story, 'pots')
            elif (e == 'cupboard' or e == 'Cupboard'):
                dialog.examine(story, 'cupboard')
            elif (e == 'bowl' or e == 'Bowl'):
                if (story.PKSwitch[0] == True):
                    dialog.examine(story, 'bowl', '1')
                    pickup = input('Take the hazelnuts?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 Hazelnut(s) obtained')
                        inv.addItem(item.food[2], 5)
                        story.PKSwitch[0] = False
                        cont()
                else:
                    dialog.examine(story, 'bowl')
            elif (e == 'basin' or e == 'Basin'):
                dialog.examine(story, 'basin')
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(story.tutorialSwitch[2] == True):
                    dialog.examine(story, 'window', '1')
                    story.chapter = '1'
                    story.tutorialSwitch[0] = False
                else:
                    dialog.examine(story, 'window')
            elif (e == 'hearth' or e == 'Hearth'):
                dialog.examine(story, 'hearth')
                gloss.constructs[1].unlock()
            elif (e == 'table' or e == 'Table' or e == 'tables' or e == 'Tables'):
                dialog.examine(story, 'table')
            elif (e == 'hornets' or e == 'Hornets'):
                if (story.tutorialSwitch[5] == False and story.c2Switch[0] == True):
                    dialog.examine(story, 'hornet')
            elif (e == 'larder' or e == 'Larder'):
                if (story.sQuests[1].accepted == True and story.sQuests[1].required[0] == False):
                    dialog.examine(story, 'larder', '1')
                    story.sQuests[1].required[0] = True
                    story.sQuests[1].completed = True
                elif (story.sQuests[1].required[0] == True):
                    dialog.examine(story, 'larder', '2')
                else:
                    dialog.examine(story, 'larder')
                gloss.constructs[3].unlock()
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '2'):
            dialog.room(story, 'living')
            if (story.sQuests[2].required[1] == True):
                dialog.room(story, 'living', '1')
            e = input('Examine: ')
            if (e == 'bookshelf' or e == 'Bookshelf'):
                if (story.sQuests[2].accepted == True and story.sQuests[2].required[0] == False):
                    dialog.examine(story, 'bookshelf', '7')
                    story.sQuests[2].required[0] = True
                elif(story.sQuests[2].required[0] == True):
                    dialog.examine(story, 'bookshelf', '8')
                else:
                    read = ''
                    while (read != 'e'):
                        print('\nThe books in the living room bookshelf include:')
                        print('\t1) Magic: The Basics')
                        print('\t2) Magical Articles of History')
                        print('\t3) Potions')
                        print('\t4) Developers Note - Kyla'"'"'s cottage')
                        print('\t5) Developers Note - Wild and Wyrd Demo')
                        print('\te) Close')
                        read = input('Read: ')
                        if(read == '1'):
                            books.reading('1', '1')
                        elif(read == '2'):
                            if(story.c3Switch[0] == False and story.c3Switch[1] == True):
                                dialog.examine(story, 'bookshelf', '1')
                                party.alder.weapon1 = item.weapons[1]
                                print(party.alder.weapon1.name,'equipped!')
                                cont()
                                dialog.examine(story, 'bookshelf', '2')
                                options = [False, False, False]
                                while(options[0] == False or options[1] == False or options[2] == False):
                                    print('1: "What is a Scion?"')
                                    print('2: "Does this have anything to do with the mouse I saw in my dream?"')
                                    print('3: "What'"'"'s with the sword blade?"')
                                    c = input('Alder: ')
                                    if (c == '1'):
                                        dialog.examine(story, 'bookshelf', '3')
                                        options[0] = True
                                    elif (c == '2'):
                                        dialog.examine(story, 'bookshelf', '4')
                                        options[1] = True
                                    elif (c == '3'):
                                        dialog.examine(story, 'bookshelf', '5')
                                        options[2] = True
                                dialog.examine(story, 'bookshelf', '6')
                                read = 'e'
                                examining = False
                                story.c3Switch[1] = False
                            else:
                                books.reading('1', '2')
                        elif(read == '3'):
                            books.reading('1', '3')
                        elif(read == '4'):
                            books.reading('2', '1')
                        elif(read == '5'):
                            books.reading('2', '2')
                    
            elif (e == 'fireplace' or e == 'Fireplace'):
                if (story.sQuests[0].accepted == True and story.sQuests[0].required[0] == False):
                    dialog.examine(story, 'fireplace','1')
                    story.sQuests[0].required[0] = True
                    examining = False
                elif (story.sQuests[0].required[0] == False):
                    dialog.examine(story, 'fireplace','2')
                else:
                    dialog.examine(story, 'fireplace')
            elif (e == 'chairs' or e == 'Chairs'):
                dialog.examine(story, 'chairs')
            elif (e == 'table' or e == 'Table'):
                if (story.c3Switch[4] == False and story.c3Switch[5] == True):
                    print('Jeb laid out his wares on the table.')
                    cont()
                    #shop('Jeb')
                    shop.open(shop.getShopkeeper(0), inv)
                    if ((story.sQuests[1].accepted == True and story.sQuests[1].submitted != True) or (story.sQuests[2].accepted == True and story.sQuests[2].submitted != True)):
                            ab = input('Abandon quests?(y/n)')
                            confirm = yn(ab)
                            if (confirm == True):
                                if (story.sQuests[1].accepted == True and story.sQuests[1].submitted != True):
                                    story.sQuests[1].accepted = False
                                    print(story.sQuests[1].name,' abandoned!')
                                if (story.sQuests[2].accepted == True and story.sQuests[2].submitted != True):
                                    story.sQuests[2].accepted = False
                                    print(story.sQuests[1].name,' abandoned!')
                                story.switch[14] = True
                                story.part = '4'
                    else:
                        story.switch[14] = True
                        story.part = '4'
                    examining = False
                else:
                    dialog.examine(story, 'table')
            elif (e == 'door' or e == 'Door'):
                dialog.examine(story, 'door')
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(story.c3Switch[1] == False and story.c3Switch[2] == True):
                    story.switch[11] = True
                    story.part = '2'
                    examining = False
                elif(story.c3Switch[2] == False and story.c3Switch[3] == True):
                    story.switch[12] = True
                    story.part = '3'
                    examining = False
                else:
                    dialog.examine(story, 'window')
            elif (e == 'wall' or e == 'Wall'):
                if (story.sQuests[2].accepted == True and story.sQuests[2].required[1] == False):
                    dialog.examine(story, 'wall','1')
                    victory = com.Battle(party.listParty(), [enemyUnits.Wall(), enemyUnits.Null(), enemyUnits.Null()],inv)
                    if (victory == True):
                        dialog.examine(story, 'wall','2')
                        story.sQuests[2].required[1] = True
                        examining = False
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '3'):
            dialog.room(story, 'outside')
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                dialog.examine(story, 'sky')
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                dialog.examine(story, 'mushroom')
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                dialog.examine(story, 'plants', '1')
            elif (e == 'trees' or e == 'Trees'):
                dialog.examine(story, 'trees')
            elif (e == 'rocks' or e == 'Rocks'):
                dialog.examine(story, 'rocks','1')
            elif (e == 'cottage' or e == 'Cottage'):
                dialog.examine(story, 'cottage')
            elif (e == 'shed' or e == 'Shed'):
                dialog.examine(story, 'shed')
            elif (e == 'bush' or e == 'Bush' or e == 'blackberry' or e == 'Blackberry' or e == 'blackberry bush' or e == 'Blackberry Bush'  or e == 'bramble' or e == 'Bramble'):
                if (story.PKSwitch[2] == True):
                    dialog.examine(story, 'bush')
                else:
                    dialog.examine(story, 'bush','1')
                if (story.PKSwitch[2] == True):
                    pickup = input('Pick the blackberries?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 blackberries obtained')
                        inv.addItem(item.food[0], 5)
                        story.PKSwitch[2] = False
                if (story.sQuests[0].accepted == True and story.sQuests[0].required[2] == False):
                    dialog.examine(story, 'bush','2')
                    count = 0
                    for i in inv.itemList:
                        if (i['item'].itemType == ItemType.ingredient):
                                if (i['item'].ingId == '1'):
                                    count += 1
                    if (count == 0):
                        inv.addItem(item.ingre[0], 1)
                    else:
                        print ('Alder already had some.')
                    examining = False
                gloss.plants[0].unlock()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '4'):
            if (story.c2Switch[2] == True):
                dialog.room(story, 'shed', '1')
            else:
                dialog.room(story, 'shed')
            if (story.sQuests[2].required[1] == True):
                dialog.room(story, 'shed', '2')
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                dialog.examine(story, 'shed_window')
            elif (e == 'tools' or e == 'Tools' or e == 'axe' or e == 'Axe' or e == 'saw' or e == 'Saw' or
                  e == 'pick' or e == 'Pick' or e == 'shovel' or e == 'Shovel' or e == 'sickle' or e == 'Sickle' or
                  e == 'rod' or e == 'Rod' or e == 'fishing' or e == 'Fishing' or e == 'fishing rod' or e == 'Fishing rod'):
                dialog.examine(story, 'tools')
            elif (e == 'pots' or e == 'Pots'):
                if (story.sQuests[2].accepted == True and story.sQuests[2].required[2] == False):
                    dialog.examine(story, 'shed_pots','1')
                    location = '2'
                    story.sQuests[2].required[2] = True
                    examining = False
                elif(story.sQuests[2].required[2] == True):
                    dialog.examine(story, 'shed_pots','2')
                else:
                    dialog.examine(story, 'shed_pots')
            elif (e == 'crates' or e == 'Crates' or e == 'boxes' or e == 'Boxes'):
                dialog.examine(story, 'crates')
            elif (e == 'table' or e == 'Table'):
                if (story.PKSwitch[1] == True):
                    dialog.examine(story, 'shed_table','1')
                    if (story.tutorialSwitch[3] == False):
                        pickup = input('Take the hunting knife?(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nHunting Knife obtained')
                            inv.addItem(item.weapons[3], 1)
                            story.PKSwitch[1] = False
                            examining = False
                            gloss.constructs[2].unlock()
                            cont()
                else:
                    dialog.examine(story, 'shed_table')
            elif (e == 'candle' or e == 'Candle'):
                dialog.examine(story, 'candle')
            elif (e == 'mortar' or e == 'Mortar' or e == 'pestle' or e == 'Pestle'):
                if (story.sQuests[0].accepted == True and story.sQuests[0].required[2] == False):
                    for i in inv.itemList:
                        if (i['item'].itemType == ItemType.ingredient and i['item'].itemId == 1030):
                            dialog.examine(story, 'mortar', '1')
                            story.sQuests[0].required[2] = True
                            examining = False
                else:
                    dialog.examine(story, 'mortar')
                gloss.constructs[4].unlock()
            elif (e == 'knife' or e == 'Knife'):
                dialog.examine(story, 'knife')
                gloss.constructs[2].unlock()
            elif (e == 'e' or e == 'E'):
                examining = False
            elif (story.c2Switch[2] == True):
                if (e == 'sack' or e == 'Sack'):
                    dialog.examine(story, 'sack')
                    if (story.PKSwitch[5] == True):
                        print("There's a bandage inside.")
                        cont()
                        pickup = input('Take the bandage.(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nBandage obtained')
                            inv.addItem(item.items[0], 1)
                            story.PKSwitch[5] = False
                elif (e == 'bow' or e == 'Bow' or e == 'quiver' or e == 'Quiver' or e == 'arrows' or e == 'Arrows'):
                    dialog.examine(story, 'bow')
        elif (location == '5'):
            dialog.room(story, 'alder_room')
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                dialog.examine(story, 'alder_window')
            elif (e == 'bed' or e == 'Bed'):
                dialog.examine(story, 'bed')
                if (story.PKSwitch[4] == True):
                    pickup = input("Among the feathers were Alder's savings. Take them?(y/n)")
                    confirm = yn(pickup)
                    if (confirm == True):
                        coins = random.randrange(+2,+3)
                        print('\n', coins,' shillings obtained!')
                        inv.shillings(coins)
                        story.PKSwitch[4] = False
                        cont()
                if ((story.tutorialSwitch[5] == False and story.tutorialSwitch[6] == True)  or (story.c2Switch[1] == False and story.c2Switch[2] == True)):
                    sleep = input('Would you like to rest?(y/n)')
                    confirm = yn(sleep)
                    if (confirm == True):
                        dialog.examine(story, 'bed', '1')
                        if (story.tutorialSwitch[5] == False and story.tutorialSwitch[6] == True):
                            if(story.sQuests[0].accepted == True and story.sQuests[0].submitted == False):
                                ab = input('Abandon quests?(y/n)')
                                confirm = yn(ab)
                                if (confirm == True):
                                    story.sQuests[0].accepted = False
                                    print(story.sQuests[0].name,' abandoned!')
                                    story.tutorialSwitch[6] = False
                                    story.part = '1'
                                    story.switch[5] = True
                                    story.chapter = '2'
                                    examining = False
                                    bed(party)
                            else:
                                story.tutorialSwitch[6] = False
                                story.part = '1'
                                story.switch[5] = True
                                examining = False
                                story.chapter = '2'
                                bed(party)
                        else:
                            bed(party)
                            if(story.c2Switch[2] == True):
                                story.switch[7] = True
                                story.part = '3'
                                story.c2Switch[2] = False
                            examining = False
                        cont()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '6'):
            if (story.mQuests[1].accepted == True and story.mQuests[1].completed == False):
                dialog.room(story, 'woods1')
            else:
                dialog.room(story, 'woods1','1')
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                dialog.examine(story, 'sky')
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                if (story.PKSwitch[3] == True):
                    dialog.examine(story, 'mushroom','1')
                    pickup = input('Take the mushrooms?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n3 mushrooms(s) obtained')
                        inv.addItem(item.food[3], 3)
                        story.PKSwitch[3] = False
                else:
                    dialog.examine(story, 'mushroom')
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                dialog.examine(story, 'plants')
            elif (e == 'trees' or e == 'Trees'):
                dialog.examine(story, 'trees')
            elif (e == 'rocks' or e == 'Rocks' or e == 'boulder' or e == 'Boulder'):
                dialog.examine(story, 'rocks')
            elif (e == 'cottage' or e == 'Cottage'):
                dialog.examine(story, 'cottage')
            elif (e == 'cricket' or e == 'Cricket' or e == 'crickets' or e == 'Crickets'):
                if (story.mQuests[1].accepted == True and story.mQuests[1].completed == False):
                    dialog.examine(story, 'cricket')
                    fight = input('Do you want to fight them.(y/n)')
                    confirm = yn(fight)
                    if (confirm == True):
                        print('Entering battle')
                        win = False
                        com.Battle(party.listParty(), [enemyUnits.Cricket(), enemyUnits.Null(), enemyUnits.Null()],inv)
                        if(party.alder.cExp > 0):
                            dialog.examine(story, 'cricket', '1')
                            win = com.Battle(party.listParty(), [enemyUnits.Hornet(), enemyUnits.Hornet(), enemyUnits.Null()],inv)
                        elif(party.alder.cExp == 0):
                            dialog.examine(story, 'cricket', '2')
                            win =com.Battle(party.listParty(), [enemyUnits.Hornet(), enemyUnits.Hornet(), enemyUnits.Null()],inv)
                        if (win == False):
                            location = '3'
                            party.alder.health = party.alder.maxHealth
                            party.alder.stamina = party.alder.maxStamina
                            game_over = True
                            break
                        else:
                            story.tutorialSwitch[5] = False
                            dialog.examine(story, 'cricket', '3')
                        examining = False
                else:
                    dialog.examine(story, 'cricket', '4')
                gloss.invertebrates[0].unlock()
                gloss.invertebrates[1].unlock()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '7'):
            if(story.c2Switch[3] == True):
                dialog.room(story, 'scion')
            else:
                dialog.room(story, 'scion','1')
            e = input('Examine: ')
            if(e == 'trees' or e == 'Trees' or e == 'pillars' or e == 'Pillars'):
                dialog.examine(story, 'scion_trees')
            elif(e == 'ceiling' or e == 'Ceiling' or e == 'mosaic' or e == 'Mosaic' or e == 'branches' or e == 'Branches'):
                dialog.examine(story, 'scion_ceiling')
            elif(e == 'light' or e == 'Light'):
                dialog.examine(story, 'scion_light')
                examining = False
                if(story.c2Switch[3] == True):
                    story.switch[8] = True
                    story.part = '4'
            elif (e == 'e' or e == 'E'):
                examining = False
            elif(story.c2Switch[3] == False):
                if(e == 'sword' or e == 'Sword'):
                    dialog.examine(story, 'scion_sword')
                    sword = input('Take the sword!(y/n)')
                    confirm = yn(sword)
                    if(confirm == True):
                        story.switch[9] = True
                        story.part = '5'
                        examining = False
                    gloss.constructs[5].unlock()
                elif(e == 'ghosts' or e == 'Ghosts' or e == 'spectors' or e == 'Spectors'):
                    dialog.examine(story, 'scion_ghost')
                elif (e == 'e' or e == 'E'):
                    examining = False
