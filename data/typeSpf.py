import enum

#enumerated classes
class SpecialType1(enum.Enum):
    manuver = 1
    spell = 2
class SpecialType2(enum.Enum):
    automatic = 1
    offence = 2
    support = 3
    enhance = 4
class AttackType(enum.Enum):
    single = 1
class SpellType(enum.Enum):
    Nature = 1
    Blessing = 2
    Shape_shifting = 3
    Animation = 4
    Illusion = 5
    Curse = 6
class CombatStatus(enum.Enum):
    Normal = 1
    Attacking = 2
    RAttacking = 3
    Blocking = 4
    Specializing = 5
    Using = 6
    Escaping = 7
    Countered = 8
    Parried = 9
class ArmourType(enum.Enum):
    hat = 1
    shirt = 2
    trousers = 3
class Weapon1Type(enum.Enum):
    sword = 1
    dagger = 2
    spear = 3
    axe = 4
    mace = 5
    staff = 6
class Weapon2Type(enum.Enum):
    bow = 1
    crossbow = 2
    sling = 3
    shield = 4
    wand = 5
class ProjectileType(enum.Enum):
    arrow = 1
    bolt = 2
    stone = 3
    toss = 4
class ItemType(enum.Enum):
    food = 1
    healing = 2
    status = 3
    ingredient = 4
