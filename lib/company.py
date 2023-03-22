from .freebie import Freebie
from .dev import Dev

class Company:

    all_companies = []

    def __init__( self, name:str, year:int ):
        self.name = name
        self.year = year

        Company.all_companies.append(self)
        
    @property
    def freebies( self ):
        return [ freebie for freebie in Freebie.all_freebies if freebie.company == self ]

    @property
    def devs( self ):
        return [ freebie.dev for freebie in self.freebies ]
    
    def give_freebie(self, dev, item_name:str, value):
            Freebie(dev, self, item_name, value)

    @classmethod
    def oldest_company( cls ):
        year = 3000
        oldest = ''
        for company in cls.all_companies:
             if company.year < year:
                year = company.year
                oldest = company
        return oldest