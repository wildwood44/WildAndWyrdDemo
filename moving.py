import itemList
import playableChars
import enemyUnits
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

def move(game_active, party, location, story, inv):
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
            print('Alder moved to the living room of the cottage.')
            party.alder.stamina -= 1
            location = '2'  
            cont()
    elif (location == '2'):
        print('1: Kitchen')
        print('2: Outside')
        print('3: Alder'"'"'s room')
        if (story.sQuests[2].required[1] == True):
            print('4: Shed')
        m = input('Move to: ')
        if (m == '1' or m == 'kitchen' or m == 'Kitchen'):
            location = '1'
            print('Alder moved to the kitchen.')
            party.alder.stamina -= 1    
            cont()
        elif (m == '2'):
            if (story.c3Switch[1] == False and story.c3Switch[2] == True and story.part == '3'):
                print('Florence:')
                print('"Wait Alder!"')
                cont()
                print('Florence:')
                print('"Keep close to me."')
                cont()
                print('Florence:')
                print('"To the window."')
                cont()
            elif (story.c3Switch[2] == False and story.c3Switch[5] == True and story.chapter == '3'):
                print('With the Gowl'"'"'s outside it wasn'"'"'t worth risking.')
            else:
                location = '3'
                if(story.c3Switch[5] == False):
                    print('The group exited the cottage through the back door.')
                else:
                    print('Alder exited the cottage through the front door.')
                party.alder.stamina -= 1
                cont()
                print
                if(story.tutorialSwitch[1] == True and story.chapter == '1'):
                    story.part = '2'
                    story.tutorialSwitch[1] = False
                    story.switch[1] = True
                    tutorial1 = False
                elif(story.c3Switch[5] == False):
                    story.switch[15] = True
                    story.c3Switch[6] = False
        elif (m == '3'):
            location = '5'
            print('Alder moved upstairs and into his bedroom.')
            party.alder.stamina -= 1    
            cont()
        elif (story.sQuests[2].required[1] == True):
            if (m == '4'):
                location = '4'
                print('Alder moved through the hole and into the shed.')
                party.alder.stamina -= 1    
                cont()
    elif (location == '3'):
        print('1: Living Room')
        print('2: Shed')
        print('3: Woods')
        m = input('Move to: ')
        if (m == '1'):
            if (story.tutorialSwitch[2] == False and story.tutorialSwitch[5] == True):
                print('Alder moved to the living room of the cottage.')    
                cont()
                print('Kyla:')
                print('"Hm!?"')
                cont()
                print('Kyla:')
                print('"What are you doing in here boy!?"')
                cont()
                print('Alder:')
                print('"Um?"')
                cont()
                print('Kyla:')
                print('"Get out there and entertain our guest!"')
                cont()
                print('Alder withdraws from the cottage.')    
                cont()
            elif (story.c2Switch[0] == True):
                location = '2'
                print('Alder moved to the living room of the cottage.')
                party.alder.stamina -= 1
                story.switch[6] = True
                story.part = '2'
            elif (story.c3Switch[2] == False and story.c3Switch[3] == True):
                location = '2'
                print('Alder moved to the living room of the cottage.')
                party.alder.stamina -= 1
                story.switch[13] = True
            else:
                location = '2'
                print('Alder moved to the living room of the cottage.')
                party.alder.stamina -= 1    
                cont()
        elif (m == '2'):        
            location = '4'
            print('Alder entered the shed at the side of the cottage.')  
            party.alder.stamina -= 1  
            cont()
        elif (m == '3'):
            if (story.mQuests[0].completed == True and party.alder.weapon1.wpId != '0'):
                location = '6'
                print('Alder left the cottage grounds.')
                party.alder.stamina -= 1    
                cont()
            else:
                print('It'"'"'s dangerous to leave the cottage grounds unarmed.')
                cont()
    elif (location == '4'):
        if (story.sQuests[2].required[1] == True):
            print('1: Living room')
        else:
            print('1: Outside')
        m = input('Move to: ')
        if (m == '1'):
            if (story.sQuests[2].required[1] == True):
                location = '2'
                print('Alder went back through the hole into the living room of the cottage.')
                party.alder.stamina -= 1
                cont()
            else:
                location = '3'
                print('Alder left the shed and returned to the front of the cottage.')
                if (party.alder.weapon1.wpId == "2"):
                    story.tutorialSwitch[4] = False
                party.alder.stamina -= 1
                cont()
    elif (location == '5'):
        print('1: Living Room')
        m = input('Move to: ')
        if (m == '1'):
            location = '2'
            if (story.chapter == '3' and story.c3Switch[0] == True):
                print('Alder jumped out of bed and hurriedly knocked on Florence'"'"'s door. She soon groggily came out.')
                cont()
                print('Florence:')
                print('*Groan*')
                cont()
                print('Florence:')
                print('"Alder, it'"'"'s really early, don’t wake me."')
                cont()
                print('Florence gave Alder an annoyed look before she noticed the sword in his hands.')
                cont()
                print('Florence:')
                print('"Alder, what is that!!"')
                cont()
                print('Alder:')
                print('"It’s a sword!"')
                cont()
                print('Florence:')
                print('"Why do you have a sword and where did it come from!"')
                cont()
                print('Alder:')
                print('"A mouse in my dreams gave it to me."')
                cont()
                print('Florence:')
                print('"What!?"')
                cont()
                print('She was confused by Alder'"'"'s response and it was clear she was sceptical.')
                cont()
                print('Kyla:')
                print('"Heh Heh."')
                cont()
                print('Kyla:')
                print('"What'"'"'s this about a sword?"')
                cont()
                print('Kyla had come out of her room somewhat amused by Florences shouts. When she looked at Alder her eyes widened as she noticed the sword that Alder had.')
                cont()
                print('Kyla:')
                print('"Boy, let me see that sword!"')
                cont()
                print('Alder:')
                print('"Um?"')
                cont()
                print('Alder:')
                print('"O-ok."')
                cont()
                print('Alder hands the sword over to Kyla and with Florences assistance she took it to the table downstairs.')
                cont()
                print('Kyla:')
                print('"It can’t be?"')
                cont()
                print('Kyla:')
                print('"Boy, in the bookshelf, there should be a blue book on magical artefacts, bring it here."')
                cont()
                print('Kyla:')
                print('"Look for the page that has this sword in it."')
                cont()
                print('Alder:')
                print('"Right."')
                story.c3Switch[0] = False
            else:
                print('Alder moved downstairs into the living room.')
            party.alder.stamina -= 1
            cont()
    elif (location == '6'):
        print('1: Cottage grounds')
        print('2: Deep Woods')
        m = input('Move to: ')
        if (m == '1'):
            location = '3'
            if(story.tutorialSwitch[5] == False):
                print('Alder:')
                print('"Florence! I'"'"'m done!"')
                cont()
                print('Florence was having a conversation with Thay. When they looked at Alder they immediately noticed the swollen red marks where the hornets had stung his exposed skin.')
                cont()
                print('Florence:')
                print('"Alder what happened? Are you ok!?"')
                cont()
                print('Alder:')
                print('"Um..."')
                cont()
                print('Alder was briefly suprised by Florence'"'"'s concern, but he knew she could get paranoid when it can to his safety.')
                cont()
                print('Alder:')
                print('"I got stung by hornets a few times but I'"'"'m alright!"')
                cont()
                print('Florence:')
                print('*Sigh*')
                cont()
                print('Florence:')
                print('"Give the bugs and the knife to me and go relax yourself."')
                cont()
                print('Thay:')
                print('"Here some plantain might ease your discomfort."')
                cont()
                print('Alder passed the bug meat and the hunting knife over to her. Florence went inside the cottage to prepare the crickets for supper while Thay applied poultice of greater plantain to Alder stings.')
                for i in inv.itemList:
                    if (i['item'].itemType == ItemType.food):
                        if (i['item'].itemId == '5'):
                            inv.removeItem(i)
                party.alder.weapon1 = item.weapons[0]
                party.alder.health += 10
                print('\nHunting Knife unequipped')
                cont()
                story.mQuests[0].qComp(party, inv)
                story.mQuests[1].qComp(party, inv)
                story.part = '4'
                story.switch[4] = True
            party.alder.stamina -= 1
        elif (m == '2'):
            print('Alder once got lost after he strayed too far from the cottage.')
            cont()
            print('He spent hours in the dark until Florence found him crying and scared.')
            cont()
            print('Kyla had been indifferent to the incident.')
            cont()
    elif (location == '7'):
        print('Alder could not move.')
    return location
