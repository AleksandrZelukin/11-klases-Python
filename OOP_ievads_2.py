class Skolens:
    def __init__(self,vards,klase="1.A"):
        self.vards = vards
        self.klase = klase
    def drukat(self):
        print(f"Skolēns {self.vards} mācās {self.klase} klasē")
        
sk1 = Skolens("Jānis")
sk2 = Skolens("Anna", "6.B")

sk1.drukat()
sk2.drukat()

class Skolotajs:
    def __init__(self,uzvards,prieksmets):
        self.uzvards = uzvards
        self.prieksmets = prieksmets
    def drukat(self):
        print(f"Skolotājs {self.uzvards} māca priekšmetu: {self.prieksmets}")

skol1 = Skolotajs("Bērziņš", "Matemātika")
skol1.drukat()