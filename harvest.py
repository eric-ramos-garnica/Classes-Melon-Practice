############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless= is_seedless
        self.is_bestseller = is_bestseller
        self.name=name
        
        

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        #pairing = [mint,straberries,prosciutto,ice cream]
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest
    def __str__(self):
        
        return f'{self.code} {self.first_harvest} { self.color} {self.is_seedless} {self.is_bestseller} {self.name} {self.pairings}'



def make_melon_types():
    """Returns a list of current melon types."""
#[muskmelon,]
    musk_melon = MelonType('musk',1998,'green','seedless','bestseller',"Muskmelon")
    musk_melon.add_pairing("mint")
    Casaba = MelonType("cas",2003,"orange", "has seeds", 'sf','Casaba')
    Casaba.add_pairing("strawberries")
    crenshaw = MelonType("cre",1996,"green", "has seeds",'sd',"Crenshaw")
    crenshaw.add_pairing ("prosciutto")
    yellow_watermelon = MelonType("yw",2013,"yellow", "has seeds", "bestseller", "Yellow Watermelon")
    yellow_watermelon.add_pairing ("ice cream")
    all_melon_types =[musk_melon,Casaba,crenshaw,yellow_watermelon]
    
    return all_melon_types
    
    # Fill in the rest


def print_pairing_info(melon_types): 
#melon_types[musk_melon,Casaba,crenshaw,yellow_watermelon]
#pairing = [mint,straberries,prosciutto,ice cream]

    """Prints information about each melon type's pairings."""
    for idx in range(0,len(melon_types)):         
            if(melon_types[idx].name == "Casaba"):
                print(f"{melon_types[idx].name} pairs with")
                print(f"- {melon_types[0].pairings[0]}")
                print(f"- {melon_types[idx].pairings[0]}")
            else:    
                print(f"{melon_types[idx].name} pairs with")
                print(f"- {melon_types[idx].pairings[0]}")
    
    
              
    
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dic ={
        "musk": melon_types[0],
        "cas": melon_types[1], 
        "cre": melon_types[2],
        "yw": melon_types[3] 
        }
    return(melon_dic)


array_obj = make_melon_types()

print_pairing_info(array_obj)



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest