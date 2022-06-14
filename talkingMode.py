import itemList
item = itemList

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

def talk(game_active, party, location, story, inv):
    #global story, tutorial1
    print('\nTalk')
    if (location == '1'):
        if (story.tutorialSwitch[5] == False and story.chapter == '1'):
            print('1: Florence')
            t = input('Talk to: ')
            if (t == '1'):
                if(alder.health < alder.maxHealth):
                    print('Florence:')
                    print('"You look worse for wear."')
                    cont()
                    print('Florence:')
                    print('"Hold still, I'"'"'ll help fix you up."')
                    cont()
                    alder.health = alder.maxHealth
                    print('Alder:')
                    print('"Thank you."')
                    cont()
                elif(alder.health == alder.maxHealth):
                    print('Florence:')
                    print('"You look tired."')
                    cont()
                    print('Florence:')
                    print('"Take a nap, you'"'"'ll feel better."')
                    cont()
        else:
            print('There was no one to talk to.')
    elif (location == '2'):
        if (story.tutorialSwitch[5] == False and story.chapter == '1'):
            if (story.sQuests[0]['accepted'] != True):
                print('1: Kyla(!)')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Madam Kyla was relaxed in her chair with her nose in a red book titled "A sorcerers guide to Dragons and Wyverns". She peered from the book to Alder.')
                    cont()
                    print('Kyla:')
                    print('"I take it Mr Prickle has gone?"')
                    cont()
                    print('Alder:')
                    print('"Yes, Madam."')
                    cont()
                    print('Kyla:')
                    print('"Making you free boy?"')
                    cont()
                    print('Alder:')
                    print('"Yes, Madam."')
                    cont()
                    print('Kyla:')
                    print('"Then clean the fireplace, wash the cauldron in the kitchen and..."')
                    cont()
                    print('Kyla:')
                    print('"Ah!"')
                    cont()
                    print('Kyla:')
                    print('"I need you to grind some bramble leaves."')
                    cont()
                    print('Kyla:')
                    print('"Use the mortar in the shed to grind them into dust."')
                    cont()
                    print('Kyla:')
                    print('"Leave the dust in the pot on the far end next to the shed table."')
                    cont()
                    print('Kyla:')
                    print('"That should keep you busy!"')
                    cont()
                    i = input('Do you accept this labour?(y/n):')
                    confirm = yn(i)
                    if(confirm == True):
                        print('Alder:')
                        print('"Yes, Madam."')
                        cont()
                        print('Kyla:')
                        print('"Excellent!"')
                        cont()
                        print('Alder accepted the chores')
                        story.sQuests[0]['accepted'] = True
                        cont()
                    else:
                        print('Alder:')
                        print('"..."')
                        cont()
                        print('Kyla:')
                        print('"Don'"'"'t you glare at me!"')
                        cont()
                        print('Kyla:')
                        print('"Work for your sanctuary!"')
                        cont()
                        print('Kyla:')
                        print('"I'"'"'m not permitting you here out of charity!"')
                        cont()
                        print('Kyla:')
                        print('"Work for your sanctuary!"')
                        cont()
                        print('Alder:')
                        print('"U-Um."')
                        cont()
                        print('Alder:')
                        print('"Y-Yes!"')
                        cont()
                        print('Alder:')
                        print('"Sorry madam."')
                        cont()
                        print('Alder knew better than to argue back. Alder accepted the chores.')
                        story.sQuests[0]['accepted'] = True
                        cont()
            else:
                print('1: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.sQuests[0]['completed'] != True):
                        print('Kyla:')
                        print('"Clean the fireplace, scrub the cauldron and grind the leaves."')
                        cont()
                        print('Kyla:')
                        print('"Those are your duties for the day."')
                        cont()
                    elif (story.sQuests[0]['completed'] == True and story.sQuests[0]['submitted'] != True):
                        print('Kyla:')
                        print('"Have you finished then?"')
                        cont()
                        print('Alder:')
                        print('"Yes madam."')
                        cont()
                        print('Kyla:')
                        print('"Good."')
                        cont()
                        story.sQuests[0]['submitted'] = True
                        print('Kyla:')
                        print('"I have no futher need for you."')
                        cont()
                        print('Kyla:')
                        print('"Do as you please."')
                        cont()
                        qComp(story.sQuests[0])
                    else:
                        print('Kyla:')
                        print('"I have no futher need for you."')
                        cont()
                        print('Kyla:')
                        print('"Do as you please."')
                        cont()
        elif (story.c2Switch[1] == False and story.chapter == '2'):
            print('1: Florence')
            print('2: Kyla')
            t = input('Talk to: ')
            if (t == '1'):
                print('Florence:')
                print('"Don'"'"'t go too far from now on."')
                cont()
                print('Florence:')
                print('"I don'"'"'t want you getting caught."')
                cont()
            elif (t == '2'):
                print('Kyla:')
                print('"They will never find this cottage."')
                cont()
                print('Kyla:')
                print('"Needless worry."')
                cont()
        elif (story.c2Switch[2] == False and story.chapter == '2'):
            print('1: Florence')
            print('2: Kyla')
            t = input('Talk to: ')
            if (t == '1'):
                print('Florence:')
                print('"Triss is very brave."')
                cont()
                print('Florence:')
                print('"She risks everything to help people get around the Gowls."')
                cont()
            elif (t == '2'):
                print('Kyla:')
                print('"I like the girl."')
                cont()
                print('Kyla:')
                print('"Shame she never stays."')
                cont()
        elif (story.chapter == '3'):
            #print(c3Switch)
            if(story.c3Switch[1] == True):
                print('1: Florence')
                print('2: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Florence:')
                    print('"I think we will need to have a long discussion about that sword Alder."')
                    cont()
                elif (t == '2'):
                    print('Kyla:')
                    print('"The book is called "Magical thing of history"."')
                    cont()
                    print('Kyla:')
                    print('"Go get it."')
                    cont()
            elif(story.c3Switch[2] == True):
                print('1: Florence')
                print('2: Kyla')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Florence:')
                    print('"I'"'"'ve never heard that voice before."')
                    cont()
                    print('Florence:')
                    print('"Check the window."')
                    cont()
                elif (t == '2'):
                    print('Kyla:')
                    print('"Hmm."')
                    cont()
            elif(story.c3Switch[6] == True):
                if (story.sQuests[1]['accepted'] != True):
                    print('1: Florence(!)')
                else:
                    print('1: Florence')
                if (story.sQuests[2]['accepted'] != True):
                    print('2: Kyla(!)')
                else:
                    print('2: Kyla')
                if(story.c3Switch[3] == False and story.c3Switch[4] == True):
                    print('3: Weasel')
                elif(story.c3Switch[4] == False and story.c3Switch[5] == True):
                    print('3: Jeb')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.sQuests[1]['accepted'] != True):
                        print('Alder:')
                        print('"What the matter Florence?."')
                        cont()
                        print('Florence:')
                        print('"We need food supplies to get to Forton!"')
                        cont()
                        print('Alder:')
                        print('"Like what?"')
                        cont()
                        print('Florence:')
                        print('"Take what you can from the larder."')
                        cont()
                        story.sQuests[1]['accepted'] = True
                    elif(story.sQuests[1]['completed'] != True):
                        print('Florence:')
                        print('"I wish we were better prepaired, but there'"'"'s nothing we can do about it"')
                        cont()
                    elif(story.sQuests[1]['submitted'] != True):
                        print('Alder:')
                        print('"This was all there was."')
                        cont()
                        print('Alder:')
                        print('"Will it be enough?"')
                        cont()
                        print('Florence:')
                        print('"I hope so."')
                        cont()
                        print('Florence:')
                        print('"Thank you, Alder."')
                        cont()
                        story.sQuests[1]['submitted'] = True
                        qComp(story.sQuests[1])
                    else:
                        print('Florence:')
                        print('"Are you doing alright Alder?"')
                        cont()
                        print('Alder:')
                        print('"Fine."')
                        cont()
                        print('Alder:')
                        print('"But are you sure you want to give up your apprenticeship?"')
                        cont()
                        print('Florence:')
                        print('"I'"'"'m not leaving you Alder!"')
                        cont()
                        print('Florence:')
                        print('"I'"'"'ll protect you no matter what!"')
                        cont()
                elif (t == '2'):
                    if (story.sQuests[2]['accepted'] != True):
                        print('Kyla:')
                        print('"Boy, gather my books from the bookshelf and the pots of ingredients from the shed and bring them here."')
                        cont()
                        print('Alder:')
                        print('"But the rat is outside, how do I get to the shed?"')
                        cont()
                        print('Kyla:')
                        print('"You will have to break down the '"'wall'"'."')
                        cont()
                        print('Kyla:')
                        print('"He'"'"'ll never hear it with my sound nullifying spell."')
                        cont()
                        print('Kyla:')
                        print('"Don'"'"'t concern yourself with any mess we need to get those valuables out safely."')
                        cont()
                        story.sQuests[2]['accepted'] = True
                    elif(story.sQuests[2]['completed'] != True):
                        print('Kyla:')
                        print('"I need the books from the shelves and the pots from the shed."')
                        cont()
                    elif(story.sQuests[2]['submitted'] != True):
                        print('Kyla:')
                        print('"Excellent!"')
                        cont()
                        print('Kyla:')
                        print('"Get them in the bag!"')
                        cont()
                        print('Kyla pulled out a bag and with Alder'"'"'s assistance placed the books and pots inside it one by one. The bag itself never got any larger or heavier while the pile gradually disappeared.')
                        cont()
                        print('Kyla:')
                        print('"Finish getting ready."')
                        cont()
                        print('Kyla:')
                        print('"We leave soon."')
                        cont()
                        story.sQuests[2]['submitted'] = True
                        qComp(story.sQuests[2])
                    else:
                        print('Kyla:')
                        print('"I was sloppy!"')
                        cont()
                        print('Kyla:')
                        print('"I should have arranged an escape route the moment Trissie told us about the Gowls!"')
                        cont()
                        print('Kyla:')
                        print('"Still, I don'"'"'t like that they knew our password."')
                        cont()
                        print('Kyla:')
                        print('"Someone must have snitched..."')
                        cont()
                if(story.c3Switch[3] == False and story.c3Switch[4] == True):
                    if (t == '3'):
                        story.switch[13] = True
                elif(story.c3Switch[4] == False and story.c3Switch[5] == True):
                    if (t == '3'):
                        print('Jeb:')
                        print('"What would you like Scion?"')
                        cont()
                        shop('Jeb')
                        if ((story.sQuests[1]['accepted'] == True and story.sQuests[1]['submitted'] != True) or (story.sQuests[2]['accepted'] == True and story.sQuests[2]['submitted'] != True)):
                            ab = input('Abandon quests?(y/n)')
                            confirm = yn(ab)
                            if (confirm == True):
                                if (story.sQuests[1]['accepted'] == True and story.sQuests[1]['submitted'] != True):
                                    story.sQuests[1]['accepted'] = False
                                    print(story.sQuests[1]['name'],' abandoned!')
                                if (story.sQuests[2]['accepted'] == True and story.sQuests[2]['submitted'] != True):
                                    story.sQuests[2]['accepted'] = False
                                    print(story.sQuests[1]['name'],' abandoned!')
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
                    dialog = [False, False]
                    while(dialog[0] == False or dialog[1] == False):
                        print('1: "So what'"'"'s Thay here for?"')
                        print('2: "How does the magic around the cottage work again?"')
                        c = input('Alder: ')
                        if (c == '1'):
                            print('Florence:')
                            print('"Potions probably."')
                            cont()
                            print('Florence:')
                            print('"He usually comes here for sanctuary or potions."')
                            cont()
                            dialog[0] = True
                        if (c == '2'):
                            print('Florence:')
                            print('"Well."')
                            cont()
                            print('Florence:')
                            print('"Kyla’s cast several illusions on the cottage, one of which makes it looks like a boulder from the outside."')
                            cont()
                            print('Florence:')
                            print('"She'"'"'s also muted the rooms and made our scents smell somewhat grassy."')
                            cont()
                            print('Florence:')
                            print('"This place cannot be seen from the outside world, so we tend to call it the burrow."')
                            cont()
                            dialog[1] = True
                    story.switch[2] = True
                    story.tutorial1 = False
                    story.tutorialSwitch[2] = False
            elif (story.tutorialSwitch[3] == True):
                print('1: Thay')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog = [False, False, False]
                    dialog2 = [False, False, False, False, False]
                    while(dialog[0] == False or dialog[1] == False or dialog2[4] == False):
                        print('1: "How was your journey?"')
                        print('2: "How did it go with Madame Kyla?"')
                        print('3: "What'"'"'s it like beyond the burrow?"')
                        if (dialog[2] == True):
                            print('4: What can you tell me about the woods?')
                            print('5: What can you tell me about the the mouse village?')
                            print('6: What can you tell me about the river?')
                            print('7: What can you tell me about the hill?')
                            print('8: Why are humans so hated?')
                        c = input('Alder: ')
                        if (c == '1'):
                            print('Thay:')
                            print('"It was quite lovely."')
                            cont()
                            print('Thay:')
                            print('"This summer has been good to us all."')
                            cont()
                            dialog[0] = True
                        if (c == '2'):
                            print('Thay:')
                            print('"The usual, gave her the herbs she wanted in exchange for the potions I need."')
                            cont()
                            print('Thay reached into his bag and pulled out a vial of black liquid. Phantom Cloak; a magic potion that erased a creature’s presence when in darkness. It was one of the many potions that brought patrons to the cottage. Alder never asked what they needed them for.')
                            cont()
                            dialog[1] = True
                        if (c == '3'):
                            print('Thay:')
                            print('"Well, to the north, there are more woodlands."')
                            cont()
                            print('Thay:')
                            print('"But to the south is the settlement in the valley where mice and other small beasts live."')
                            cont()
                            print('Thay:')
                            print('"West you’ll run into the river and if you climb to the treetops you can see Hare Hill east from here."')
                            cont()
                            print('Thay:')
                            print('"Wait!?"')
                            cont()
                            print('Seeing growing interest and curiosity on Alder'"'"'s face, Thay abruptly began to show concern.')
                            cont()
                            print('Thay:')
                            print('"Alder, you aren'"'"'t thinking of going to these places are you!?"')
                            cont()
                            print('Alder:')
                            print('"I..."')
                            cont()
                            print('Alder:')
                            print('"think, it would be nice to see new places."')
                            cont()
                            print('Thay:')
                            print('"No!"')
                            cont()
                            print('Thay:')
                            print('"NO!! Alder!"')
                            cont()
                            print('Thay:')
                            print('"It’s too dangerous!!"')
                            cont()
                            print('Thay:')
                            print('"If anyone sees you, you will be killed!!"')
                            cont()
                            print('Thay:')
                            print('"I cannot even express how much humans are hated these days!!"')
                            cont()
                            print('Alder:')
                            print('"Ok! Ok!"')
                            cont()
                            print('Alder:')
                            print('"I won’t go wandering!!"')
                            cont()
                            print('Alder:')
                            print('"I'"'"'m sorry!"')
                            cont()
                            print('Thay:')
                            print('"I hope not!"')
                            cont()
                            print('Thay:')
                            print('"I’d never forgive myself if anything were to happen to you."')
                            cont()
                            print('Alder realised that the hedgehog was getting agitated and so decided to move on.')
                            cont()
                            dialog[2] = True
                        if (dialog[2] == True):
                            if (c == '4'):
                                print('Thay:')
                                print('"Oldwyrm woods is where we are right now."')
                                cont()
                                print('Thay:')
                                print('"This ancient woodland goes on for miles."')
                                cont()
                                print('Thay:')
                                print('"There are many birds in these woods and unfortunately that includes birds of prey, but most go after small creatures so you'"'"'ll be alright."')
                                cont()
                                dialog2[0] = True
                            if (c == '5'):
                                print('Alder:')
                                print('"It’s not that I want to go there, I’d just like to know."')
                                cont()
                                print('Thay:')
                                print('"It’s called Forton."')
                                cont()
                                print('Thay:')
                                print('"It’s known for its great library, taking in orphans within the region and being the resting place of the hero, Agrimus."')
                                cont()
                                print('Thay:')
                                print('"It is also one of the few mouse settlements that is not controlled by the woodland church."')
                                cont()
                                dialog2[1] = True
                            if (c == '6'):
                                print('Alder:')
                                print('"Florence and I sometimes go there to get water."')
                                cont()
                                print('Alder:')
                                print('"With caution of course."')
                                cont()
                                print('Alder:')
                                print('"We caught a fish in our bucket once."')
                                cont()
                                print('Thay:')
                                print('"Hmm. You sure that’s safe?"')
                                cont()
                                print('Thay:')
                                print('"There are many creatures drifting on the river."')
                                cont()
                                print('Thay:')
                                print('"Swimming in it too."')
                                cont()
                                print('Alder:')
                                print('"It’s alright."')
                                cont()
                                print('Alder:')
                                print('"Florence has always kept us hidden."')
                                cont()
                                print('Thay:')
                                print('"Err, ok then."')
                                cont()
                                dialog2[2] = True
                            if (c == '7'):
                                print('Alder:')
                                print('"It’s not that I want to go there, I’d just like to know."')
                                cont()
                                print('Thay:')
                                print('"Hare Hill is the largest hill in the region."')
                                cont()
                                print('Thay:')
                                print('"It is home to many hare and rabbit villages."')
                                cont()
                                print('Thay:')
                                print('"At the top is the capital, Breabuck."')
                                cont()
                                print('Thay:')
                                print('"But it is a difficult and exhausting hike. Some routes lead to rock walls travelers need to scramble up."')
                                cont()
                                print('Thay:')
                                print('"Unless they go through the rabbits tunnels."')
                                cont()
                                print('Thay:')
                                print('"Oh! Nevermind."')
                                cont()
                                print('Alder:')
                                print('"What?"')
                                cont()
                                print('Thay:')
                                print('"Just. Nevermind."')
                                cont()
                                dialog2[3] = True
                            if (c == '8'):
                                print('Thay:')
                                print('"Well. There was a certain king who did very, very bad things."')
                                cont()
                                print('Alder:')
                                print('"What kinds of things?"')
                                cont()
                                print('Thay:')
                                print('"Things you'"'"'re too young to hear."')
                                cont()
                                print('Thay:')
                                print('"But all you need to know is that he was cruel and unforgivable."')
                                cont()
                                print('Thay:')
                                print('"So unforgivable in fact that along with his followers, woodland folk even took vengeance on the humans who did not support him."')
                                cont()
                                print('Alder:')
                                print('"But why?"')
                                cont()
                                print('Alder:')
                                print('"What did they do?"')
                                cont()
                                print('Thay:')
                                print('"Nothing."')
                                cont()
                                print('Thay:')
                                print('"But that didn’t matter to those who had lost friends and family in the conflict."')
                                cont()
                                print('Thay:')
                                print('"Best for you to stay within the burrows borders young one."')
                                cont()
                                print('Thay:')
                                print('"If you are seen."')
                                cont()
                                print('Thay:')
                                print('"You will be assumed aligned with the kings ideals and killed."')
                                cont()
                                print('Alder gave a sad longing look to the deep wood. He’d like to see more than the tiny patch he called home. But alas as Thay said, the danger was too great.')
                                cont()
                                dialog2[4] = True
                    story.switch[3] = True
                    story.part = '3'
                    story.tutorialSwitch[3] = False
                    story.tutorial1 = False
            elif (story.tutorialSwitch[4] == True):
                print('1: Florence')
                t = input('Talk to: ')
                if (t == '1'):
                    dialog = [False]
                    while(dialog[0] == False):
                        print('Florence:')
                        print('"The knife should be in the shed. You can go once you'"'"'ve got it."')
                        cont()
                        dialog[0] = True
            elif (story.tutorialSwitch[5] == True):
                print('1: Florence')
                t = input('Talk to: ')
                if (t == '1'):
                    if (story.mQuests[0]['accepted'] == True and story.mQuests[0]['completed'] == False):
                        dialog = [False, False]
                        while(dialog[0] == False and dialog[1] == False):                    
                            print('1: "I have the knife!"')                  
                            print('2: "Nevermind"')
                            c = input('Alder: ')
                            if (c == '1'): 
                                print('Florence:')
                                print('"Fantastic!"')
                                cont()
                                print('Florence:')
                                print('"Just please don'"'"'t go too far."')
                                cont()
                                dialog[0] = True
                            if (c == '2'):
                                dialog[1] = True
            
            else:
                print('There was no one to talk to.')
        elif(story.chapter == '2'):
            if (story.c2Switch[0] == False and story.c2Switch[1] == True):
                print('1: Trissie')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Trissie quickly set up a makeshift dummy out of leaves, sticks and a cheaply made old burlap sack that was intended for foraging before planting it in the ground so it would stand upright. The finished product was crude and clearly rushed, but would make a good target.')
                    cont()
                    print('Trissie:')
                    print('"That'"'"'ll do."')
                    cont()
                    print('Trissie:')
                    print('"Alder, wait there."')
                    cont()
                    print('Trissie went into the shed and retrived a bow and some arrows set aside for hunting. Alder thought she looked a little silly dragging the bow which was big even for him. The bow was originally meant for Florence, but finding herself unskilled she never used it. Trissie handed them to Alder.')
                    cont()
                    alder.weapon2 = weapons[3]
                    print('\nTraining bow equipped')
                    itemCount(projec[0], 5)
                    print('\n5 Primitive arrows obtained')
                    print('Trissie:')
                    print('"Now set the arrow in the bow, take aim and fire."')
                    cont()
                    print('Trissie:')
                    print('"Let'"'"'s begin."')
                    cont()
                    battle([enemyUnits.Dummy(), Null(), Null()])
                    if (alder.health > 0 or game_active == True):
                        print('Trissie:')
                        print('"Nice shot!"')
                        cont()
                        print('Trissie:')
                        print('"But it will be hard for me to leave these woods if I stay any longer!"')
                        cont()
                        print('Alder:')
                        print('"There’s one more thing I’d like to know Triss."')
                        cont()
                        print('Trissie:')
                        print('"Yes?"')
                        cont()
                        dialog = [False, False]
                        while(dialog[0] == False and dialog[1] == False):
                            print('1: "What are the Gowls like?"')
                            print('2: "Will we see each other again soon?"')
                            c = input('Alder: ')
                            if (c == '1'):
                                print('Trissie:')
                                print('"Well, if I’d have to give an example?"')
                                cont()
                                print('Trissie:')
                                print('"I have a brother in the Gowls"')
                                cont()
                                print('Trissie points her thumb at her tail stump.')
                                cont()
                                print('Trissie:')
                                print('"And because I helped a human, he did this to me."')
                                cont()
                                story.branchSwitch[0] = '1'
                                dialog[0] = True
                            elif (c == '2'):
                                print('Trissie:')
                                print('"I’m not easy to catch but you must be careful and stay safe."')
                                cont()
                                print('Trissie:')
                                print('"If you do, I'"'"'m sure we'"'"'ll meet before long."')
                                cont()
                                story.branchSwitch[0] = '2'
                                dialog[1] = True
                        print('Trissie moved swiftly towards the nearest tree and in an instant had climbed up and disappeared among the branches. It was as if she'"'"'d vanished. Leaving not even a rustle of leaves.')
                        cont()
                        print('Alder returned to the cottage a little disappointed with Trissie gone so soon. But he had work to do and he set about his remaining chores for the day.')
                        cont()
                        story.c2Switch[1] = False
            else:
                print('There was no one to talk to.')
        elif (story.chapter == '3'):
            if (story.c3Switch[2] == False and story.c3Switch[3] == True):
                print('1: Rat')
                t = input('Talk to: ')
                if (t == '1'):
                    print('Alder did not want to get too close to the rat. Even if he could not touch or speak to him.')
            else:
                print('There was no one to talk to.')
                    
    elif(location == '7'):
        if(story.c2Switch[3] == False):
            print('1: Mouse')
            t = input('Talk to: ')
            if (t == '1'):
                print('Mouse:')
                print('"..."')
                cont()
                print('The mouse smimled warmly at Alder, but did not say a word.')
                cont()
        else:
            print('There was no one to talk to.')
    else:
        print('There was no one to talk to.')
