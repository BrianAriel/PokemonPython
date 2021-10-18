from constants import *
from models import *

#First, we define pokemon with its stats

pokemon1 = Pokemon("Bulbasur",100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

#Second, stats
pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTCK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTCK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}