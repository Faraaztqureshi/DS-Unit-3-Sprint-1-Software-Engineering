from random import randint

class Product:
    '''The Acme Product class which contains important information
    about products
    '''
    def __init__(self, name= None, price = 10, weight = 20, flammability = 0.5,
                 identifier = None):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def stealability(self):
        '''Calculates the price divided by weight
        '''
        stealability = self.price / self.weight
        if 0 < stealability < 0.5:
            return print("Not so stealable...")
        elif 0.5 <= stealability < 1.0:
            return print("Kinda stealable.")
        else:
            return print("Very stealable!")
    
    def explode(self):
        '''Calculates the flammability times weight
        '''
        goes_boom = self.flammability * self.weight
        if goes_boom < 10:
            return print("...fizzle.")
        if 10 <= goes_boom < 50:
            return print("...boom!")
        else:
            return print("...BABOOM!!")
    
class BoxingGlove(Product):
    '''The BoxingGlove class contains specific informatin
    about boxing gloves
    '''
    def __init__(self, weight = 10):
      super().__init__()
      self.weight = 10
    
    def explode(self):
        return print("...it's a glove.")
    
    def punch(self):
        if self.weight < 5:
            return print("That tickles.")
        elif 5 <= self.weight < 15:
            return print("Hey that hurt!")
        else:
            return print("OUCH!")

