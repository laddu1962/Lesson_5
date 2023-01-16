import random

# exercise 2

class Collectibles:
    total_points = 0

    def __init__(self, name):
        self.name = name
        self.value = 0

    def collect(self):
        Collectibles.total_points += self.value

class Coin(Collectibles):

    def __init__(self, name, value):
        Collectibles.__init__(self, name)
        self.value = value


class Potion(Collectibles):
    colours = ["Red", "Blue", "Green", "Yellow"]
    def __init__(self, name , value):
        Collectibles. __init__(self, name)
        self.value = value
        self. colours = random.choice(Potion.colours)


coin = Coin("coin", 1)
potions = Potion("potion", 1)
print(vars(potions))
print(vars(coin))

# test
while Collectibles.total_points < 300:
    choice = input("Enter a number between 1 and 6")
    if not choice.isdigit():
        print("That is not a number, you failed")
        break
    if choice.int() >6:
        print("That number is too high")
        break
    if choice.int() <=3:
        coin = Coin



# Exercise 1

class Enemy:

    weapons = {"dagger": 5, "sword": 10, "lightsaber": 15}

    names = ["Edwin", "Harry", "Ben", "Katie"]
    homelands = ["Sheffield", "Uxbridge", "Riverdale", "West London"]
    ability = ["The hook", "Dragon Breath", "Bankai", "Prime Minister"]

    def __init__(self, name, homeland, ability):
        self.name = name
        self.homeland = homeland
        self.ability = ability

    def Set_Bio(self, bio):
        if not isinstance(bio, str):
            print("bio must be a string")
            return
        self.bio = bio

    def Get_Bio(self):
        return self.bio

    def GetRandomWeapon(self):
        self.weapon = random.choice(list(Enemy.weapons.items()))

for i in range(4):
    name = Enemy.names[i]
    homeland = random.choice(Enemy.homelands)
    ability = random.choice(Enemy.ability)
    enemy = Enemy(name, homeland, ability)
    enemy.GetRandomWeapon()
    print("{} is from {} with the ability of {}".format(name, homeland, ability))


print(vars(enemy))

#enemy1 = Enemy("Jeff","Liverpool","Flying")
#enemy1.Set_Bio("This enemy is great")
#enemy1.GetRandomWeapon()
#print(vars(enemy1))
#enemy2 = Enemy("Pep","Southampton","Instant Death")
#enemy2.Set_Bio("This enemy is great")
#enemy2.GetRandomWeapon()
#print(vars(enemy2))


