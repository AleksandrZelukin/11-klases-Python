class Skolens:
    def __init__(self,vards,klase):
        self.vards = vards
        self.klase = klase
    def drukat(self):
        print(f"Skolens vards: {self.vards}, klase: {self.klase}")
        
skolens1 = Skolens("Jānis", "10.A")
skolens2 = Skolens("Anna", "9.B")
skolens3 = Skolens("Pēteris", "11.C")
skolens1.drukat()
skolens2.drukat()
skolens3.drukat()