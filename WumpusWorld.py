from Tile import Tile
from Player import Player

class Wumpus():
    def __init__(self, size=10):
        """ Initiate a wumpus game, default size = 10 """
        self.size = size
        # Board determined by size
        # Initially blank board, but you can recall memories from your travels

        # remove visited=True, for a partially observable board
        self.world  = [ [ Tile() for t in range(size)] for i in range(size) ]
        # Board with all secrets uncovered
        # The teacher's manual of game boards
        #self.solved = [ [ Tile(visited=True) for t in range(size)] for i in range(size) ]
        
        self.player = Player([0, 0])
        self.world[2][2].add_wumpus()
        self.world[5][5].add_pit()
        self.world[3][3].add_gold()

        # generate random location for wumpus
        # wumpus is a non-moving player
        self.wumpus = Player([2, 2])

        # generate smells
        i, j = self.wumpus.location
        if self.wumpus.location[1] != 0:
            self.world[i][j-1].add_smell()
        if self.wumpus.location[1] != self.size - 1:
            self.world[i][j+1].add_smell()
        if self.wumpus.location[0] != 0:
            self.world[i-1][j].add_smell()
        if self.wumpus.location[0] != self.size - 1:
            self.world[i+1][j].add_smell()
        # generate pits

        # generate breezes

        for i in range(self.size):
            for j in range(self.size):
                if self.world[i][j].pit:
                    if j != 0:
                        self.world[i][j-1].add_breeze()
                    if j != self.size - 1:
                        self.world[i][j+1].add_breeze()
                    if i != 0:
                        self.world[i-1][j].add_breeze()
                    if i != self.size - 1:
                        self.world[i+1][j].add_breeze()
                   
            
        # generate random gold location, can be same as Wumpus
        
    
    def print_board(self):
        """ Printing the board, used for the wumpus world """
        for i in range(self.size):
            for j in range(self.size):
                if self.player.location == [i, j]:
                    print self.player.character,
                elif not self.world[i][j].visited:
                    print " # ",
                elif self.world[i][j].has_death():
                    print " & ",
                elif self.world[i][j].has_hazard():
                    print " ? ",
                elif self.world[i][j].has_gold():
                    print " $ ",
                else:
                    print " # ",
            print
    def message(self, msg1, msg2="", msg3=" "):
        """ output a message to the screen of a specific format 

        
        EXAMPLE
        ====================================
        | You are facing south [1, 2]
        | You move forward
        | It stinks in here!
        | You meet the Wumpus (RIP)
        | It's cold in here!
        | It's a long drop (RIP)
        | Oo shiny!
        | You found the gold! Congrats!
        =====================================

        """
        print "==========================================="
        print "|%s" % msg2 # status messages (location, contents of tile)
        print "|%s" % msg1 # main message
        for m in msg3:
            print "|%s" % m # personalized message based on context
        print "==========================================="
    def game_loop(self):
        """ Game driver """
        i, j = self.player.get_location()
        # resolve 
        last_cmd_msg = "Welcome to the Wumpus World"
        while self.player.alive and not self.player.has_gold:

            self.message(last_cmd_msg, "You are facing %s %s" % (self.player.direction, self.player.location))
            self.print_board()
            cmd = raw_input("> ")
            if cmd == "q":
                last_cmd_msg = "Good bye!"
                break

            # movement controls
            elif cmd == "f":
                # move forward
                d = self.player.direction
                if d == "west" and self.player.location[1] != 0:
                    self.player.location[1] -= 1
                    self.world[i][j].visited = True
                elif d == "east" and self.player.location[1] != self.size - 1:
                    self.player.location[1] += 1
                    self.world[i][j].visited = True
                elif d == "north" and self.player.location[0] != 0:
                    self.player.location[0] -= 1
                    self.world[i][j].visited = True
                elif d == "south" and self.player.location[0] != self.size - 1:
                    self.player.location[0] += 1
                    self.world[i][j].visited = True
                else:
                    last_cmd_msg = "There's a wall in your path"
                    continue
                last_cmd_msg = "You have moved forward"
                # /move forward

            elif cmd == "l":
                self.player.left()
            elif cmd == "r":
                self.player.right()
            # /movement controls
                pass
            else:
                last_cmd_msg = "Sorry, didn't understand that command"
            
            i, j = self.player.get_location()
            # check for updates to the board
            if self.player.location == self.wumpus.location:
                self.player.alive = False
                last_cmd_msg = "You have met with the Wumpus [RIP]"
            
            elif self.world[i][j].has_gold(): 
                self.player.has_gold = True
                last_cmd_msg = "$$$ Congratulations $$$"

            elif self.world[i][j].pit:
                self.player.alive = False
                last_cmd_msg = "Your screams become hard to hear as you descend [RIP]"
            
            elif self.world[i][j].breeze:
                self.world[i][j].visit()
                last_cmd_msg = "Is it cold in here, or is it just me?"
            elif self.world[i][j].smell:
                self.world[i][j].visit()
                last_cmd_msg = "It stinks in here!"


        self.message(last_cmd_msg, "You are facing %s %s" % (self.player.direction, self.player.location))
       
