class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 10
        self.chakra = 10
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nChakra: {self.chakra}")

    def attack( self , pirate ):
        pirate.health -= self.strength
        self.chakra += 5
        return self

    def shuriken(self , pirate):
        if self.chakra >= 5 and pirate.health >= 0 :
            pirate.health -= (self.strength * self.speed * 0.4)
            self.chakra -= 5
            print("POW!!!!!")
        else :
            pirate.death()  
            print("Attack Failed. Insufficent chakra.")
        pirate.show_stats()
        self.show_stats()
        return self

    def meditate(self):
        self.health += 10
        self.chakra += 5
        self.show_stats
        return self

    def death(self):
        if self.health <= 0:
            print("Ninja has died! Pirate wins!")
        return self