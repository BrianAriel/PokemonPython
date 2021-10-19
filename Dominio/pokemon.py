from constants import *


class Pokemon:
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = [] #Vector de ataques
        self.stats = {}
        self.baseStats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = 0

    def compute_stats(self):
        self.stats = {
            HP: self.compute_hp_stat(),
            ATTACK: self.compute_standard_stat(ATTACK),
            DEFENSE: self.compute_standard_stat(DEFENSE),
            SPATTCK: self.compute_standard_stat(SPATTCK),
            SPDEFENSE: self.compute_standard_stat(SPDEFENSE),
            SPEED: self.compute_standard_stat(SPEED)
        }

    def compute_standard_stat(self, stat):
        value1 = (2 * self.baseStats[stat] + self.iv[stat] + int(self.ev[stat] / 4)) * self.level
        return (int(value1 / 100) + 5) * NATURE_MATRIX[self.nature][stat]

    def compute_hp_stat(self):
        value1 = (2 * self.stats["HP"]+self.iv["HP"]+int(self.ev["HP"]/4)) * self.level
        return int(value1 / 100) + self.level + 10


class Attack:
    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy





















