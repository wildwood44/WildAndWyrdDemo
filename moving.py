import itemList
import playableChars
import enemyUnits
import dialog
from data import typeSpf
item = itemList
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

def move(game_active, party, location, story, inv, gloss):
    print('\nMove')
    for i in locations:
        if (location == i['locId']):
            print('Currently:',i['name'])
    if (location == '1'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            if(story.tutorialSwitch[0] == True):
                story.tutorialSwitch[0] = False
            dialog.move(story, location, m)
            party.alder.stamina -= 1
            location = '2'
    elif (location == '2'):
        print('1: Kitchen')
        print('2: Outside')
        print('3: Alder'"'"'s room')
        if (story.sQuests[2].required[1] == True):
            print('4: Shed')
        m = input('Move to: ')
        if (m == '1' or m == 'kitchen' or m == 'Kitchen'):
            dialog.move(story, location, m)
            location = '1'
            party.alder.stamina -= 1
        elif (m == '2'):
            if (story.c3Switch[1] == False and story.c3Switch[2] == True and story.part == '3'):
                dialog.move(story, location, m, '1')
            elif (story.c3Switch[2] == False and story.c3Switch[5] == True and story.chapter == '3'):
                dialog.move(story, location, m, '2')
            else:
                if(story.c3Switch[5] == False):
                    dialog.move(story, location, m, '3')
                else:
                    dialog.move(story, location, m)
                location = '3'
                party.alder.stamina -= 1
                if(story.tutorialSwitch[1] == True and story.chapter == '1'):
                    story.part = '2'
                    story.tutorialSwitch[1] = False
                    story.switch[1] = True
                    tutorial1 = False
                    gloss.folklore[0].unlock()
                elif(story.c3Switch[5] == False):
                    story.switch[15] = True
                    story.c3Switch[6] = False
        elif (m == '3'):
            dialog.move(story, location, m)
            location = '5'
            party.alder.stamina -= 1
        elif (story.sQuests[2].required[1] == True):
            if (m == '4'):
                dialog.move(story, location, m)
                location = '4'
                party.alder.stamina -= 1    
    elif (location == '3'):
        print('1: Living Room')
        print('2: Shed')
        print('3: Woods')
        m = input('Move to: ')
        if (m == '1'):
            if (story.tutorialSwitch[2] == False and story.tutorialSwitch[5] == True):
                dialog.move(story, location, m, '1')
            elif (story.c2Switch[0] == True):
                dialog.move(story, location, m)
                location = '2'
                party.alder.stamina -= 1
                if (story.tutorialSwitch[6] == False):
                    story.switch[6] = True
                    story.part = '2'
            elif (story.c3Switch[2] == False and story.c3Switch[3] == True):
                dialog.move(story, location, m)
                location = '2'
                party.alder.stamina -= 1
                story.switch[13] = True
            else:
                dialog.move(story, location, m)
                location = '2'
                party.alder.stamina -= 1    
        elif (m == '2'):
            dialog.move(story, location, m)      
            location = '4'
            party.alder.stamina -= 1  
        elif (m == '3'):
            if (story.mQuests[0].completed == True and party.alder.weapon1.wpId != 1008):
                dialog.move(story, location, m)
                location = '6'
                party.alder.stamina -= 1    
            else:
                dialog.move(story, location, m, '1')
    elif (location == '4'):
        if (story.sQuests[2].required[1] == True):
            print('1: Living room')
        else:
            print('1: Outside')
        m = input('Move to: ')
        if (m == '1'):
            if (story.sQuests[2].required[1] == True):
                dialog.move(story, location, m, '1')
                location = '2'
                party.alder.stamina -= 1
            else:
                dialog.move(story, location, m)
                location = '3'
                if (party.alder.weapon1.wpId == 1010):
                    story.tutorialSwitch[4] = False
                party.alder.stamina -= 1
    elif (location == '5'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            if (story.chapter == '3' and story.c3Switch[0] == True):
                dialog.move(story, location, m, '1')
                story.c3Switch[0] = False
            else:
                dialog.move(story, location, m)
            location = '2'
            party.alder.stamina -= 1
    elif (location == '6'):
        print('1: Cottage grounds')
        print('2: Deep Woods')
        m = input('Move to: ')
        if (m == '1'):
            if(story.tutorialSwitch[5] == False):
                dialog.move(story, location, m, '1')
                for i in inv.itemList:
                    if (i['item'].itemType == ItemType.food):
                        if (i['item'].itemId == 1005):
                            inv.removeItem(i)
                party.alder.weapon1 = item.weapons[0]
                party.alder.health += 10
                print('\nHunting Knife unequipped')
                cont()
                story.mQuests[0].qComp(party, inv)
                story.mQuests[1].qComp(party, inv)
                story.part = '4'
                story.switch[4] = True
                gloss.plants[1].unlock()
            else:
                dialog.move(story, location, m)
            party.alder.stamina -= 1
            location = '3'
        elif (m == '2'):
            dialog.move(story, location, m)
    elif (location == '7'):
        dialog.move(story, location, '0')
    return location
