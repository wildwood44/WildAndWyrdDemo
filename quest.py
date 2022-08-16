from data import typeSpf

ItemType = typeSpf.ItemType
ArmourType = typeSpf.ArmourType
Weapon1Type = typeSpf.Weapon1Type
Weapon2Type = typeSpf.Weapon2Type
class Quest():
    def __init__(self, questId, client, name, desc,
                 reward, rewardCount,
                 qType,required,qnt):
        self.questId=questId
        self.client=client
        self.name=name
        self.desc=desc
        self.reward= reward
        self.rewardCount= rewardCount
        self.qType=qType
        self.required=required
        self.qnt=qnt
        self.accepted=False
        self.completed=False
        self.submitted=False
    #Progress
    def questProgress(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            if (self.qType == 'action'):
                count = 0
                for i in self.required:
                    if (i == True):
                        count += 1
                if (count == len(self.required)):
                    self.completed = True
            if (self.qType == 'collect'):
                count = 0
                for j in inv.itemList:
                    if(self.required[count].itemType == j['item'].itemType):
                        if(self.required[count].itemId == j['item'].itemId):
                            if (j['count'] == self.qnt):
                                self.completed = True
                    count += 1
    #Quest Rewards
    def qComp(self, party, inv):
        self.submitted = True
        print(self.name, 'Completed!')
        print(self.reward)
        if(self.reward != 'none' and self.rewardCount > 0):
            if self.reward == 'shillings':
                inv.shillings(self.rewardCount)
            elif self.reward == 0:
                inv.shill += self.rewardCount
            elif self.reward == True:
                print('Ping')
                self.reward = False
            else:
                inv.addItem(self.reward, self.rewardCount)
        return self.reward
    def autoComp(self, party, inv):
        if(self.submitted == True):
            return self.qComp(self, party, inv)
    #Print side quests
    def printSideQuests(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            print('Quest: ',self.name, ' Client: ',self.client)
            if (self.qType == 'action'):
                j = 0
                for i in self.desc:
                    print('\t',i, self.required[j])
                    j += 1
            elif (self.qType == 'collect'):
                #i = 0
                for i in self.desc:
                    amount = 0
                    for k in inv.itemList:
                        for l in self.required:
                            if (k['item'].itemType == l.itemType and k['item'].itemId == l.itemId):
                                amount = k['count']
                    print('\t',i, '(', amount, '/', self.qnt,')')
            if(self.reward != 'none' and self.rewardCount > 0):
                if self.reward == 'shillings':
                    print('\tReward: ', 'Shillings', 'x', self.rewardCount,'\n')
                elif self.reward == 0:
                    print('\tReward: ', 'Shillings', 'x', self.rewardCount,'\n')
                else:
                    print('\tReward: ', self.reward.name, 'x', self.rewardCount,'\n')

class A_Quest(Quest):
    def __init__(self, questId, client, name, desc,
                 reward, rewardCount,required,qnt):
        Quest.__init__(self, questId, client, name, desc,
                 reward, rewardCount,
                 'action',required,qnt)

    #Progress
    def questProgress(self, party, inv):
            count = 0
            for i in self.required:
                if (i == True):
                    count += 1
            if (count == len(self.required)):
                self.completed = True
    #Print side quests
    def printSideQuests(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            print('Quest: ',self.name, ' Client: ',self.client)
            j = 0
            for i in self.desc:
                print('\t',i, self.required[j])
                j += 1

class C_Quest(Quest):
    def __init__(self, questId, client, name, desc,
                 reward, rewardCount,required,qnt):
        Quest.__init__(self, questId, client, name, desc,
                 reward, rewardCount,
                 'collect',required,qnt)

    #Progress
    def questProgress(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            count = 0
            for j in inv.itemList:
                if(self.required[count].itemType == j['item'].itemType):
                    if(self.required[count].itemId == j['item'].itemId):
                        if (j['count'] == self.qnt):
                            self.completed = True
                count += 1
    #Print side quests
    def printSideQuests(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            print('Quest: ',self.name, ' Client: ',self.client)
            for i in self.desc:
                amount = 0
                for k in inv.itemList:
                    for l in self.required:
                        if (k['item'].itemType == l.itemType and k['item'].itemId == l.itemId):
                            amount = k['count']
                print('\t',i, '(', amount, '/', self.qnt,')')
class E_Quest(Quest):
    def __init__(self, questId, client, name, desc,
                 reward, rewardCount,required,wearer):
        Quest.__init__(self, questId, client, name, desc,
                 reward, rewardCount,
                 'equip',required,0)
        self.wearer = wearer

    #Progress
    def questProgress(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            for j in self.required:
                if(j.itemType == ArmourType.hat):
                    if(self.wearer.head.armId == j.armId):
                        self.completed = True
                if(j.itemType == ArmourType.shirt):
                    if(self.wearer.head.armId == j.armId):
                        self.completed = True
                if(j.itemType == ArmourType.trousers):
                    if(self.wearer.head.armId == j.armId):
                        self.completed = True
                if(j.itemType == Weapon1Type.sword or j.itemType == Weapon1Type.dagger or j.Weapon1Type == Weapon1.spear or
                   j.itemType == Weapon1Type.axe or j.itemType == Weapon1Type.mace or j.Weapon1Type == Weapon1.staff):
                    if(self.wearer.weapon1.wpId == j.wpId):
                        self.completed = True
                if(j.itemType == Weapon2Type.bow or j.itemType == Weapon2Type.crossbow or j.itemType == Weapon2Type.sling or
                   j.itemType == Weapon2Type.shield or j.itemType == Weapon2Type.wand):
                    if(self.wearer.weapon1.wpId == j.wpId):
                        self.completed = True
    #Print side quests
    def printSideQuests(self, party, inv):
        if(self.accepted == True and self.submitted != True):
            print('Quest: ',self.name, ' Client: ',self.client)
            for i in self.desc:
                for j in self.required:
                    if(j.itemType == ArmourType.hat):
                        if(self.wearer.head.armId == j.armId):
                            print('\t', j, 'equiped.')
                        else:
                            print('\t', j, 'not equiped.')
                    if(j.itemType == ArmourType.shirt):
                        if(self.wearer.shirt.armId == j.armId):
                            print('\t', j, 'equiped.')
                        else:
                            print('\t', j, 'not equiped.')
                    if(j.itemType == ArmourType.trousers):
                        if(self.wearer.trousers.armId == j.armId):
                            print('\t', j, 'equiped.')
                        else:
                            print('\t', j, 'not equiped.')
                    if(j.itemType == Weapon1Type.sword or j.itemType == Weapon1Type.dagger or j.Weapon1Type == Weapon1.spear or
                       j.itemType == Weapon1Type.axe or j.itemType == Weapon1Type.mace or j.Weapon1Type == Weapon1.staff):
                        if(self.wearer.weapon1.wpId == j.wpId):
                            print('\t', j, 'equiped.')
                        else:
                            print('\t', j, 'not equiped.')
                    if(j.itemType == Weapon2Type.bow or j.itemType == Weapon2Type.crossbow or j.itemType == Weapon2Type.sling or
                       j.itemType == Weapon2Type.shield or j.itemType == Weapon2Type.wand):
                        if(self.wearer.weapon2.wpId == j.wpId):
                            print('\t', j, 'equiped.')
                        else:
                            print('\t', j, 'not equiped.')

