import pickle
PIK = "demo.dat"
location = '1'
chapter = '1'
part = '1'
data = [location, chapter, part]
def save(location, chapter, part):
    data = [location, chapter, part]
    with open(PIK, "wb") as f:
        pickle.dump(data, f)
def loadGame():
    with open(PIK, "rb") as f:
        print (pickle.load(f))
#with open(PIK, "wb") as f:
#    pickle.dump(len(data), f)
#    for value in data:
#        pickle.dump(value, f)
#data2 = []
#with open(PIK, "rb") as f:
#    for _ in range(pickle.load(f)):
#        data2.append(pickle.load(f))
#print (data2)
while(True):
    i = input('Save or load: ')
    if (i == 'save'):
        location = input('location: ')
        chapter = input('chapter: ')
        part = input('part: ')
        save(location, chapter, part)
    elif (i == 'load'):
        loadGame()

