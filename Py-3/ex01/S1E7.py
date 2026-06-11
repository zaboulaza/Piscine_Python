from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, nom, is_alive=True):
        self.first_name = nom
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def __str__(self) :
        return self.__repr__()
    
    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"
        
    def die(self):
        self.is_alive = False

class Lannister(Character):
    """"""
    def __init__(self, nom, is_alive=True):
        self.first_name = nom
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        
    def die(self): 
        self.is_alive = False
        
    def __str__(self) :
        return self.__repr__()
    
    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    @classmethod
    def create_lannister(cls, nom, is_alive=True):
        return (cls(nom, is_alive))
