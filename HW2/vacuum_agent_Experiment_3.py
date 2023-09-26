# Author: Daeshaun Morrison & Reema Norford, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 3/21/2023
# Instructor: Professor Silveyra
# Description: A vacuum agent that cleans dirty spots(indexes with value = 1) in X steps given. A messy kid creates a dirty spot every 10 steps
# Errors:

import random
import math


class Environment:
    clean = 0
    dirty = 1

    def __init__(self, rows, cols):
        #iterate through envy and populate randomly
        self.rows = 10
        self.cols = 10
        # Populate a random environment of size (`rows` x `cols`)
        self.envy = [[0,1,0,1,0,1,0,1,1,1,0,1] for i in range(self.cols+2)]
        # Create and give the most outer "walls" the value of 9 to signify that it's the environment's walls that the AI can not cross
        for x in range(self.rows+2):
            self.envy[x][0] = 9
            self.envy[x][self.rows+1] = 9

        for y in range(self.cols+2):
            self.envy[0][y] = 9
            self.envy[self.cols+1][y] = 9
        
    def getStatus(self, posRow, posCol):
        return self.envy[posRow][posCol]

    def setStatus(self, posRow, posCol, status):
        self.envy[posRow][posCol] = status
    
    def printEnvy(self):
        for eachRow in self.envy:
            print(eachRow , "\n")

    def messy_Kid(self):
        self.setStatus(random.randint(1,10), random.randint(1,10), 1)


class Agent:
    def __init__(self):
        self.playGround = Environment(10,10)
        # randomly generate a starting position for the agent in the `environment`
        self.initalPosX = random.randint(1,10)
        self.initalPosY = random.randint(1,10)
        self.currentPosX = int(self.initalPosX)
        self.currentPosY = int(self.initalPosY)
        self.currentPos = [self.currentPosX, self.currentPosY]

    # Return a list of all dirty spots; indexes where value = 1
    def scanEnvy(self):
            dirtyList = []
            for x in range(self.playGround.rows+1):
                for y in range(self.playGround.cols+1):
                    if (self.playGround.getStatus(x,y) == 1):
                        dirtyList.append([x,y])
            return dirtyList
    # return a single list of the row and column of the closest dirty spot to the current position of the agent
    def findNearest(self):
            dList = self.scanEnvy()
            near = 12
            nearPoint = [12,12]
            for item in range(len(dList)):
                dl = dList[item]
                check = math.sqrt(((dl[0]-self.currentPos[0])**2)+((dl[1]-self.currentPos[1])**2))
                if (check < near):
                    near = check
                    nearPoint = dList[item]
            return nearPoint
    # Loops until the given `steps` = 0
    def move(self, steps):
        clean = False
        totalSteps = steps
        # Keep running until all dirty spots are clean and steps have not run out.
        while (totalSteps > 0 and clean == False):
            arrived = False
            destination = self.findNearest()
            # If there are not dirty spaces, end loop
            if (destination == [12,12]):
                break
            else:
                # Move one step at a time and clean each spot  
                while arrived == False and totalSteps > 0:
                    while self.currentPosX > destination[0] and totalSteps > 0:
                        totalSteps -= 1
                        self.currentPosX -= 1
                    while self.currentPosX < destination[0] and totalSteps > 0:
                        totalSteps -= 1
                        self.currentPosX += 1
                    while self.currentPosY > destination[1] and totalSteps > 0:
                        totalSteps -= 1
                        self.currentPosY -= 1
                    while self.currentPosY < destination[1] and totalSteps > 0:
                        totalSteps -= 1
                        self.currentPosY += 1
                    arrived = True
                self.playGround.setStatus(destination[0], destination[1], 0)
            #  An agent(simulating a messy child) makes one index dirty every 10 steps
            if totalSteps % 10 == 0:
                self.playGround.messy_Kid()

    def otherMove(self,steps):
        totalSteps = steps
        while (totalSteps > 0):
            # Place agent in random space
            self.currentPosX = random.randint(1,10)
            self.currentPosY = random.randint(1,10)
            self.currentPos = [self.currentPosX, self.currentPosY]
            totalSteps -= 1
            destination = self.currentPos
            self.playGround.setStatus(destination[0], destination[1], 0)
            if totalSteps % 10 == 0:
                self.playGround.messy_Kid()


    def printArea(self):
        self.playGround.printEnvy()
    
print("____")

dirtySpaceLeft = 0
avgDirtySpaceLeft = 0

for x in range(100):
    rooma = Agent()
    rooma.move(125)
    scoreList = rooma.scanEnvy()
    dirtySpaceLeft += len(scoreList)

avgDirtySpaceLeft = dirtySpaceLeft / 100

rooma.printArea()
print("Average dirty space left. The experiment ran 100 times: ", avgDirtySpaceLeft)
# --------------------------------------
dirtySpaceLeftRan = 0
avgDirtySpaceLeftRan = 0

for x in range(100):
    roomaRan = Agent()
    roomaRan.otherMove(125)
    scoreListRan = roomaRan.scanEnvy()
    dirtySpaceLeftRan += len(scoreListRan)

avgDirtySpaceLeftRan = dirtySpaceLeftRan / 100
print("Environment after the rooma cleaned some spot on the 100th run:")
roomaRan.printArea()
print("Average dirty space left when rooma is randomly placed. The experiment ran 100 times: ", avgDirtySpaceLeftRan)