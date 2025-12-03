class MajasDzivnieks:
    def dz(self):
        pass
    
class Kakis(MajasDzivnieks):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dz(self):
        return f"Manam kaķim {self.name} ir {self.age} gadi"
    
class Suns(MajasDzivnieks):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dz(self):
        return f"Manam suniem {self.name} ir {self.age} gadi"
        
       
dzivnieks1 = Kakis("Barsik", 2)
dzivnieks2 = Suns("Reks",4)

print(dzivnieks1.dz())
print(dzivnieks2.dz())