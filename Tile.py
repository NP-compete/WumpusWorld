class Tile():
    def __init__(self, visited=False, wumpus=False, pit=False, gold=False, player=False, smell=False, breeze=False):
        """ Each tile on the board is this """
        self.visited = visited
        self.wumpus = wumpus
        self.smell = smell
        self.pit = pit
        self.breeze = breeze
        self.gold = gold
    
    def add_wumpus(self):
        """ add wumpus to current tile """
        self.wumpus = True

    def add_pit(self):
        """ adds pit to the current tile """
        self.pit = True

    def add_breeze(self):
        """ breeze intended to be added by wumpus class, after deciding where pits reside """
        self.breeze = True

    def add_smell(self):
        """ smell inteded to be added by wumpus class, after deciding where the wumpus resides """
        self.smell = True

    def add_gold(self):
        """ place a gold for someone to find """
        self.gold = True
    
    def visit(self):
        """ you have visited the tile """
        self.visited = True

    def has_hazard(self):
        """ hazards indicate danger, but do not cause death """
        return self.smell or self.breeze

    def has_death(self):
        """ beware these tiles """
        return self.wumpus or self.pit
    
    def has_gold(self):
        """ congrats! you win the game """
        return self.gold

    def to_string(self):
        """ printable version of the dangers and hazards """

        s = ""
        # a tile can possibly contain =  WsPbG
        # W = wumpus
        # s = Smell
        # P = Pit
        # b = Breeze
        # G = Gold
        
        # Used for printing purposes only
        # upper case for fatal dangers
        # lower case for dangerous indicators

        if self.wumpus:
            s += "W"
        if self.smell:
            s += "s"
        if self.pit:
            s += "P"
        if self.breeze:
            s += "b"
        if self.gold:
            s += "G"

        return s

