# Author: Daeshaun Morrison & Reema Norford, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 3/21/2023
# Instructor: Professor Silveyra
# Description: 
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
        # Populate a randoms

        # random.seed(10) # using seed?
        # self.envy = [[random.randint(0,1) for i in range(self.rows+2)] for i in range(self.cols+2)]

        self.envy = [[0,1,0,1,0,1,0,1,1,1,0,1] for i in range(self.cols+2)]
        
        for x in range(self.rows+2):
            self.envy[x][0] = -1
            self.envy[x][self.rows+1] = -1

        for y in range(self.cols+2):
            self.envy[0][y] = -1
            self.envy[self.cols+1][y] = -1

            
    def getStatus(self, posRow, posCol):
        return self.envy[posRow][posCol]

    def setStatus(self, posRow, posCol, status):
        self.envy[posRow][posCol] = status
    
    def printEnvy(self):
        for eachRow in self.envy:
            print(eachRow , "\n")

class Agent:
    def __init__(self):
        self.playGround = Environment(10,10)
        self.initalPosX = random.randint(1,10)
        self.initalPosY = random.randint(1,10)
        self.currentPosX = int(self.initalPosX)
        self.currentPosY = int(self.initalPosY)
        self.currentPos = [self.currentPosX, self.currentPosY]
        print("Rooma started at points: ",self.initalPosX, self.initalPosY)
        print("Inital Pos",self.currentPos)

    def scanEnvy(self):
            dirtyList = []
            for x in range(self.playGround.rows+1):
                for y in range(self.playGround.cols+1):
                    if (self.playGround.getStatus(x,y) == 1):
                        dirtyList.append([x,y])
            return dirtyList
                

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

    def move(self, steps):
        clean = False
        totalSteps = steps
        while (totalSteps > 0 and clean == False):
            arrived = False
            destination = self.findNearest()
            if (destination == [12,12]):
                break
            else:
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
                self.playGround.setStatus(destination[0], destination[1], 999)
        print("remaining steps left: ",totalSteps)

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
print("____")
rooma.move(7500000)
print("____")
rooma.printArea()
print("____")
print(rooma.currentPos)
