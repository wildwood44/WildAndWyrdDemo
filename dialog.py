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
