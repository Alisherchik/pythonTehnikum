class DreamTeam:
    def __init__(self, kick, run, stay):
        self.kick = kick
        self.run = run
        self.stay = stay

class Forvard(DreamTeam):
    def __init__(self, kick, run, stay, push):
        super().__init__(kick,run,stay)
        # super().__init__(kick, run, stay):
        # self.kick = kick
        # self.run = run
        # self.stay = stay
        self.push = push

class Player(DreamTeam):
    def __int__(self, kick, run, stay, stopball):
        super().__int__(kick,run,stay)
        self.stopball = stopball

class Goalkeeper(DreamTeam)
