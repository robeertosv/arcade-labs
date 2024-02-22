import random
class Room:
    def __init__(self, description="",north=0, south=0, east=0, west = 0):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        n = random.randint(0,2)
        # Ternary comparator to create prize
        self._tienePremio = (True if n == 0 else False)
    @property
    def tienePremio(self):
        return self._tienePremio
    @tienePremio.setter
    def tienePremio(self,value):
        self._tienePremio = False
def main():
    roomList = []
    room = Room(description = "This is the Second Bedroom", north = None, south = None, east =None, west=1)
    roomList.append(room)
    room = Room(description = "This is the South Hall", north = 4, south = None, east =0, west=2)
    roomList.append(room)
    room = Room(description = "This is the Dining Room", north = None, south = None, east =1, west=None)
    roomList.append(room)
    room = Room(description = "This is the First Bedroom", north = None, south = None, east =None, west=4)
    roomList.append(room)
    room = Room(description = "This is the North Hall", north =6, south=1, east=3, west=5)
    roomList.append(room)
    room = Room(description = "This is the Kitchen", north=None, south=None, east=4, west=None)
    roomList.append(room)
    room = Room(description = "This is the Balcony", north=None, south=4, east=None, west=None)
    roomList.append(room)

    currentRoom = random.randint(0,6)
    done = False
    print("Find the Balcony")
    print()

    while not done:
        print(f"{roomList[currentRoom].description}, where do you want to go?")
        choice = input()
        roomList[currentRoom].tienePremio = False


        if(choice == 'w'):
            if(roomList[currentRoom].north != None):
                currentRoom = roomList[currentRoom].north
            else:
                print("There's no room in the north")
        elif choice == 's':
            if(roomList[currentRoom].south != None):
                currentRoom = roomList[currentRoom].south
            else:
                print("There's no room in the south")
        elif choice == 'a':
            if(roomList[currentRoom].east != None):
                currentRoom = roomList[currentRoom].east
            else:
                print("There's no room in the east")
        elif choice == 'd':
            if(roomList[currentRoom].west != None):
                currentRoom = roomList[currentRoom].west
            else:
                print("There's no room in the west")
        else:
            print("Invalid")


        if currentRoom == 6:
            flag = False
            for r in roomList:
                if r.tienePremio:
                    flag = False
                    break
                else:
                    flag = True

            if flag:
                done = True
            else:
                print("Tienes que encontrar todos los premios primero")


    print("Congrats!! You won!!!")

if __name__ == '__main__':
    main()