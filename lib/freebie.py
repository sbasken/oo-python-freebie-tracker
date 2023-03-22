
class Freebie:

    all_freebies = []
    
    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company        
        self.item_name = item_name
        self.value = value

        Freebie.all_freebies.append(self)

    #f"{dev name} owns a {freebie item_name} from {company name}"
    def print_details( self ):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"