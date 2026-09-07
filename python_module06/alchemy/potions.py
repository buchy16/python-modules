from .elements import creat_fire, creat_air, creat_earth, creat_water


def healing_potion():
    return f"Healing potion brewed with {creat_fire()} and {creat_water()}"


def strength_potion():
    return f"Strength potion brewed with {creat_earth()} and {creat_fire()}"


def invisibility_potion():
    return f"Invisibility potion brewed with {creat_air()} and {creat_water()}"


def wisdom_potion():
    return f"Wisdom potion brewed with all elements: \
{creat_fire()}, {creat_air()}, {creat_earth()} and {creat_water()}"
