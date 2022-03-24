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
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melons_info = {}

    for melon in melon_types:
        melons_info[melon.code] = (melon.first_harvest, melon.color, melon.is_seedless, melon.is_bestseller, melon.name)

    return melons_info

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



