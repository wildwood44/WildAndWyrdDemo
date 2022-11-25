class Page():
    def __init__(self, glossId, section, name):
        self.glossId = glossId
        self.section = section
        self.name = name
        self.unlocked = False
    def unlock(self):
        self.unlocked = True
    def printPage(self):
        f = open("data/Glossary.txt", "rt")
        for i in f:
            line = i.split('$ ')
            if (line[0] == self.section and line[1] == self.name):
                newline = line[2].split('£')
                print(line[2].strip('\n'))
        f.close()
    def __str__(self):
        if (self.unlocked == False):
            return str(self.section + ' : ???')
        else:
            return str(self.section + ' : ' + self.name)



class Glossary():
    def __init__(self):
        self.constructs = [
            Page(0, 'constructs', 'cauldron'),
            Page(1, 'constructs', 'hearth'),
            Page(2, 'constructs', 'knife'),
            Page(3, 'constructs', 'larder'),
            Page(4, 'constructs', 'mortar and pestle'),
            Page(5, 'constructs', 'sword'),
            ]
        self.mammal = [
            Page(7, 'mammal', 'brown rat'),
            Page(8, 'mammal', 'common shrew'),
            Page(9, 'mammal', 'european hedgehog'),
            Page(10, 'mammal', 'field vole'),
            Page(11, 'mammal', 'mole'),
            Page(12, 'mammal', 'red fox'),
            Page(13, 'mammal', 'red squirrel'),
            Page(14, 'mammal', 'weasel'),
            Page(15, 'mammal', 'wood mouse'),
            ]
        self.invertebrates = [
            Page(16, 'invertebrates', 'cricket'),
            Page(17, 'invertebrates', 'hornet'),
            ]
        self.plants = [
            Page(18, 'plants', 'bramble'),
            Page(19, 'plants', 'plantain'),
            ]
        self.folklore = [
            Page(20, 'folklore', 'witch'),
            ]
    def getGlossary(self):
        print('\n1: constructs')
        print('2: folklore')
        print('3: invertebrates')
        print('4: mammals')
        print('5: plants')
        print('e: exit')
        section = input('Select: ')
        count = 1
        if(section == '1' or section == 'construct' or section == 'Construct'):
            for i in self.constructs:
                print(count,') ', str(i))
                count += 1
        elif(section == '2' or section == 'folklore' or section == 'Folklore'):
            for i in self.folklore:
                print(count,') ', str(i))
                count += 1
        elif(section == '3' or section == 'invertebrates' or section == 'invertebrates'):
            for i in self.invertebrates:
                print(count,') ', str(i))
                count += 1
        elif(section == '4' or section == 'mammal' or section == 'Mammal'):
            for i in self.mammal:
                print(count,') ', str(i))
                count += 1
        elif(section == '5' or section == 'plants' or section == 'Plants'):
            for i in self.plants:
                print(count,') ', str(i))
                count += 1
        return section
    def openGlossary(self, section):
        if (section == '1' or section == 'construct' or section == 'Construct' or
            section == '2' or section == 'folklore' or section == 'Folklore' or
            section == '3' or section == 'invertebrates' or section == 'Invertebrates' or
            section == '4' or section == 'mammal' or section == 'Mammal' or
            section == '5' or section == 'plants' or section == 'Plants'):
            item = input('Open: ')
            if(section == '1' or section == 'construct' or section == 'Construct'):
                if (str(item) == '1' and self.constructs[0].unlocked == True):
                    self.constructs[0].printPage()
                elif (str(item) == '2' and self.constructs[1].unlocked == True):
                    self.constructs[1].printPage()
                elif (str(item) == '3' and self.constructs[2].unlocked == True):
                    self.constructs[2].printPage()
                elif (str(item) == '4' and self.constructs[3].unlocked == True):
                    self.constructs[3].printPage()
                elif (str(item) == '5' and self.constructs[4].unlocked == True):
                    self.constructs[4].printPage()
                elif (str(item) == '6' and self.constructs[5].unlocked == True):
                    self.constructs[5].printPage()
            elif(section == '2' or section == 'folklore' or section == 'Folklore'):
                if (str(item) == '1' and self.folklore[0].unlocked == True):
                    self.folklore[0].printPage()
            elif(section == '3' or section == 'invertebrates' or section == 'Invertebrates'):
                if (str(item) == '1' and self.invertebrates[0].unlocked == True):
                    print('Ping')
                    self.invertebrates[0].printPage()
                elif (str(item) == '2' and self.invertebrates[1].unlocked == True):
                    self.invertebrates[1].printPage()
            elif(section == '4' or section == 'mammal' or section == 'Mammal'):
                if (str(item) == '1' and self.mammal[0].unlocked == True):
                    self.mammal[0].printPage()
                elif (str(item) == '2' and self.mammal[1].unlocked == True):
                    self.mammal[1].printPage()
                elif (str(item) == '3' and self.mammal[2].unlocked == True):
                    self.mammal[2].printPage()
                elif (str(item) == '4' and self.mammal[3].unlocked == True):
                    self.mammal[3].printPage()
                elif (str(item) == '5' and self.mammal[4].unlocked == True):
                    self.mammal[4].printPage()
                elif (str(item) == '6' and self.mammal[5].unlocked == True):
                    self.mammal[5].printPage()
                elif (str(item) == '7' and self.mammal[6].unlocked == True):
                    self.mammal[6].printPage()
                elif (str(item) == '8' and self.mammal[7].unlocked == True):
                    self.mammal[7].printPage()
                elif (str(item) == '9' and self.mammal[8].unlocked == True):
                    self.mammal[8].printPage()
            elif(section == '5' or section == 'plants' or section == 'Plants'):
                if (str(item) == '1' and self.plants[0].unlocked == True):
                    self.plants[0].printPage()
                elif (str(item) == '2' and self.plants[1].unlocked == True):
                    self.plants[1].printPage()
            return True
        elif(section != 'e' and section != 'exit' and section != 'Exit'):
            return True
        else:
            return False

    def main(self):
        viewing = True
        while (viewing == True):
            viewing = self.openGlossary(self.getGlossary())
        
