class Parrents():
    def __init__(self,Eays, Head):
        self.Eays = Eays
        self.Head = Head

class Kids(Parrents):
    def __init__(self, Eays, Head, Skill):
        super().__init__(Eays, Head)
        self.Skill = Skill

        

