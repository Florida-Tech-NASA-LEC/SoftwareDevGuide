class Mammal:
    def setLiveBirth(self, birth):
        self.liveBirth = birth

    def setHabitat(self, habitat):
        self.habitat = habitat

    def setNumOfLegs(self, n):
        self.legs = n

    def getLiveBirth(self):
        return self.liveBirth

    def getHabitat(self):
        return self.habitat

    def getNumOfLegs(self):
        return self.legs

class Dolphin(Mammal):
    def sonar(self):
        print "Dolphins can use echo location to find prey!"

class Dog(Mammal):
    def bark(self):
        print "Bork bork!"

class Echidna(Mammal):
    def layEgg(self):
        print "BLOOP!"

fido = Dog()
fido.setNumOfLegs(4)
fido.bark()

flipper = Dolphin()
flipper.setHabitat("Ocean")
flipper.sonar()
print flipper.getHabitat()

spike = Echidna()
spike.setLiveBirth(False)
if not spike.getLiveBirth():
    spike.layEgg()
