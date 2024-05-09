import random

class Character:
    def __init__(self, name, race, hp, strength):
        self.name = name
        self.race = race
        self.hp = hp
        self.strength = strength
        

    
    def attack(self):
        return random.randint(1, self.strength)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0
    
    def __str__(self):
        return f"{self.name} (Race: {self.race}, HP: {self.hp}, Strength: {self.strength})"

class Monster(Character):
    def __init__(self, name, hp, strength, loot):
        super().__init__(name, hp, strength)
        self.loot = loot
    
    def drop_loot(self):
        return self.loot

class Player(Character):
    def __init__(self, name, race, hp, strength, gold=0):
        super().__init__(name, race, hp, strength)
        self.gold = gold
    
    def add_gold(self, amount):
        self.gold += amount