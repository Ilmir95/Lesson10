from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    @abstractmethod
    def calculate(self):
        pass
class Coat(Clothes):
    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)
class Suit(Clothes):
    @property
    def calculate(self):
        return round((self.param * 2) + 0.5 )
coat = Coat(70)
suit = Suit(150)
print(coat.calculate)
print(suit.calculate)