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
    # def __str__(self):
        
    #     return f'{self.code} {self.first_harvest} { self.color} {self.is_seedless} {self.is_bestseller} {self.name} {self.pairings}'



def make_melon_types():
    """Returns a list of current melon types."""
#[muskmelon,]
    musk_melon = MelonType('musk',1998,'green','seedless','bestseller',"Muskmelon")
    musk_melon.add_pairing("mint")
    Casaba = MelonType("cas",2003,"orange", "has seeds", 'sf','Casaba')
    Casaba.add_pairing("mint")
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
                count =0
                while count <len(melon_types[idx].pairings)-1:
                    print(f"{melon_types[count].name} pairs with")
                    print(f"- {melon_types[count].pairings[count]}")
                    print(f"- {melon_types[idx].pairings[count +1]}")
                    count +=1
            else:    
                print(f"{melon_types[idx].name} pairs with")
                print(f"- {melon_types[idx].pairings[0]}")
    
    
              
    
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dic ={}
    for obj in melon_types:
        melon_dic[obj.code] = obj.name
    # for key,value in melon_dic.items():
    #     print(f'{key}======= {value}')
    return(melon_dic)





############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self,melon_type,shape_rating,color_rating,filed,Harvested_by ):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.filed = filed
        self.Harvested_by = Harvested_by

    def is_sellable(self):
        """Determine whether this melon can be sold."""
        if self.shape_rating > 5 and self.color_rating > 5 and self.filed != 3:
            return True
        else:
            return False
            
            



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_by_id = make_melon_type_lookup(melon_types)

    # Fill in the rest
    array_melons = []

    melon1 = Melon(melon_by_id["yw"],8,7,2,"Harvested by Sheila")
    array_melons.append(melon1 )
    melon2 = Melon(melon_by_id["yw"],3,4,2,"Harvested by Sheila")
    array_melons.append(melon2 )
    melon3 = Melon(melon_by_id["yw"],9,8,3,"Harvested by Sheila")
    array_melons.append(melon3 )
    melon4 = Melon(melon_by_id["cas"],10,6,35,"Harvested by Sheila")
    array_melons.append(melon4 )
    melon5 = Melon(melon_by_id["cre"],8,9,35,"Harvested by Michael")
    array_melons.append(melon5 )
    melon6 = Melon(melon_by_id["cre"],8,2,35,"Harvested by Michael")
    array_melons.append(melon6 )
    melon7 = Melon(melon_by_id["cre"],2,3,4,"Harvested by Michael")
    array_melons.append(melon7 )
    melon8 = Melon(melon_by_id["musk"],6,7,4,"Harvested by Michael")
    array_melons.append(melon8 )
    melon9 = Melon(melon_by_id["yw"],7,10,3,"Harvested by Michael")
    array_melons.append(melon9 )
    
    return array_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    #melons = [melon1,melon2,melon3 ..]
   
    for melon in melons:
      
        if melon.is_sellable() == True:
            sellable = 'CAN BE SOLD'
        else:
            sellable = 'NOT SELLABLE'
    
        print(f'{melon.Harvested_by} from Field {melon.filed} ({sellable})')
        




array_melons =make_melons(make_melon_types())
get_sellability_report(array_melons)