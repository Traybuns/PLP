class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self._power = power         
        self.strength = strength

    def display_info(self):
        print(f"{self.name} has {self._power} powers and strength level {self.strength}.")

    def attack(self):
        print(f"{self.name} attacks using {self._power} ")


class FlyingHero(Superhero):
    def __init__(self, name, power, strength, speed):
        super().__init__(name, power, strength)
        self.speed = speed

    def fly(self):
        print(f"{self.name} is flying at speed {self.speed} km/h")

    def attack(self):  
        print(f"{self.name} swoops in with a flying strike using {self._power}")

hero1 = Superhero("Photon Girl", "Light Manipulation", 90)
hero2 = FlyingHero("Falcon Blaze", "Fire Wings", 85, 200)

hero1.display_info()
hero1.attack()
print("-----")
hero2.display_info()
hero2.fly()
hero2.attack()
