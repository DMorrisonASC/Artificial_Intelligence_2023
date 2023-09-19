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
    def __init__(self):
        #iterate through envy and populate randomly
        self.envy = [[random.randint(0,1) for i in range(10)] for i in range(10)]

    def getStatus(self, posRow, posCol):
        print(self.envy[posRow][posCol])

    def setStatus(self, posRow, posCol, status):
        self.envy[posRow][posCol] = status
        print(self.envy[posRow][posCol])
    
    def printEnvy(self):
        for eachRow in self.envy:
            print(eachRow , "\n")

x = Environment()
x.printEnvy()

class Agent:
    def __init__(self):
        playGround = Environment()
        initalPos = [random.randint(0,10)][random.randint(0,10)]
        currentPos = [initalPos[0]][initalPos[1]]

    def move(self, steps):
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
