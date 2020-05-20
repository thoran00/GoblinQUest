# classes and functions
import random
import sys

class Game_Objects:
    def __init__(self, name, health, desc):
        self.name = name
        self.health = health
        self.desc = desc

class Player(Game_Objects):
    def healing(self):
        w = random.randint(1, 3)
        if Main_Character.health < 5 and Main_Character.health > 0:
            if (w + self.health) > 5:
                self.health = 5
            else:
                self.health = self.health + w
            print("You just healed yourself for {} points!".format(w))
            print("Your health is now at {}.".format(Main_Character.health))
            Ezekiel.attack_player()
            return
        else:
            print("You are already at full health.")
            return
    def attack_enemy(self):
        w = random.randint(1, 3)
        x = random.randint(1, 5)
        if x == 5:
            print("You Missed!")
            Ezekiel.attack_player()
        else:
            if Ezekiel.health > 0:
                Ezekiel.health = Ezekiel.health - x
                print("You just hit the Goblin for {} points!".format(x))
                print("The Goblin's health is now at {}".format(Ezekiel.health))
                if Ezekiel.health <= 0:
                    print("The Goblin has been defeated.")
                    print("Congratulations, you have won Goblin Quest!")
                    game_over()
                else:
                    Ezekiel.attack_player()
    def death(self):
        while True:
            if self.health <= 0:
                print("You have been defeated")
                print("Game Over")
                sys.exit()
                return

class Goblin(Game_Objects):
    def got_killed(self):
        if self.health <= 0:
            print("The Goblin has been defeated.")
            print("Congratulations, you won Goblin Quest!")
            sys.exit()
            return
    def attack_player(self):
        g = random.randint(1, 3)
        Main_Character.health = Main_Character.health - g
        print("The Goblin has attacked you for {}!".format(g))
        print("Your health is now at", Main_Character.health)
        if Main_Character.health <= 0:
            return Main_Character.death()


def game_over():
    while True:
        print("Game Over")
        sys.exit()
        return

# This is the main function of the program, ie controls how the game is actually played
def action_board():
    while True:
        action = input("Please press y to attack, b to heal, or f to quit the game: ")
        if action == "y":
            Main_Character.attack_enemy()
        elif action == "b":
            Main_Character.healing()
        elif action == "f":
            game_over()
        else:
            print("Uh oh, that action doesn't exist. Please enter a listed action.")

# These are the characters
Ezekiel = Goblin("Goblin", 5, "A Foul Creature")
Main_Character = Player(input("What is your name? "), 5, "The Main Protagonist")

# This is the main program
print("Hello, {}! Welcome to Goblin Quest!".format(Main_Character.name))
print("Your health is at {}".format(Main_Character.health))
action_board()
