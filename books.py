
import random
#Read books
def reading(series, book):
    bookPages = []
    readType = 'lines'
    f = open("data/books.txt", "rt")
    skip = False
    for i in f:
        line = i.split('$ ')
        if (line[0] == series and line[1] == book):
            readType = line[3]
            bookPages.append(i)
    print('')
    if (readType == 'lines'):
        for i in bookPages:
            line = i.split('$ ')
            if (line[0] == series and line[1] == book):
                image = line[5]
                content = line[6]
                tabbedline = line[6].split('£')
                if (image != 'None'):
                    print(image)
                if (len(tabbedline) > 1):
                    for i in tabbedline:
                        print('\t',i.strip('\n'))
                else:
                    print('\n',content.strip('\n'))
    elif (readType == 'story'):
        for i in bookPages:
            if(skip == False):
                line = i.split('$ ')
                if (line[0] == series and line[1] == book):
                    image = line[5]
                    content = line[6]
                    tabbedline = line[6].split('£')
                    if (image != 'None'):
                        print(image)
                    if (len(tabbedline) > 1):
                        for i in tabbedline:
                            print('\t',i)
                    else:
                        print('\n',content.strip('\n'))
                    s = input()
                    if(s == 'skip'):
                        skip = True
    elif (readType == 'random'):
        i = random.choice(bookPages)
        line = i.split('$ ')
        if (line[0] == series and line[1] == book):
            image = line[5]
            content = line[6]
            tabbedline = line[6].split('£')
            if (image != 'None'):
                print(image)
            if (len(tabbedline) > 1):
                for i in tabbedline:
                    print('\t',i)
            else:
                print('\n',content.strip('\n'))
