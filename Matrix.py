import copy
import numpy as np
class Matrix:

    def __init__(self,entries):

        self.entries = copy.deepcopy(entries)
        self.rows = len(self.entries)
        self.cols = len(self.entries[0])


    def setEntry(self,i,j,value):
        self.entries[i][j] = value
    def getEntry(self,i,j):
        return self.entries[i][j]
    def __str__(self):
        res = str()
        for i in range(0,self.rows):
            res = res + str(self.entries[i]) + "\n"
        return res
    def __add__(self,other):
        resList = list(list())

        if(other.rows == self.rows and other.cols == self.cols):
            for i in range(0, self.rows):
                resList.append([0 for j in range(0, self.cols)])

            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    resList[i][j] = self.entries[i][j] + other.getEntry(i,j)
        return Matrix(resList)
    def __sub__(self,other):
        resList = list(list())

        if(other.rows == self.rows and other.cols == self.cols):
            for i in range(0, self.rows):
                resList.append([0 for j in range(0, self.cols)])

            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    resList[i][j] = self.entries[i][j] - other.getEntry(i,j)
        return Matrix(resList)

    def __mul__(self,other):
        if(other.rows == self.cols):
            resList = list(list())
            for i in range(0, self.rows):
                resList.append([0 for j in range(0, other.cols)])
            for i in range(0,self.rows):
                for j in range(0,other.cols):
                    for k in range(0,self.cols):
                        resList[i][j] = resList[i][j] + self.getEntry(i,k)*other.getEntry(k,j)
            return Matrix(resList)
        else:
            print("Matricies are of invalid dimensions")

