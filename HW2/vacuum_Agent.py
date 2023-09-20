# Author: Daeshaun Morrison & Reema Norford, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 3/21/2023
# Instructor: Professor Silveyra
# Description: 
# Errors:

import random
#vacuum agent


class Agent:
    pass
    # x=0
    # y=0
    # envy1 = Environment
    # clean()


    ##move Left Right Up Down
    ##clean, or do nothing
    ##perceive location or status of location

class Environment:
    clean = 0
    dirty = 1
    def __init__(self, rows, cols):
        #iterate through envy and populate randomly
        self.rows = 10
        self.cols = 10
        self.envy = [[random.randint(0,1) for i in range(self.rows+2)] for i in range(self.cols+2)]
        
        for x in range(self.rows+2):
            self.envy[x][0] = 2
            self.envy[x][self.rows+1] = 2

        for y in range(self.cols+2):
            self.envy[0][y] = 2
            self.envy[self.cols+1][y] = 2

            
    def getStatus(self, posRow, posCol):
        print(self.envy[posRow][posCol])

    def setStatus(self, posRow, posCol, status):
        self.envy[posRow][posCol] = status
        print(self.envy[posRow][posCol])

    def getDirtySpot(self):
        pass

    
    def printEnvy(self):
        for eachRow in self.envy:
            print(eachRow , "\n")


# x = Environment(10,10)
# x.getStatus(0,3)
# x.printEnvy()

class Agent:
    def __init__(self):
        self.playGround = Environment(10,10)
        self.initalPosX = random.randint(0,10)
        self.initalPosY = random.randint(0,10)
        self.currentPosX = int(self.initalPosX)
        self.currentPosY = int(self.initalPosY)
        # playGround.printEnvy()

    def move(self, steps, destination, currentPosX, currentPosY):
        arrived = False

        while arrived == False:
            for x in destination[0]:
                if currentPosX > destination[0]:
                    steps -= 1
                    currentPosX -= 1
                elif currentPosX < destination[0]:
                    pass

            
        

    def goLeft(self):
        if currentPos[0] > 0:
            currentPos[0] -= 1

    def goRight(self): 
        if currentPos[0] < 10:
            currentPos[0] += 1

    def goUp(self): 
        if currentPos[1] > 0:
            currentPos[0] -= 1
    def goDown(self): 
        if currentPos[1] < 10:
            currentPos[0] += 1

    def printArea(self):
        self.playGround.printEnvy()
    
rooma = Agent()
rooma.printArea()

# x.getStatus(0,0)
    #populateEnvy()
    #updateEnvy(x,y,u)
    
    ##10 x 10 grid
    ##boundaries cannot be passed
    ##locations can have status clean or dirty, randomly assigned

#simple reflex agent
    #considers location and current status of location to determine what to do

#agent
	#-x:int
	#-y:int
	#-active:boolean
	#-cost:int
	#-battery		how many steps can I move, how many left, charge
	#-envy1:envy		maybe
	#+move
	#+setActive()
	#+clean()
	#+getCost()
	#+getActive()
	#+stop()
	#+moveALot()
	#+checkEnvironment()
	#+stuck()
	#+allClean()	only agent knows		simple* - knows it’s done

#Environment
	#-envy:list[][]
	#-agent1: agent		maybe
	#+populateEnvy()
	#+updateEnvy(x,y,u)


