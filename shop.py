import itemList
item = itemList
class ShopItem():
    def __init__(self, item, cost, inStock):
        self.item = item
        self.cost = cost
        self.inStock = inStock

class Shopkeeper():
    def __init__(self, name, items):
        self.name = name
        self.items = items
    def printItems(self):
        count = 1
        for i in self.items:
            print(count,': ',i.item.name, ' Remaining:', i.inStock, ' Cost:', i.cost)
            count += 1
    def selectItem(self, inv):
        count = 1
        p = input('Purchase: ')
        for i in self.items:
            if(p == str(count)):
                if (inv.shill >= i.cost and i.inStock > 0):
                    print('\nYou bought a ',i.item.name)
                    inv.shillings(-i.cost)
                    inv.addItem(i.item, 1)
                    i.inStock -= 1
                elif(I.inStock <= 0):
                    print('\nThere were none left')
                else:
                    print('\nYou don'"'"'t have enough shillings')
            count += 1

sk = [Shopkeeper("Jeb", [
        ShopItem(item.items[0], 5, 2),
        ShopItem(item.food[1], 5, 1),
        ShopItem(item.food[2], 5, 1),
    ])]


#The user should buy items from shop
class Shop():
    def open(self, seller, inv):
        shopping = True
        while(shopping == True):
            print(inv.shill)
            seller.printItems()
            print('\nFeel free to browse my wares.')
            seller.selectItem(inv)
            print('e - Exit')
            p = input('Purchase: ')
            if (p == 'e'):
                print()
                shopping = False
    def getShopkeeper(self, num):
        return sk[num]

#Shop.open(Shop.getShopkeeper(0), [])
