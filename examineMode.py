import itemList
import combat
import playableChars
import enemyUnits
import books
item = itemList
com = combat
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

def examine(game_over, party, location, story, inv):
    alder = party.alder
    examining = True
    while (examining == True):
        print('\nExamine')
        print('Type "e" to end examining')
        for i in locations:
            if (location == i['locId']):
                print(i['name'])
        if (location == '1'):
            print("The cottage kitchen contained various 'pots' hanging on the wall. It had a 'stove' where a 'cauldron' was dangling on a chain. In addition, a smaller room served as the 'larder'. There was also a 'cupboard' and two 'tables', one of which had a wooden 'bowl' on it. Alder had been washing dishes in a 'basin' on the other table next to the 'window'.")
            e = input('Examine: ')
            if (e == 'cauldron' or e == 'Cauldron'):
                if (story.sQuests[0]['accepted'] == True and story.sQuests[0]['required'][1] == False):
                    print('Alder got a wet cloth and started scrubbing the cauldron. Florace peeked into the living room at Kyla and then went over to help him.')
                    cont()
                    print('Florace:')
                    print('"Shh."')
                    story.sQuests[0]['required'][1] = True
                    examining = False
                else:
                    print("A small metal cauldron was suspended above the stove by a chain. It was empty right now.")
                cont()
            elif (e == 'pots' or e == 'Pots'):
                print('Various pots and pans were hung on hooks along the wall.')
                cont()
            elif (e == 'cupboard' or e == 'Cupboard'):
                print('The cupboard was full of plates, bowls and other kitchen and dining utensils.')
                cont()
            elif (e == 'bowl' or e == 'Bowl'):
                if (story.PKSwitch[0] == True):
                    print('A large wooden bowl. It has hazelnuts in it.')
                    pickup = input('Take the hazelnuts?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 Hazelnut(s) obtained')
                        inv.addItem(item.food[2], 5)
                        story.PKSwitch[0] = False
                        cont()
                else:
                    print('A large wooden bowl. It'"'"'s empty.')
                    cont()
            elif (e == 'basin' or e == 'Basin'):
                print('The basin Alder was washing in was full of water from Alder cleaning dishes. Clean plates were lined up to the side.')
                cont()
            elif (e == 'window' or e == 'Window' or e == 'windows' or e == 'Windows'):
                if(story.tutorialSwitch[2] == True):
                    print('Florace and Thay were talking outside the window.')
                    cont()
                    print('Alder:')
                    print('"I'"'"'m coming out"')
                    story.chapter = '1'
                    story.tutorialSwitch[0] = False
                else:
                    print('The clearing at the front of of the cottage can be seen through the window.')
                cont()
            elif (e == 'stove' or e == 'Stove'):
                print('The stove was made of metal plates above an unlit fireplace full of dry branches. The fire would heat the metal plates of the stove to cook meat.')
                cont()
            elif (e == 'table' or e == 'Table' or e == 'tables' or e == 'Tables'):
                print('A rectangular wooden table stood in the centre of the room while a thinner one with a basin stood by the window.')
                cont()
            elif (e == 'hornets' or e == 'Hornets'):
                if (story.tutorialSwitch[5] == False and story.c2Switch[0] == True):
                    print('The hornets Alder slew were hung up on hooks. To be cooked for supper.')
                    cont()
            elif (e == 'larder' or e == 'Larder'):
                if (story.sQuests[1]['accepted'] == True):
                    print('There was only a single loaf of bread in the larder. It would have to do.')
                    story.sQuests[1]['completed'] = True
                elif (story.sQuests[1]['completed'] == True):
                    print('The larder was empty.')
                else:
                    print('A small cool room of shelves and hooks to store food, mostly empty except for a loaf of bread. Kyla’s familiar Tawie was out resupplying. Alder was not looking forward to her return.')
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '2'):
            print("The living room was a homely place that was accessible by both the front and back 'door' and lit by the 'windows'. It had two 'chairs' and a 'table' in front of a 'fireplace' as well as a single 'bookshelf' with three shelves full of books.")
            if (story.sQuests[2]['required'][1] == True):
                print('There was a large hole in the wall.')
            e = input('Examine: ')
            if (e == 'bookshelf' or e == 'Bookshelf'):
                if (story.sQuests[2]['accepted'] == True and story.sQuests[2]['required'][0] == False):
                    print('Alder carried each of the books and put them in a neat pile near the stairs.')
                    cont()
                    story.sQuests[2]['required'][0] = True
                elif(story.sQuests[2]['required'][0] == True):
                    print('The bookshelf was empty.')
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
                                print('Alder:')
                                print('"A "Cohuleen Druith" hat."')
                                cont()
                                print('Alder:')
                                print('"The "Ring of Eluned"."')
                                cont()
                                print('Alder:')
                                print('"The "Gae Bulg" spear."')
                                cont()
                                print('Alder:')
                                print('"Found it!"')
                                cont()
                                print('Alder:')
                                print('"It’s called "Lief", "The sword of the seasons"."')
                                cont()
                                print('Kyla:')
                                print('"As I thought."')
                                cont()
                                print('Kyla:')
                                print('"But there is only one way to confirm this."')
                                cont()
                                print('Kyla unsheathed that sword and held it in her hand. The blade darkened and bent and it was not long before it dropped off leaving only the handle.')
                                cont()
                                print('Kyla:')
                                print('"Boy you can have the sword back now, make sure you hold it by the grip."')
                                cont()
                                print('Alder said nothing as he picked up the sword. As he did, a new blade started to grow from the rain-guard until it was back to its original glory.')
                                cont()
                                alder.weapon1 = weapons[1]
                                print(alder.weapon1['name'],'equipped!')
                                cont()
                                print('Florace:')
                                print('"What did you do?"')
                                cont()
                                print('Kyla:')
                                print('"The sword only sprouts for the Scion."')
                                cont()
                                print('Kyla:')
                                print('"In order words."')
                                cont()
                                print('Kyla:')
                                print('"You."')
                                cont()
                                dialog = [False, False, False]
                                while(dialog[0] == False or dialog[1] == False or dialog[2] == False):
                                    print('1: "What is a Scion?"')
                                    print('2: "Does this have anything to do with the mouse I saw in my dream?"')
                                    print('3: "What'"'"'s with the sword blade?"')
                                    c = input('Alder: ')
                                    if (c == '1'):
                                        print('Kyla:')
                                        print('"What is…!?"')
                                        cont()
                                        print('Kyla:')
                                        print('"How do you not know what the Scion is!?"')
                                        cont()
                                        print('Florace:')
                                        print('"I thought it was more important that he knew herbs and how to read and write than history."')
                                        cont()
                                        print('Kyla:')
                                        print('*Sigh*')
                                        cont()
                                        print('Kyla:')
                                        print('"The Scion is the great hero of Avalon."')
                                        cont()
                                        print('Kyla:')
                                        print('"They are able to pass on their knowledge and natural abilites after death."')
                                        cont()
                                        print('Kyla:')
                                        print('"One previous Scion killed a dragon, while another saved countless innocents from slavers."')
                                        cont()
                                        print('Kyla:')
                                        print('"And I knew one who put kings themselves in their rightful place."')
                                        cont()
                                        print('Kyla:')
                                        print('"But I digress."')
                                        cont()
                                        dialog[0] = True
                                    elif (c == '2'):
                                        print('Kyla:')
                                        print('"That mouse was no doubt Agrimus; the Scion before you."')
                                        cont()
                                        print('Kyla:')
                                        print('"He appeared to you to pass on his title and sword."')
                                        cont()
                                        print('Kyla:')
                                        print('"I am shocked he chose you though."')
                                        cont()
                                        print('Kyla:')
                                        print('"He was the hero of the war against the humans of Glorion."')
                                        cont()
                                        print('Kyla:')
                                        print('"And out of countless potentials he goes for my servant."')
                                        cont()
                                        dialog[1] = True
                                    elif (c == '3'):
                                        print('Kyla:')
                                        print('"It’s in the book."')
                                        cont()
                                        print('Kyla:')
                                        print('"The sword blade is like a plant and the grip its roots."')
                                        cont()
                                        print('Kyla:')
                                        print('"When held by the Scion it grows and strengthens, when held by any other it weakens and dies."')
                                        cont()
                                        dialog[2] = True
                                print('???:')
                                print('"The rabbit seeks his burrow!"')
                                cont()
                                print('*Click*')
                                print('*Ring*')
                                cont()
                                print('The door unlocked and the bell chimed in responce to the words of the voice outside. The ringing filled the resounded throught the cottage but was prevelant in the already alerted living room.')
                                cont()
                                print('Alder, Florace and Kyla:')
                                print('"...?"')
                                cont()
                                print('Florace:')
                                print('"Who is that?"')
                                cont()
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
                if (story.sQuests[0]['accepted'] == True and story.sQuests[0]['required'][0] == False):
                    print('Alder got to work cleaning the fireplace using a brush and cloth. By the end his arms were completely blackened by soot.')
                    cont()
                    print('Kyla:')
                    print('"Throw that ash outside."')
                    cont()
                    print('Kyla:')
                    print('"If it gets on the floor, you'"'"'re cleaning it up."')
                    cont()
                    story.sQuests[0]['required'][0] = True
                    examining = False
                elif (story.sQuests[0]['required'][0] == False):
                    print('The fireplace was unlit. It was used last night and still had ash and soot in it.')
                    cont()
                    print('Alder:')
                    print('"I’ll clean it up later."')
                    cont()
                else:
                    print('The fireplace was unlit.')
                    cont()
            elif (e == 'chairs' or e == 'Chairs'):
                print('There were two wooden armchairs both with partridge feather cushions.')
                cont()
            elif (e == 'table' or e == 'Table'):
                if (story.c3Switch[4] == False and story.c3Switch[5] == True):
                    print('Jeb laid out his wares on the table.')
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
                    examining = False
                else:
                    print("A single round wooden table sat a safe distance from the fire, but close enough to feel its warmth.")
                    cont()
            elif (e == 'door' or e == 'Door'):
                print('There was a door for either side of the house, both leading outside.')
                cont()
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
                    print('There were four windows showing the clearing on either side of the cottage.')
                    cont()
            elif (e == 'wall' or e == 'Wall'):
                if (story.sQuests[2]['accepted'] == True and story.sQuests[2]['required'][1] == False):
                    print('Alder aligned himself with where the tools hung in the shed on the other side of the wall.')
                    cont()
                    victory = com.Battle(party, [enemyUnits.Wall(), enemyUnits.Null(), enemyUnits.Null()],inv)
                    if (victory == True):
                        print('The swords power was incredible. With a bit of force it easily pierced the clay walls and Alder tore it down through the gap he had created, the tools on the other side now fallen amongst rubble. Kyla apparently found this amusing. But the hole allowed Alder to enter the shed.')
                        cont()
                        story.sQuests[2]['required'][1] = True
                        examining = False
            elif (e == 'e' or e == 'E'):
                examining = False
            else:
                print('Alder thought about it, but it was of no interest to him.')
                cont()
        elif (location == '3'):
            print("The burrow was within a deep wood, isolated from society. The 'sky' was clear blue and the late summer 'plant' was abundant amongst the 'trees' and 'rocks' of the forest. Part of the stone disguising the 'cottage', was actually an old 'shed' with a slanted roof, nearby was a large 'bramble' bush.")
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                print('It was a bright, clear blue.')
                cont()
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                print('There were a variety of late-summer mushrooms growinig around the area.')
                cont()
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                print('Various weeds, wildflowers and moss interspersed with bramble bushes holding ripe blackberries.')
                cont()
            elif (e == 'trees' or e == 'Trees'):
                print('Various trees made up the woodland, the majority were birch, rowen and holly.')
                cont()
            elif (e == 'rocks' or e == 'Rocks'):
                print('There were a few boulders in the area. None were as large as the cottage.')
                cont()
            elif (e == 'cottage' or e == 'Cottage'):
                print('While the cottage was made to look like a large boulder from the outside, it actually had two floors and was made from white clay bricks. It was cosy and well protected against the elements, but Alder had always felt constricted.')
                cont()
            elif (e == 'shed' or e == 'Shed'):
                print('The shed had a single old door. From the outside it looked like part of the larger stone, but it was really made entirely of splintered wooden planks.')
                cont()
            elif (e == 'bush' or e == 'Bush' or e == 'blackberry' or e == 'Blackberry' or e == 'blackberry bush' or e == 'Blackberry Bush'  or e == 'bramble' or e == 'Bramble'):
                if (story.PKSwitch[2] == True):
                    print('The bramble bush was a convenient source of fresh fruit at this time of year. It still had a few blackberries on it.')
                else:
                    print('It still had a few blackberries on it but they were out of reach and Alder did not want to get pricked by its thorns.')
                if (story.PKSwitch[2] == True):
                    pickup = input('Pick the blackberries?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n5 blackberries obtained')
                        inv.addItem(item.food[0], 5)
                        story.PKSwitch[2] = False
                if (story.sQuests[0]['accepted'] == True and story.sQuests[0]['required'][2] == False):
                    print('Alder picked some bramble leaves, careful to avoid the thorns. He wondered what potion Kyla was going to use them for.')
                    count = 0
                    for i in inv:
                        if (i['type'] == ItemType.ingredient):
                                if (i['ingId'] == '1'):
                                    count += 1
                    if (count == 0):
                        inv.addItem(item.ingre[0], 1)
                    else:
                        print ('Alder already had some.')
                    examining = False
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '4'):
            if (story.c2Switch[2] == True):
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'. Opposite the entrance was a 'table' used for crafts with an old 'sack' was slumped against it and a 'bow' and 'quiver' full of 'arrows'.")
            else:
                print("The inside of the shed was illuminated by a 'window' on the left side from the entrance. It was full of loose ‘tools’ Alder used for gathering, woodwork and gardening, while ingredients and more fragile equipment for magic potions were held in 'pots' and 'crates'. Opposite the entrance was a 'table' used for crafts.")
            if (story.sQuests[2]['required'][1] == True):
                print('There was a large hole in the wall.')
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('A single window was to the left upon entering through the doorway.')
                cont()
                print('it'"'s"' angle meant that upon looking through, only the woods could been seen.')
                cont()
            elif (e == 'tools' or e == 'Tools' or e == 'axe' or e == 'Axe' or e == 'saw' or e == 'Saw' or
                  e == 'pick' or e == 'Pick' or e == 'shovel' or e == 'Shovel' or e == 'sickle' or e == 'Sickle' or
                  e == 'rod' or e == 'Rod' or e == 'fishing' or e == 'Fishing' or e == 'fishing rod' or e == 'Fishing rod'):
                print('Various tools were hung on the wall and sat on the shelves, including an axe, saw, pick, shovel, sickle and fishing rod.')
                cont()
            elif (e == 'pots' or e == 'Pots'):
                if (story.sQuests[2]['accepted'] == True and story.sQuests[2]['required'][2] == False):
                    print('Alder carried each pot one by one to the living room, their weight varyied by how full they were and what was in them. The heaviest pot was full of ground up plant matter and weighed as much as a cannon ball. Alder brought the last one in with great strain.')
                    cont()
                    location = '2'
                    story.sQuests[2]['required'][2] = True
                    examining = False
                elif(story.sQuests[2]['required'][2] == True):
                    print('There weren'"'"'t any pots left.')
                else:
                    print('The pots contained potion ingredients, left in the shed to save space in the main cottage. One pot was completely filled with eyeballs.')
                    cont()
            elif (e == 'crates' or e == 'Crates' or e == 'boxes' or e == 'Boxes'):
                print('Kyla had put spare magical tools in study crates to keep them from breaking.')
                cont()
            elif (e == 'table' or e == 'Table'):
                if (story.PKSwitch[1] == True):
                    print("On the table was an unlit 'candle', a 'mortar' and 'pestle' and a hunting 'knife'.")
                    if (story.tutorialSwitch[3] == False):
                        pickup = input('Take the hunting knife?(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nHunting Knife obtained')
                            inv.addItem(item.weapons[2], 1)
                            story.PKSwitch[1] = False
                            examining = False
                            cont()
                else:
                    print("On the table was an unlit 'candle' and a 'mortar' and 'pestle'.")
                    cont()
            elif (e == 'candle' or e == 'Candle'):
                print('The candle was placed in a candlestick. It was unlit.')
                cont()
            elif (e == 'mortar' or e == 'Mortar' or e == 'pestle' or e == 'Pestle'):
                if (story.sQuests[0]['accepted'] == True and story.sQuests[0]['required'][2] == False):
                    for i in inv:
                        if (i['type'] == ItemType.ingredient and i['ingId'] == '1'):
                            print('Alder ground the leaves with the pestle until they were powder. He then put them in a nearby pot containing remnants of the same powder.')
                            cont()
                            story.sQuests[0]['required'][2] = True
                            examining = False
                else:
                    print('A mortar and pestle were on the table.')
                    cont()
                    print('Florace recently used them to grind ingredients for potions.')
                    cont()
            elif (e == 'knife' or e == 'Knife'):
                print('The knife was designed for hunting but it looks like someone has been using it to cut ingredients.')
                cont()
            elif (e == 'e' or e == 'E'):
                examining = False
            elif (story.c2Switch[2] == True):
                if (e == 'sack' or e == 'Sack'):
                    print('The old burlap sack was intended for foraging, but was cheaply made and on the verge of falling apart.')
                    if (story.PKSwitch[5] == True):
                        print('There'"'"'s a bandage inside.')
                        cont()
                        pickup = input('Take the bandage.(y/n)')
                        confirm = yn(pickup)
                        if (confirm == True):
                            print('\nBandage obtained')
                            inv.addItem(item.items[0], 1)
                            story.PKSwitch[5] = False
                    cont()
                elif (e == 'bow' or e == 'Bow' or e == 'quiver' or e == 'Quiver' or e == 'arrows' or e == 'Arrows'):
                    print('A practice bow and a quiver full of arrows. They were intended as a gift for Florace but she was never interested in archery, so they were passed to Alder instead.')
                    cont()
        elif (location == '5'):
            print("Sunlight beamed through the solitary curtainless 'window' of Alder's small bedroom, which contained only a makeshift 'bed'.")
            e = input('Examine: ')
            if (e == 'window' or e == 'Window'):
                print('Through the small, curtainless window, Alder could see sunlight breaching the branches of the Oldwyrm Woods near the edge of the clearing.')
                cont()
            elif (e == 'bed' or e == 'Bed'):
                print('It was cheaply made from dry wood and partridge feathers. It was powdered with herbs to stop it smelling. Thay helped Alder make it.')
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
                        print('Alder got into his makeshift bed and drifted to sleep for the night.')
                        if (story.tutorialSwitch[5] == False and story.tutorialSwitch[6] == True):
                            if(story.sQuests[0]['accepted'] == True and story.sQuests[0]['submitted'] == False):
                                ab = input('Abandon quests?(y/n)')
                                confirm = yn(ab)
                                if (confirm == True):
                                    story.sQuests[0]['accepted'] = False
                                    print(story.sQuests[0]['name'],' abandoned!')
                                    story.tutorialSwitch[6] = False
                                    story.part = '1'
                                    story.switch[5] = True
                                    story.chapter = '2'
                                    examining = False
                                    bed()
                            else:
                                story.tutorialSwitch[6] = False
                                story.part = '1'
                                story.switch[5] = True
                                examining = False
                                story.chapter = '2'
                                bed()
                        else:
                            bed()
                            if(story.c2Switch[2] == True):
                                story.switch[7] = True
                                story.part = '3'
                                story.c2Switch[2] = False
                            examining = False
                        cont()
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '6'):
            if (story.mQuests[0]['accepted'] == True and story.mQuests[0]['completed'] == False):
                print("The cottage was out of sight, but being familiar with the surrounding 'plants', and 'rocks' Alder knew where he was. There were some 'crickets' nearby, perfect for tonight’s meal.")
            else:
                print("The cottage was out of sight, but being familiar with the surrounding 'plants', and 'rocks' Alder knew where he was.")
            e = input('Examine: ')
            if (e == 'sky' or e == 'Sky'):
                print('It was a bright, clear blue.')
                cont()
            elif (e == 'mushroom' or e == 'Mushroom' or e == 'mushrooms' or e == 'Mushrooms'):
                if (story.PKSwitch[3] == True):
                    print('There were a variety of late-summer mushrooms growing around the area. Many of which are edible.')
                    cont()
                    pickup = input('Take the mushrooms?(y/n)')
                    confirm = yn(pickup)
                    if (confirm == True):
                        print('\n3 mushrooms(s) obtained')
                        inv.addItem(item.food[3], 3)
                        story.PKSwitch[3] = False
                else:
                    print('There was a variety of late-summer mushrooms around the area. Some circled the area as part of the spell need to go between the realms. Alder knew better than to pick these.')
                    cont()
            elif (e == 'plants' or e == 'Plants' or e == 'plant' or e == 'Plant'):
                print('Various weeds, wildflowers and moss.')
                cont()
            elif (e == 'trees' or e == 'Trees'):
                print('Various trees made up the woodland, the most frequent were birch, rowen and holly.')
                cont()
            elif (e == 'rocks' or e == 'Rocks' or e == 'boulder' or e == 'Boulder'):
                print('There were a few boulders in the area. There was a large one were the cottage was.')
                cont()
            elif (e == 'cottage' or e == 'Cottage'):
                print('The cottage was gone from sight. Replaced with a large boulder.')
                cont()
            elif (e == 'cricket' or e == 'Cricket' or e == 'crickets' or e == 'Crickets'):
                if (story.mQuests[0]['accepted'] == True and story.mQuests[0]['completed'] == False):
                    print('Some large brown crickets were in the area.')
                    cont()
                    fight = input('Do you want to fight them.(y/n)')
                    confirm = yn(fight)
                    if (confirm == True):
                        print('Entering battle')
                        win = False
                        com.Battle(party.listParty(), [enemyUnits.Cricket(), enemyUnits.Null(), enemyUnits.Null()],inv)
                        if(party.alder.cExp > 0):
                            print('Alder:')
                            print('"Hunt succesful."')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('As Alder collected the slain cricket, a loud buzzing came at him from his side. Two hornets came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            win = com.Battle(party.listParty(), [enemyUnits.Hornet(), enemyUnits.Hornet(), enemyUnits.Null()],inv)
                        elif(party.alder.cExp == 0):
                            print('Alder:')
                            print('"Come back you!"')
                            cont()
                            print('Alder tried in vain to get the cricket, but it had already jumped out of reach.')
                            cont()
                            print('???:')
                            print('"Bzz!"')
                            cont()
                            print('The loud buzzing of insect wings came from Alder'"'"'s side. Two hornets came at him.')
                            cont()
                            print('Alder:')
                            print('"Ahhh!"')
                            cont()
                            win =com.Battle(party.listParty(), [enemyUnits.Hornet(), enemyUnits.Hornet(), enemyUnits.Null()],inv)
                        if (win == False):
                            #print('When Alder is defeated he will lose some of his possessions such as currency. The story will be taken back to before the fight so another attempt can be made.')
                            location = '3'
                            party.alder.health = party.alder.maxHealth
                            party.alder.stamina = party.alder.maxStamina
                            game_over = True
                            break
                        else:
                            story.tutorialSwitch[5] = False
                            print('The hornets were still twitching, but Alder knew they were dead.')
                            cont()
                            print('Alder:')
                            print('"Did I anger them?"')
                            cont()
                            print('Alder was puzzled by the attack but regardless it was time to return to Florace.')
                            cont()
                        examining = False
                else:
                    print('The other crickets had fled.')
            elif (e == 'e' or e == 'E'):
                examining = False
        elif (location == '7'):
            if(story.c2Switch[3] == True):
                print("Large 'trees' surrounded him in a neat circle like pillars; the 'branches' formed a mosaic ceiling. There was a 'light' from an unknown source that shone in the center in front of Alder.")
            else:
                print("The mouse was holding the 'sword's' hilt to Alder's hand while ghostly 'spectors' watched.")
            e = input('Examine: ')
            if(e == 'trees' or e == 'Trees' or e == 'pillars' or e == 'Pillars'):
                print('Giant trees formed a perfect circle around the clearing like pillars.')
            elif(e == 'ceiling' or e == 'Ceiling' or e == 'mosaic' or e == 'Mosaic' or e == 'branches' or e == 'Branches'):
                print('The ceiling was covered in various different leaves such as oak, cider, alder and many others which Alder did not recognise, their branches were curved so the whole was a spiralling mosaic.')
            elif(e == 'light' or e == 'Light'):
                print('From the centre of the clearing a misty light hung from unknown source, illuminating the area as far as the trees.')
                examining = False
                if(story.c2Switch[3] == True):
                    story.switch[8] = True
                    part = '4'
            elif (e == 'e' or e == 'E'):
                examining = False
            elif(story.c2Switch[3] == False):
                if(e == 'sword' or e == 'Sword'):
                    print('The double edged sword was a dark green with silver embellishments along the hilt and scabbard. It was a size suited for a mouse but would still be heavy for one. Now that it was closer Alder could see detail in its design. What looked like a thorny stem engraved around the grip, the rain-guard was shaped to resemble leaves and the pommel was tear-shaped. A rounded slot was carved into the scabbard.')
                    cont()
                    sword = input('Take the sword!(y/n)')
                    confirm = yn(sword)
                    if(confirm == True):
                        story.switch[9] = True
                        story.part = '5'
                        examining = False
                elif(e == 'ghosts' or e == 'Ghosts' or e == 'spectors' or e == 'Spectors'):
                    print('The ghostly specters lingered within the darkness between the trees. Every creature of Albion imaginable was there.')
                elif (e == 'e' or e == 'E'):
                    examining = False
