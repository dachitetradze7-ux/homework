class Gamer:
    count = 0
    def  __init__(self, game, time_played):
        self.favouirte_game = game
        self.hours = time_played
        

    def play(self):
        self.hours += 1

    @classmethod
    def count_gamers(cls):
        print(cls.count)

irakli = Gamer("roblox", 100)
zurabi = Gamer("RDR2", 200)
dachi = Gamer("RDR2", 1000)

# dachi.play()
# dachi.play()
# dachi.play()
# dachi.play()

# Gamer.play(dachi)
# print(dachi.hours)

# class figther:
#     def __init__(self ,health, damage, speed):
#         self.health = health
#         self.damage = damage
#         self.speed = speed

# class archer(figther):
#     def __init__(self, health, damage, speed, range, reload):
#         super(). __init__( health, damage, speed)
#         self.reload = reload

# wizard = archer(30, 50, 20, 100, 20)
# print(wizard.damage)
# print(wizard.speed)
# print(wizard.health)












    





