import random

class RandomAngka:
    def __init__(self, angka=None):
        if(angka is None):
            angka = self.generateAngka()
        self.angka = angka
        
    def generateAngka(self,min=1,max=100):
        return random.randrange(min,max)