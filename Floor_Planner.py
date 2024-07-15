import random

# #Pang color lang ng output
def color_text(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

# #Room object para madali ma-access information regarding sa mga rooms
class Room:
    def __init__(self, width, height, symbol, name):
        self.width = width
        self.height = height
        self.symbol = symbol
        self.name = name
        self.isAQueen = False

#Main
class FloorPlan:
    #Create floor grid
    def __init__(self, rows, columns, e_x, e_y, rooms, sort, random, logfile):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]
        self.rooms = [room for room in rooms]
        self.logfile = logfile
        
        if random:
            self.randomizeRooms()
            self.logfile.log("Rooms randomized")
        if sort == "Ascending":
            self.sortRooms(False)
            self.logfile.log("Rooms sorted, smallest to largest")
        elif sort == "Descending":
            self.sortRooms(True)
            self.logfile.log("Rooms sorted, largest to smallest")
        
        self.planFloor(e_x, e_y)
    
    #Create rooms
    def createRoom(self, width, height, symbol):
        self.rooms.append(Room(width, height, symbol))
    
    #self explanatory
    def placeEntrance(self, r, c):
        self.grid[r][c] = 'black'
        self.logfile.log(f"Entrance placed at X:{c}, Y:{r}")
    
    #self explanatory
    def sortRooms(self, reverse):
        self.rooms.sort(key=lambda room: room.height + room.width, reverse=reverse)
    
    #self explanatory
    def randomizeRooms(self):
        random.shuffle(self.rooms)
    
    #lapag room
    def placeRoom(self, row, col, room):
        for r in range(row, row + room.height):
            for c in range(col, col + room.width):
                self.grid[r][c] = Room(room.width, room.height, room.symbol, room.name)
                self.logfile.log(f"Room {room.name} cell placed at R:{r} C:{c}")
                
                center_row = row + (room.height // 2)
                center_col = col + (room.width // 2)
                
                if r == center_row and c == center_col:
                   self.grid[r][c].isAQueen = True
                   self.logfile.log(f"Room center found at R:{r} C:{c}")

    #yung isSafe() ng n-queens basically
    def canPlaceRoom(self, row, col, room): 
        for r in range(row, row + room.height):
            for c in range(col, col + room.width):
                self.logfile.log(f"Checking R:{r} C:{c} for if current room's cell will overlap with another's")
                if self.grid[r][c] != 0:
                    self.logfile.log(f"Found cell that will overlap with current room's cell at R:{r} C:{c}")
                    return False
        for ree in range(row, row + room.height):
            for cee in range(col, col + room.width):
               
                center_row = row + (room.height // 2)
                center_col = col + (room.width // 2)
              
                if ree == center_row and cee == center_col:
                # Check diagonally for existing queens
                    for r, c in zip(range(ree, -1, -1), range(cee, -1, -1)):
                        self.logfile.log(f"Checking upper-left diagonal of middle cell if there are existing queens. Currently at R:{r} C:{c}")
                        if isinstance(self.grid[r][c], Room) and self.grid[r][c].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False
                    
                    for r, c in zip(range(ree, self.rows, 1), range(cee, -1, -1)):
                        self.logfile.log(f"Checking lower-left diagonal of middle cell if there are existing queens. Currently at R:{r} C:{c}")
                        if isinstance(self.grid[r][c], Room) and self.grid[r][c].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False
                    
                    for r, c in zip(range(ree, -1, -1), range(cee, self.columns, 1)):
                        self.logfile.log(f"Checking upper-right diagonal of middle cell if there are existing queens. Currently at R:{r} C:{c}")
                        if isinstance(self.grid[r][c], Room) and self.grid[r][c].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False

                    for r, c in zip(range(ree, self.rows, 1), range(cee, self.columns, 1)):
                        self.logfile.log(f"Checking lower-right diagonal of middle cell if there are existing queens. Currently at R:{r} C:{c}")
                        if isinstance(self.grid[r][c], Room) and self.grid[r][c].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False

                    # Check if there is already a queen in the same column
                    for c in range(self.rows):
                        self.logfile.log(f"Checking column of middle cell if there are existing queens. Currently at R:{c} C:{cee}")
                        if isinstance(self.grid[c][cee], Room) and self.grid[c][cee].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False

                    # Check if there is already a queen in the same row
                    for r in range(self.columns):
                        self.logfile.log(f"Checking row of middle cell if there are existing queens. Currently at R:{ree} C:{c}")
                        if isinstance(self.grid[ree][r], Room) and self.grid[ree][r].isAQueen:
                            self.logfile.log(f"Queen found, room cannot be placed at R:{ree}, C:{cee}")
                            return False
        return True

    #placement ng mga rooms
    def solveNQueens(self, n, room_index):
        #pag nalapag na lahat ng rooms
        self.logfile.log(f"Placing room: {room_index}")
        if room_index == len(self.rooms):
            self.logfile.log(f"All rooms placed, exiting")
            return True
        
        room = self.rooms[room_index]
        
        #check each row and col if pwede ilapag yung room
        for col in range(self.columns - room.width + 1):
            for row in range(self.rows - room.height + 1):
                if self.canPlaceRoom(row, col, room):
                    self.placeRoom(row, col, room)
                    if self.solveNQueens(n, room_index + 1):
                        self.logfile.log(f"Room placed, going to next room.")
                        return True
                    #pag nacheck na lahat ng rooms tas di parin malapag yung next aalisin muna to para ilapag sa iba
                    self.logfile.log(f"Current room could not be placed, removing its cells.")
                    self.removeRoom(row, col, room)
        return False

    def removeRoom(self, row, col, room):
        for r in range(row, row + room.height):
            for c in range(col, col + room.width):
                self.logfile.log(f"Removing cells of current room. Currently at R:{r} C:{c}")
                self.grid[r][c] = 0
    
    #ito tinatawag sa labas para i-run ung app        
    def planFloor(self, r, c):
        self.placeEntrance(r - 1, c - 1)
        if not self.solveNQueens(len(self.rooms), 0):
            self.rooms = []
            self.logfile.log(f"No valid arrangement found.")
            return False
        else:
            self.logfile.log(f"All rooms placed, showing grid.")
            self.showGrid()
            return self.grid

    def showGrid(self):
        for row in self.grid:
            for cell in row:
                # print(cell.symbol if isinstance(cell, Room) else "███████", end="\t")
                print(cell.isAQueen if isinstance(cell, Room) else "███████", end="\t")
            print("\n")

# floor = FloorPlan(4, 4)
# floor.createRoom(2, 2, f'{color_text("███████", "red")}')
# floor.createRoom(2, 2, f'{color_text("███████", "green")}')
# floor.createRoom(5, 5, f'{color_text("███████", "yellow")}')
# floor.createRoom(10, 4, f'{color_text("███████", "yellow")}')
# floor.createRoom(3, 3, f'{color_text("███████", "yellow")}')
# floor.createRoom(1, 1, f'{color_text("███████", "yellow")}')
# floor.createRoom(4, 5, f'{color_text("███████", "yellow")}')
# floor.createRoom(4, 4, f'{color_text("███████", "blue")}')
# floor.createRoom(1, 1, f'{color_text("███████", "magenta")}')
# floor.createRoom(1, 1, f'{color_text("███████", "magenta")}')
# floor.createRoom(1, 1, f'{color_text("███████", "magenta")}')
# floor.createRoom(1, 1, f'{color_text("███████", "magenta")}')
# floor.createRoom(1, 1, f'{color_text("███████", "magenta")}')
# floor.createRoom(3, 3, f'{color_text("███████", "cyan")}')
# floor.createRoom(3, 3, f'{color_text("███████", "cyan")}')
# floor.createRoom(2, 4, f'{color_text("███████", "yellow")}')

# floor.planFloor(4, 1)