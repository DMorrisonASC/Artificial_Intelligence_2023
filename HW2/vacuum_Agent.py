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
        self.envy = [[random.randint(0,1) for i in range(self.rows+2)] for i in range(self.cols+2)]
        
        for x in range(self.rows+2):
            self.envy[x][0] = 2
            self.envy[x][self.rows+1] = 2

        for y in range(self.cols+2):
            self.envy[0][y] = 2
            self.envy[self.cols+1][y] = 2

            
    def getStatus(self, posRow, posCol):
        return self.envy[posRow][posCol]

    def setStatus(self, posRow, posCol, status):
        self.envy[posRow][posCol] = status
        print("New State is at Coors:",self.envy[posRow][posCol])
    
    def printEnvy(self):
        for eachRow in self.envy:
            print(eachRow , "\n")

class Agent:
    def __init__(self):
        self.playGround = Environment(10,10)
        self.initalPosX = random.randint(0,10)
        self.initalPosY = random.randint(0,10)
        self.currentPosX = int(self.initalPosX)
        self.currentPosY = int(self.initalPosY)
        self.currentPos = [self.currentPosX, self.currentPosY]
        print("Rooma started at points: ",self.initalPosX, self.initalPosY)
        # playGround.printEnvy()

    def scanEnvy(self):
            dirtyList = []
            for x in range(self.playGround.rows):
                for y in range(self.playGround.cols):
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
        arrived = False
        totalSteps = steps
        destination = self.findNearest()

        while arrived == False:
            while self.currentPosX > destination[0]:
                totalSteps -= 1
                self.currentPosX -= 1
            while self.currentPosX < destination[0]:
                totalSteps -= 1
                self.currentPosX += 1
            while self.currentPosY > destination[1]:
                totalSteps -= 1
                self.currentPosY -= 1
            while self.currentPosY < destination[1]:
                totalSteps -= 1
                self.currentPosY += 1

            arrived = True
            
        # self.playGround.getStatus(destination[0], destination[1])
        self.playGround.setStatus(destination[0], destination[1], 999)
        self.playGround.getStatus(destination[0], destination[1]) 
        print("remaining steps taken:",totalSteps)

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
rooma.move(75)
print("____")
rooma.printArea()
print("____")
print(rooma.currentPos)
