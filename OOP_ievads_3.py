class TransportLidzeklis:
    def __init__(self,razotajs,gads):
        self.razotajs=razotajs
        self.gads=gads
    def paradi_info(self):
        return f"Ražotājs: {self.razotajs}, Gads: {self.gads}"
    
class ElektroTransportLidzeklis(TransportLidzeklis):
    def __init__(self, razotajs, gads, baterijas_veids):
        super().__init__(razotajs, gads)
        self.baterijas_veids = baterijas_veids
    def paradi_info(self):
        pamat_info = super().paradi_info()
        return f"{pamat_info}, Akumulatora veids: {self.baterijas_veids}"
class DziedDzensTransportLidzeklis(TransportLidzeklis):
    def __init__(self, razotajs, gads, degvielas_tips):
        super().__init__(razotajs, gads)
        self.degvielas_tips = degvielas_tips
    def paradi_info(self):
        pamat_info = super().paradi_info()
        return f"{pamat_info}, Degvielas tips: {self.degvielas_tips}"
# Piemēra izmantošana
elektro_auto = ElektroTransportLidzeklis("Tesla", 2020, "Litija-jona")
dzied_dzens_auto = DziedDzensTransportLidzeklis("Toyota", 2018, "Benzīns")  
print(elektro_auto.paradi_info())
print(dzied_dzens_auto.paradi_info())