class Player:
    def __init__(self, speed, run):
        self.speed = speed
        self.run = run
        print("Быстрые игроки!")
class Zashitnik(Player):
    def __init__(self, attention, speed, run):
        super().__init__(speed,run)
        self.attention = attention
        print("Защитник внимательно играет!")
class Poluzashitnik(Player):
    def __init__(self, dexterity, speed, run):
        super().__init__(speed, run)
        self.dexterity = dexterity
        print("Полузащтник даёт пас!")
class Vratar(Player):
    def __init__(self, reaction, speed):
        super().__init__(speed,run=None)
        self.reaction = reaction
    def lovit_myach(self,lovit_maych):
        print("Вратарь ловит мяч!")

print(Zashitnik,Poluzashitnik,Vratar)
player1 = Zashitnik(attention="внимание", speed="скорость", run="бег")
player2 = Poluzashitnik(dexterity="ловкость", speed="скорость", run="бег")
player3 = Vratar(reaction="реакция", speed="скорость")
player3.lovit_myach("Вратарь ловит мяч")