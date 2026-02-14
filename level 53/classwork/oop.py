# Object Oriented Programming
class fighter:
    pass

samurai = fighter()
print(type(samurai))
ninja = fighter()


def __init__(self, health, damage, speed):
    self.health = health
    self.damage = damage
    self.speed = speed
samurai = fighter("samurai", 220, 40, 25)
ninja = fighter("ninja", 400, 20, 100)
print(samurai.name)
print(samurai.health)
print(samurai.speed)
print(samurai.damage)

print(ninja.name)
print(ninja.health)
print(ninja.speed)
print(ninja.damage)


class medic:
    def heal_up():
        print("healed up")
        




