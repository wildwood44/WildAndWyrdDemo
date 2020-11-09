chapter = '0'

def printline():
    print()

def cutscene():
    if (chapter == '0'):
        skip = False
        f = open("data/Cutscenes.txt", "rt")
        for i in f:
            if(skip == False):
                line = i.split('$ ')
                if (line[0] == '0'):
                    newline = line[4].split('£')
                    if (len(newline) > 1):
                        print(newline[0],'\n',newline[1])
                    else:
                        print(line[4])
                    s = input()
                    if(s == 'skip'):
                        skip = True
cutscene()
