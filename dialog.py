def cutscene(story, read):
    skip = False
    f = open("data/Cutscenes.txt", "rt")
    for i in f:
        if(skip == False):
            line = i.split('$ ')
            if (line[0] == story.chapter and line[1] == read and line[2] == story.part):
                newline = line[4].split('£')
                if (len(newline) > 1):
                    print(newline[0],'\n',newline[1].strip('\n'))
                else:
                    print(line[4].strip('\n'))
                s = input()
                if(s == 'skip'):
                    skip = True
    f.close()
def talk(story, read, option='0'):
    skip = False
    f = open("data/Talk_Dialog.txt", "rt")
    for i in f:
        if(skip == False):
            line = i.split('$ ')
            if (line[0] == story.chapter and line[1] == read and line[2] == story.part and line[3] == option):
                newline = line[5].split('£')
                if (len(newline) > 1):
                    print(newline[0],'\n',newline[1].strip('\n'))
                else:
                    print(line[5].strip('\n'))
                s = input()
                if(s == 'skip'):
                    skip = True
    f.close()
    
def room(story, item, option='default'):
    f = open("data/Examine_Dialog.txt", "rt")
    for i in f:
        line = i.split('$ ')
        if (line[0] == item and line[1] == option):
            newline = line[3].split('£')
            if (len(newline) > 1):
                print(newline[0],'\n',newline[1].strip('\n'))
            else:
                print(line[3].strip('\n'))
    f.close()

    
def examine(story, item, option='default'):
    skip = False
    f = open("data/Examine_Dialog.txt", "rt")
    for i in f:
        if(skip == False):
            line = i.split('$ ')
            if (line[0] == item and line[1] == option):
                newline = line[3].split('£')
                if (len(newline) > 1):
                    print(newline[0],'\n',newline[1].strip('\n'))
                else:
                    print(line[3].strip('\n'))
                s = input()
                if(s == 'skip'):
                    skip = True
    f.close()
    
def move(story, location, to, option='default'):
    skip = False
    f = open("data/Move_Dialog.txt", "rt")
    for i in f:
        if(skip == False):
            line = i.split('$ ')
            if (line[0] == location and line[1] == to and line[2] == option):
                newline = line[4].split('£')
                if (len(newline) > 1):
                    print(newline[0],'\n',newline[1].strip('\n'))
                else:
                    print(line[4].strip('\n'))
                s = input()
                if(s == 'skip'):
                    skip = True
    f.close()
