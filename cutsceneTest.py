chapter = '0'
part = '1'
switch = [True]

def cutscene():
    global chapter, part, switch
    running = True
    while(running == True):
        if (chapter == '0'):
            skip = False
            f = open("data/Cutscenes.txt", "rt")
            for i in f:
                if(skip == False):
                    line = i.split('$ ')
                    if (line[0] == chapter):
                        newline = line[4].split('£')
                        if (len(newline) > 1):
                            print(newline[0],'\n',newline[1])
                        else:
                            print(line[4])
                        s = input()
                        if(s == 'skip'):
                            skip = True
            chapter = '1'
        elif (chapter == '1'):
            if (switch[0] == True):
                skip = False
                f = open("data/Cutscenes.txt", "rt")
                for i in f:
                    if(skip == False):
                        line = i.split('$ ')
                        if (line[0] == chapter):
                            if(line[1] == '0' and line[2] == part):
                                newline = line[4].split('£')
                                if (len(newline) > 1):
                                    print(newline[0],'\n',newline[1])
                                else:
                                    print(line[4])
                                s = input()
                                if(s == 'skip'):
                                    skip = True
                            elif(line[1] == '1' and line[2] == part):
                                newline = line[4].split('£')
                                if (len(newline) > 1):
                                    print(newline[0],'\n',newline[1])
                                else:
                                    print(line[4])
                                s = input()
                                if(s == 'skip'):
                                    skip = True
            
cutscene()
