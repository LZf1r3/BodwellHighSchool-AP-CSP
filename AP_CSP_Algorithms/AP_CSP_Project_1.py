"""
LZ's AP CSP Project 1
RPG Game
"""

import random
import os

class Attacks:
    def __init__(self, name, damage, uses):
        self.name = name
        self.damage = damage
        self.uses = uses

    def usable(self):
        if self.uses >= 0:
            return True
        else:
            return False
        
class Classes:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

class Monster:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.set_life = health

attacks = [Attacks("Fireball ", 3, 3), Attacks("Slash", 5, 5), Attacks("Backstab", 4, 4), Attacks("Frostbolt", 2, 6), Attacks("Smash", 6, 2), Attacks("Lunge", 3, 4), Attacks("Dart", 4, 3), Attacks("Blackhole", 999, 1)]

classes = [Classes("Mage", 35, [attacks[0], attacks[3], attacks[7]]), Classes("Warrior", 67, [attacks[1], attacks[4], attacks[5]]), Classes("Rogue", 40, [attacks[2], attacks[5], attacks[6]])]

class Player:
    def __init__(self, name, _class, health, attacks):
        self.name = name
        self._class = _class
        self.health = health
        self.attacks = attacks
        self.set_life = health
    
    def fight(self, enemy):
        os.system("cls")   
        print(f"You have encountered a {enemy.name} with {enemy.health}HP")
        while True:
            if self.health <= 0:
                print("YOU HAVE BEEN DEFEATED")
                break
            
            elif enemy.health <= 0:
                print(f"YOU HAVE DEFEATED THE {enemy.name}")
                break
            
            else:
                attack()
                print("Choose your attack (The index):")
                for i in range(len(self.attacks)):
                    print(f"{i+1}. {self.attacks[i].name} | Uses left: {self.attacks[i].uses}")
                choice = int(input("User .:"))
                os.system("cls")
                while choice-1 not in range(len(self.attacks)):
                    print("Invalid input. Try again: ")
                    choice = int(input("User .:"))
                for n, __attack in enumerate(self.attacks):
                    if choice-1 == n:
                        if __attack.uses >0:
                            __attack.uses -= 1
                            enemy.health -= __attack.damage
                            print(f"You have chosen {__attack.name}!\nYou dealt {__attack.damage} damage \nPlayer HP: {self.health} | {enemy.name} HP: {enemy.health}")
                        else:
                            print("You wasted your turn trying an over-used attack!")


    """
    def fight(self, enemy):
        print(f"You must defeat a(n) {enemy.name} to proceed")
        while self.health > 0 and enemy.health>0:
           print(f"Player: HP({self.health}/{self.set_life}) Monster: 
           HP({self.health}/{self.set_life})")
            self.attack(self, enemy)
    """ 

def generate_monster():
    monsters_list = [Monster("Goblin", random.randint(1,25), [attacks[1],attacks[6],attacks[2]]), Monster("Orc", 50, [attacks[4],attacks[5]]), Monster("Dragon",80, [attacks[0],attacks[1],attacks[4],attacks[7]]),Monster("Pleasant",10,[attacks[2],attacks[6]])]
    return random.choice(monsters_list)

def choose_class():
    print("choose your class and attacks for this run:\n")

    options = []
    for i in classes:
        options.append(i.name.lower())

    for i in range(len(classes)):
        print(f"{i + 1}. {classes[i].name} (Health: {classes[i].health})")
        for j in range(len(classes[i].attacks)):
            print(f"   {j + 1}. {classes[i].attacks[j].name} (Damage: {classes[i].attacks[j].damage}, Uses: {classes[i].attacks[j].uses})")
        print('\n')
    
    choice = str(input("Type the name of the desired class: ")).lower()

    while choice not in options:
        print("Invalid class, please choose an adequate one!")
        choice = str(input("User .:"))

    else:
        print(f"Class Selected: {choice}")
        for i in classes:
            if i.name.lower() != choice:
                classes.remove(i)
        return i

def attack(enemy,player):
        attack = random.choice(enemy.attacks)
        print(f"{enemy.name} have used {attack.name}")
        player.health -= attack.damage
    
if __name__ == "__main__":
    print("Welcome to LZ's RPG")
    player = Player(str(input("Enter your character's name: ")),choose_class().name,classes[0].health, classes[0].attacks)
    player.fight(generate_monster())
