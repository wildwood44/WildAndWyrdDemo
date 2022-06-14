import playableChars
#Character Base Stats
#Set Classes
alder = playableChars.Alder()
class Statistics():
    def levelUP(self, p):
        #print(p.cNext, ' ', p.cExp)
        if(p.cExp >= p.cNext):
            while(p.cExp >= p.cNext and p.cLvl < 60):
                if(p.cLvl < 60):
                    p.cLvl += 1
                    p.maxHealth += 5
                    p.maxStamina += 5
                    p.health += 5
                    p.stamina += 5
                    p.baseAttack += 2
                    p.baseDefence += 2
                    p.baseAccuracy += 2
                    p.baseSpeed += 2
                    p.baseEvasion += 2
                    p.skillPoints += 1
                    print(p.name,' leveled up!')
                    if(p.cLvl == 60):
                        print('Max Level')
                    else:
                        if(p.cLvl < 5):
                            p.cNext = round(p.cNext*1.65)
                        elif(p.cLvl < 20):
                            p.cNext = round(p.cNext*1.55)
                        elif(p.cLvl < 30):
                            p.cNext = round(p.cNext*1.45)
                        elif(p.cLvl < 40):
                            p.cNext = round(p.cNext*1.35)
                        elif(p.cLvl < 50):
                            p.cNext = round(p.cNext*1.25)
                        elif(p.cLvl < 60):
                            p.cNext = round(p.cNext*1.15)
                        #print(p.cNext)

    def stBoost(self, p, sb):
        if(sb['stat'] == 'h' and sb['active']):
            p.maxHealth += sb['boost']
            p.health += sb['boost']
        elif(sb['stat'] == 's' and sb['active']):
            p.maxStamina += sb['boost']
            p.stamina += sb['boost']
        elif(sb['stat'] == 'at' and sb['active']):
            p.baseAttack += sb['boost']
        elif(sb['stat'] == 'df' and sb['active']):
            p.baseDefence += sb['boost']
        elif(sb['stat'] == 'ac' and sb['active']):
            p.baseAccuracy += sb['boost']
        elif(sb['stat'] == 'sp' and sb['active']):
            p.baseSpeed += sb['boost']
        elif(sb['stat'] == 'ev' and sb['active']):
            p.baseEvasion += sb['boost']

    def skillTree(self, p):
        print('\nSkills')
        print('Skill Points: ', p.skillPoints)
        print('You can spend skill points on a stat boost or a character skill.')
        print('1: Stat Boosts')
        print('2: Special Skills')
        skill = input('Skill Type: ')
        if (skill == '1'):
            sbl = []
            print('\nStat Boosts')
            print('Skill Points: ', p.skillPoints)
            count = 1
            temp = False
            for i in p.statBoost:
                if (i['No'] == '1' and i['active'] == False):
                    print(count,': ', i['name'], ' + ', i['boost'])
                    count += 1
                elif (i['No'] == '2' and i['active'] == False and temp == True):
                    print(count,': ', i['name'], ' + ', i['boost'])
                    count += 1
                elif (i['No'] == '3' and i['active'] == False and temp == True):
                    print(count,': ', i['name'], ' + ', i['boost'])
                    count += 1
                if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                    temp = True
                else:
                    temp = False
            sb = input('Boost: ')
            count = 1
            for i in p.statBoost:
                if (i['No'] == '1' and i['active'] == False):
                    if(sb == str(count)):
                        if (p.skillPoints > 0):
                            i['active'] = True
                            stBoost(p,i)
                            print(i['name'],'has been unlocked!')
                            p.skillPoints -= 1
                        else:
                            print('You do not have enough skill points.')
                    count += 1
                elif (i['No'] == '2' and i['active'] == False and temp == True):
                    if(sb == str(count)):
                        if (p.skillPoints > 0):
                            i['active'] = True
                            stBoost(p,i)
                            print(i['name'],'has been unlocked!')
                            p.skillPoints -= 1
                        else:
                            print('You do not have enough skill points.')
                    count += 1
                elif (i['No'] == '3' and i['active'] == False and temp == True):
                    if(sb == str(count)):
                        if (p.skillPoints > 0):
                            i['active'] = True
                            stBoost(p,i)
                            print(i['name'],'has been unlocked!')
                            p.skillPoints -= 1
                        else:
                            print('You do not have enough skill points.')
                    count += 1
                if ((i['No'] == '1' or i['No'] == '2') and i['active'] == True):
                    temp = True
                else:
                    temp = False
        elif (skill == '2'):
            print('\nSpecial Skills')
            print('Skill Points: ', p.skillPoints)
            count = 1
            for i in p.special:
                if (i['unlocked'] == False):   
                    print(count,': ', i['name'], ' - ', i['effect'])
                    count += 1
            sa = input('Boost: ')
            count = 1
            for i in p.special:
                if (i['unlocked'] == False):
                    if(sa == str(count)):
                        if (p.skillPoints > 0):
                            i['unlocked'] = True
                            print(i['name'], 'has been unlocked')
                            p.skillPoints -= 1
                        else:
                            print('You do not have enough skill points.')
                    count += 1
