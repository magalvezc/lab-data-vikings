# Soldier
class Soldier:
    def __init__(self, health, strenght):
        self.health = health
        self.strenght = strenght
    
    def attack(self):
        return self.strenght
    
    def receive_damage(self,damage):
        self.health -= damage
        
    pass

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strenght):
        self.name = name
        super().__init__(health, strenght)
    
    def receive_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            return f'{self.name} has received {self.damage} points of damage'
        
        if self.health < 0:
            return f'{self.name} has died in act of combat'
    
    def battle_cry(self):
        return 'Odin Owns you all'
    
    pass

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strenght):
        super().__init__(self, health, strenght)
    
    def receive_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            return f'A Saxon has received {self.damage} points of damage'
        
        if self.health < 0:
            return f'A Saxon has died in act of combat'
            
    pass

# War
class War:
    def __init__(self):
        vikingArmy = []
        saxonArmy = []
    
    def add_Viking(self, Viking): #falta realizar cada interación para agregar más de 1
        vikingArmy.append(Viking)
        
    def add_Saxon(self, Saxon): #falta realizar cada interación para agregar más de 1
        saxonArmy.append(Saxon)
        
    def viking_attack(self):
        if Saxon.health() == Viking.strenght():
            saxonArmy.remove()
        return Saxon.received_damage()
    
    def saxon_attack(self):
        if Vikin.health() == Saxon.strenght():
            vikingArmy.remove()
        return Viking.received_damage()
        
    pass
