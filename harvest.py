############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        
        return self.pairings

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        return self.code


def make_melon_types():
    """Returns a list of current melon types."""

    musk = MelonType(
        'musk', 1998, 'green', True, True, "Muskmelon"
    )
    casaba = MelonType(
        'cas', 2003, 'orange', False, False, 'Casaba'
    )
    crenshaw = MelonType(
        'cren', 1996, 'green', False, False, 'Crenshaw'
    )
    y_water = MelonType(
        'yw', 2013, 'yellow', False, True, 'Yellow Watermelon'
    )

    all_melon_types = [musk, casaba, crenshaw, y_water]
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings: 
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melons_info = {}

    for melon in melon_types:
        melons_info[melon.code] = (melon.first_harvest, melon.color, melon.is_seedless, melon.is_bestseller, melon.name)

    return melons_info

############
# Part 2   #
############


class Melon(MelonType):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, field, harvester):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3
            

    # if both its shape and color ratings are greater than 5 = True
    # not from field 3
    

def make_melons():
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon1 = Melon('yw', 8, 7, 2, 'Sheila')
    melon2 = Melon('yw', 3, 4, 2, 'Sheila')
    melon3 = Melon('yw', 9, 8, 3, 'Sheila')
    melon4 = Melon('cas', 10, 6, 35, 'Sheila')
    melon5 = Melon('cren', 8, 9, 35, 'Michael')
    melon6 = Melon('cren', 8, 2, 35, 'Michael')
    melon7 = Melon('cren', 2, 3, 4, 'Michael')
    melon8 = Melon('musk', 6, 7, 4, 'Michael')
    melon9 = Melon('yw', 7, 10, 3, 'Sheila')

    return [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    melons = make_melons()

    for melon in melons:
        if melon.is_sellable():
            sellability ='(CAN BE SOLD)'
        else:
            sellability = '(NOT SELLABLE)'

        print(f'Harvested by {melon.harvester} from field {melon.field} {sellability}')
        # if melon.is_sellable():
        #     print('(CAN BE SOLD')
        # else:
        #     print('(NOT SELLABLE)')


