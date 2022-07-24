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
    def questProgress(self, inv):
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
    def qComp(self, inv):
        self.submitted = True
        print(self.name, 'Completed!')
        if(self.reward != 'none' and self.rewardCount > 0):
            if self.reward == 'shillings':
                inv.shillings(self.rewardCount)
            elif self.reward == 0:
                inv.shill += self.rewardCount
            else:
                inv.addItem(self.reward, self.rewardCount)
    #Print side quests
    def printSideQuests(self, inv):
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


