class Player():
    def __init__(self, location):
        """ stats for player character and wumpus """
        self.location = location

        # You can't make dead people, sorry
        self.alive = True
        self.has_gold = False

        # clockwise
        self.n = 0 # used as index for d and c
        self.d = ["east", "south", "west", "north"]
        self.direction = self.d[0] # east

        self.c = ["[>]", "[v]", "[<]", "[^]"]
        self.character = self.c[0] # >

    def right(self):
        """ turn right; Used by wumpus game driver """
        self.n = (self.n + 1) % 4

        self.direction = self.d[self.n]
        self.character = self.c[self.n]

    def left(self):
        """ turn left; Used by wumpus game driver """
        self.n = (self.n - 1) % 4

        self.direction = self.d[self.n]
        self.character = self.c[self.n]

    def get_location(self):
        """ location of player """
        return self.location[0], self.location[1]
