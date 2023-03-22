from .freebie import Freebie

class Dev:

    all_devs = []

    def __init__( self, name:str ):
        self.name = name
        Dev.all_devs.append(self)

    @property
    def freebies( self ):
        return [ freebie for freebie in Freebie.all_freebies if freebie.dev == self ]
    
    @property
    def companies( self ):
        return [ freebie.company for freebie in self.freebies]
    
    def received_one(self, item_name):
        for item in self.freebies:
            return item_name == item.item_name
        
    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev
            print(f"Your freebie was given to {dev.name}")
        else:
            print("That doesn't belong to you!")

        
