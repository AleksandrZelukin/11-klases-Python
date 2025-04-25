class Skolnieks:
    def __init__(self, vards, klase):
        self.vards = vards
        self.klase = klase
    def ievadi_datus():
        vards = input("Ievadi skolnieka vārdu: ")
        klase = input("Ievadi klasi, kurā mācās: ")
        return Skolnieks(vards, klase)
    def izdrukat_datus(self):
        return f"Skolnieks {self.vards} mācās {self.klase} klasē."

class Skolotajs:
    def __init__(self, vards, klase,prieksmets):
        self.vards = vards
        self.klase = klase 
        self.prieksmets = prieksmets  
    def ievadi_datus():
        vards = input("Ievadi skolotāja vārdu: ")
        klase = input("Ievadi klasi, kurā mācā: ")
        prieksmets = input("Ievadi priekšmetu: ")
        return Skolotajs(vards, klase, prieksmets)
    def izdrukat_datus(self):
        return f"Skolotājs {self.vards} māca {self.klase} klasē {self.prieksmets} priekšmetu."
        
        
class Prieksmets:
    def __init__(self, nosaukums, klase):
        self.nosaukums = nosaukums
        self.klase = klase
        
    def ievadi_datus(self):
        self.nosaukums = input("Ievadi priekšmeta nosaukumu: ")
        self.klase = input("Ievadi klasi: ")
        
    def izvadit_datus(self):
        print("Priekšmeta nosaukums:", self.nosaukums)
        print("Klase:", self.klase)
        
class Klase:   
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        
    def ievadi_datus(self):
        self.nosaukums = input("Ievadi klases nosaukumu: ")
        
    def izvadit_datus(self):
        print("Klases nosaukums:", self.nosaukums)
        
class Skola:   
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        
    def ievadi_datus(self):
        self.nosaukums = input("Ievadi skolas nosaukumu: ")
        
    def izvadit_datus(self):
        print("Skolas nosaukums:", self.nosaukums)
        

sk=Skolnieks.ievadi_datus() 

sl=Skolotajs.ievadi_datus()
print(sk.izdrukat_datus())
print("un")
print(sl.izdrukat_datus())