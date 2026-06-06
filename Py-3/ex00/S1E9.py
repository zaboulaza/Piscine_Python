from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, nom, is_alive=True):
        pass
    
    @abstractmethod
    def die(self) :
        pass
    
class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, nom, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = nom
        self.is_alive = is_alive
        
    def die(self) : 
        """Your docstring for Method"""
        self.is_alive = False
        
#end