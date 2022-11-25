import itemList
import combat
import playableChars
import enemyUnits
import shop
import dialog
item = itemList
com = combat
shop = shop.Shop()

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

def talk(game_active, party, location, story, inv, gloss):
    #global story, tutorial1
    print('\nTalk')
    if (location == '1'):
        if (story.tutorialSwitch[5] == False and story.chapter == '1'):
            print('1: Florence')
            t = input('Talk to: ')
            if (t == '1'):
                if(party.alder.health < party.alder.maxHealth):
                    dialog.talk(story, '6', t)
                    party.alder.health = party.alder.maxHealth
                elif(party.alder.health == party.alder.maxHealth):
                    dialog.talk(story, '6', t+'.1')
        else:
            print('There was no one to talk to.')
    elif (location == '2'):
        if (story.tutorialSwitch[5] == False and story.chapter == '1'):
            if (story.sQuests[0].accepted != True):
                print('1: Kyla(!)')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog.talk(story, 'q0', '1')
                    i = input('Do you accept this labour?(y/n):')
                    confirm = yn(i)
                    if(confirm == True):
                        dialog.talk(story, 'q0', '1.1')
                        story.sQuests[0].accepted = True
                    else:
                        dialog.talk(story, 'q0', '1.2')
                        story.sQuests[0].accepted = True
            else:
                print('1: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.sQuests[0].completed != True):
                        dialog.talk(story, 'q0', '2')
                    elif (story.sQuests[0].completed == True and story.sQuests[0].submitted != True):
                        dialog.talk(story, 'q0', '2.1')
                        story.sQuests[0].qComp(party, inv)
                    else:
                        dialog.talk(story, 'q0', '2.2')
        elif (story.c2Switch[1] == False and story.chapter == '2'):
            print('1: Florence')
            print('2: Kyla')
            t = input('Talk to: ')
            if (t == '1'):
                dialog.talk(story, '2', t)
            elif (t == '2'):
                dialog.talk(story, '2', t)
        elif (story.c2Switch[0] == False and story.chapter == '2'):
            print('1: Florence')
            print('2: Kyla')
            t = input('Talk to: ')
            if (t == '1'):
                dialog.talk(story, '1', t)
            elif (t == '2'):
                dialog.talk(story, '1', t)
        elif (story.chapter == '3'):
            #print(c3Switch)
            if(story.c3Switch[1] == True):
                print('1: Florence')
                print('2: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog.talk(story, '1', t)
                elif (t == '2'):
                    dialog.talk(story, '1', t)
            elif(story.c3Switch[2] == True):
                print('1: Florence')
                print('2: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog.talk(story, '2', t)
                elif (t == '2'):
                    dialog.talk(story, '2', t)
            elif(story.c3Switch[6] == True):
                if (story.sQuests[1].accepted != True):
                    print('1: Florence(!)')
                else:
                    print('1: Florence')
                if (story.sQuests[2].accepted != True):
                    print('2: Kyla(!)')
                else:
                    print('2: Kyla')
                if(story.c3Switch[3] == False and story.c3Switch[4] == True):
                    print('3: Weasel')
                elif(story.c3Switch[4] == False and story.c3Switch[5] == True):
                    print('3: Jeb')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.sQuests[1].accepted != True):
                        dialog.talk(story, 'q1', '1')
                        story.sQuests[1].accepted = True
                    elif(story.sQuests[1].completed != True):
                        dialog.talk(story, 'q1', '2')
                    elif(story.sQuests[1].submitted != True):
                        dialog.talk(story, 'q1', '3')
                        story.sQuests[1].qComp(party, inv)
                    else:
                        dialog.talk(story, '6', t)
                elif (t == '2'):
                    if (story.sQuests[2].accepted != True):
                        dialog.talk(story, 'q2', '1')
                        story.sQuests[2].accepted = True
                    elif(story.sQuests[2].completed != True):
                        dialog.talk(story, 'q2','2')
                    elif(story.sQuests[2].submitted != True):
                        dialog.talk(story, 'q2', '3')
                        story.sQuests[2].qComp(party, inv)
                    else:
                        dialog.talk(story, '6', t)
                if(story.c3Switch[3] == False and story.c3Switch[4] == True):
                    if (t == '3'):
                        story.switch[13] = True
                elif(story.c3Switch[4] == False and story.c3Switch[5] == True):
                    if (t == '3'):
                        print('Jeb:')
                        print('"What would you like Scion?"')
                        cont()
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
        else:
            print('There was no one to talk to.')
    elif (location == '3'):
        if (story.chapter == '1'):
            if (story.tutorialSwitch[2] == True):
                print('1: Florence')
                t = input('Talk to: ')
                if (t == '1'):
                    options = [False, False]
                    while(options[0] == False or options[1] == False):
                        print('1: "So what'"'"'s Thay here for?"')
                        print('2: "How does the magic around the cottage work again?"')
                        c = input('Alder: ')
                        if (c == '1'):
                            dialog.talk(story, '2', c)
                            options[0] = True
                        if (c == '2'):
                            dialog.talk(story, '2', c)
                            options[1] = True
                    story.switch[2] = True
                    story.tutorial1 = False
                    story.tutorialSwitch[2] = False
            elif (story.tutorialSwitch[3] == True):
                print('1: Thay')
                t = input('Talk to: ')
                if (t == '1'):
                    options = [False, False, False]
                    options2 = [False, False, False, False, False]
                    while(options[0] == False or options[1] == False or options2[4] == False):
                        print('1: "How was your journey?"')
                        print('2: "How did it go with Madame Kyla?"')
                        print('3: "What'"'"'s it like beyond the burrow?"')
                        if (options[2] == True):
                            print('4: What can you tell me about the woods?')
                            print('5: What can you tell me about the the mouse village?')
                            print('6: What can you tell me about the river?')
                            print('7: What can you tell me about the hill?')
                            print('8: Why are humans so hated?')
                        c = input('Alder: ')
                        if (c == '1'):
                            dialog.talk(story, '3', c)
                            options[0] = True
                        if (c == '2'):
                            dialog.talk(story, '3', c)
                            options[1] = True
                        if (c == '3'):
                            dialog.talk(story, '3', c)
                            options[2] = True
                        if (options[2] == True):
                            if (c == '4'):
                                dialog.talk(story, '3', c)
                                options2[0] = True
                            if (c == '5'):
                                dialog.talk(story, '3', c)
                                options2[1] = True
                            if (c == '6'):
                                dialog.talk(story, '3', c)
                                options2[2] = True
                            if (c == '7'):
                                dialog.talk(story, '3', c)
                                options2[3] = True
                            if (c == '8'):
                                dialog.talk(story, '3', c)
                                options2[4] = True
                    story.switch[3] = True
                    story.part = '3'
                    story.tutorialSwitch[3] = False
                    story.tutorial1 = False
            elif (story.tutorialSwitch[4] == True):
                print('1: Florence')
                t = input('Talk to: ')
                if (t == '1'):
                    options = [False]
                    while(options[0] == False):
                        dialog.talk(story, '4')
                        options[0] = True
            elif (story.tutorialSwitch[5] == True):
                print('1: Florence')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.mQuests[0].completed == True):
                        options = [False, False]
                        while(options[0] == False and options[1] == False):                    
                            print('1: "I have the knife!"')                  
                            print('2: "Nevermind"')
                            c = input('Alder: ')
                            if (c == '1'): 
                                dialog.talk(story, '5')
                                options[0] = True
                            if (c == '2'):
                                options[1] = True
            
            else:
                print('There was no one to talk to.')
        elif(story.chapter == '2'):
            if (story.c2Switch[0] == False and story.c2Switch[1] == True):
                print('1: Trissie')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog.talk(story, '1', '3')
                    party.alder.weapon2 = item.weapons[9]
                    print('\nTraining bow equipped')
                    inv.addItem(item.projec[0], 5)
                    print('\n5 Primitive arrows obtained')
                    cont()
                    dialog.talk(story, '1', '3.1')
                    com.Battle(party.listParty(), [enemyUnits.Dummy(), enemyUnits.Null(), enemyUnits.Null()],inv)
                    if (party.alder.health > 0 or game_active == True):
                        dialog.talk(story, '1', '3.2')
                        options = [False, False]
                        while(options[0] == False and options[1] == False):
                            print('1: "What are the Gowls like?"')
                            print('2: "Will we see each other again soon?"')
                            c = input('Alder: ')
                            if (c == '1'):
                                dialog.talk(story, '1', '3.3')
                                story.branchSwitch[0] = '1'
                                options[0] = True
                            elif (c == '2'):
                                dialog.talk(story, '1', '3.4')
                                story.branchSwitch[0] = '2'
                                options[1] = True
                        dialog.talk(story, '1', '3.5')
                        story.c2Switch[1] = False
            else:
                print('There was no one to talk to.')
                    
    elif(location == '7'):
        if(story.c2Switch[3] == False):
            print('1: Mouse')
            t = input('Talk to: ')
            if (t == '1'):
                dialog.talk(story, '3', t)
        else:
            print('There was no one to talk to.')
    else:
        print('There was no one to talk to.')
