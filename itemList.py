import ItemClasses
item = ItemClasses
#Items lists
weapons = [item.Sword('0','None',0,0,''),
           item.Sword('1','Lief',500,5,'Legendary sword of the Scion.'),
           item.Dagger('2','Hunting Knife',5,1,'A knife used to hunt insects.'),
           item.Sword('3','Relic Sword', 10,3, '',),
           item.Spear('4','Relic Spear',8,3, ''),
           item.Axe('5','Relic Axe', 12,4, ''),
           item.Mace('6','Old Club', 10,4,''),
           item.Staff('7','Crooked Stick', 3,2, ['0'],[''],''),
           item.Bow('1','Training Bow', 20,2, 'A large bow made for practice.'),
           item.Crossbow('1','Training Crossbow', 20,2, ''),
           item.Sling('1','Grass Sling', 20,2, 'A sling made from grass; not very practical'),
           item.Shield('1','Wooden Shield', 20,4,'A basic round wooden shield.'),
           item.Wand('1','Poison wand', 1, '1', 'Poison Nettle', 'A wand containing a weak poison'),
           item.Staff('8', 'Mushroom staff',  3,2, ['2', '3', '4'],['Grow mushrooms','Grow mushrooms','Grow mushrooms'],'')
           ]

armours = [item.Hat('1','None',0,0,''),
           item.Shirt('1','Old Tunic', 1,1,'An old shirt with holes in it.'),
           item.Shirt('2', 'Travelling Cloak', 10,10,'A too large black cloak. Good for keeping ou of sight but heavy.'),
           item.Trousers('1','Worn Trousers', 1,1,'An old pair of trousers long past their prime')
           ]
food = [item.Food('1','Blackberry',1,5),
        item.Food('2','Dried Fruit',1,5),
        item.Food('3','Hazelnut',1,5),
        item.Food('4', 'Mushroom', 1,5),
        item.Food('5', 'Raw Bug Meat',3,10),
        item.Food('6', 'Brown Bread',3,50)
        ]
projec = [item.Arrow('1','Primitive Arrow', 10,1,'Arrows made from stone heads and twigs.'),
          item.Toss('2','Rope Net', 0,1, 'A rope net to catch your enemies.'),
          item.Bolt('3','Wooden Bolt', 10,1,''),
          item.Stone('4','Softstone', 10,1,'')
          ]
items = [item.Healing('1', 'Bandage', 10,1, 'A cloth bandage to treat wounds')
         ]
