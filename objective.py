class Objective():
    #Print the objectives
    def printObjective(self, story, inv, party):
        print("\nObjectives")
        print("Main:")
        if(story.tutorialSwitch[0] == True):
            print("\tYou will need to have a quick look around. Type "'"examine" or "e"'" to explore the room Alder is currently in then type in an 'object' from that room like the window.")
        elif(story.tutorialSwitch[1] == True):
            print('\tAlder needs to go outside. He will have to "move"("m") through the living room and then move outside.')
        elif(story.tutorialSwitch[2] == True):
            print('\tTalk(t) to Florence.')
        elif(story.tutorialSwitch[3] == True):
            print('\tTalk(t) to Thay.')
        elif(story.tutorialSwitch[4] == True):
            print('\tExamine table in the shed, pick up knife and "equip"("x") as main weapon.')
            for q in story.mQuests:
                q.printSideQuests(party, inv)
        elif(story.tutorialSwitch[5] == True):
            for q in story.mQuests:
                q.printSideQuests(party, inv)
        elif(story.tutorialSwitch[6] == True):
            print('\tReturn to the cottage and examine to bed to end the day.')
            print('\tTalk to characters if a character has a "!" mark then they will quest for Alder.')
        elif(story.c2Switch[0] == True):
            print('\tMove to the living room to attend meeting.')
        elif(story.c2Switch[1] == True):
            print('\tTalk to Trissie for archery practice')
        elif(story.c2Switch[2] == True):
            print('\tGo to bed.')
        elif(story.c2Switch[3] == True):
            print('\tExplore strange place.')
        elif(story.c3Switch[0] == True and chapter == '2'):
            print('\tTake sword!')
        elif(story.c3Switch[0] == True and chapter == '3'):
            print('\tGet Florence!')
        elif(story.c3Switch[1] == True):
            print('\tRead "Read Magical articles of history".')
        elif(story.c3Switch[2] == True):
            print('\tLook out living room window.')
        elif(story.c3Switch[3] == True):
            print('\tLook out living room window.')
        elif(story.c3Switch[4] == True):
            print('\tTalk to weasel')
        elif(story.c3Switch[5] == True):
            print('\tBuy from Jeb.')
        elif(story.c3Switch[6] == True):
            print('\tLeave cottage.')
            
        print("\nSide:")
        for q in story.sQuests:
            q.printSideQuests(party, inv)
