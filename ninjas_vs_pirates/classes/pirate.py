class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        #self.max_health = 100

        

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        ninja.show_stats()
        self.show_stats()
        return self

    #Mana or health gain from drinking rum
    #def rum (self):
    #    self.health += 10
    #    SUEDO CODE FOR MAINTAING MAX HEALTH AFTERE HEAL
    #    if self.health >= self.max_health
    #        self.health = self.max_health
    #    if self.health <80
    #        print("You are sufficiently drunk now!")  #THIS SENARIO, HEALTH IS ALSO HOW DRUNK
    #    return self                                   #YOU ARE

    #sword attack
    #could use stength and speed for attack
    #def attack_sword(self, ninja):
        #if ninja.health > 0:
            #ninja.health -= self.strength and self.speed


    #borken bottle attack
    #only works is health/drunk level is high enough (last resort is the bottle)
    #def attack_bottle(self, ninja):
    #   if ninja.health > 0:
    #   


    def death(self):
        if self.health <= 0:
            print("JackSparrow has died! Ninja wins!")
        return self