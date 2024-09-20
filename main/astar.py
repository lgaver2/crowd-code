
from queue import PriorityQueue
import re
from sys import api_version

class Astar:
    def __init__(self,size):
        self.size=size
        res=[]
        for i in range(0,self.size):
            for j in range(0,self.size):
                res.append((i,j))
        self.tup=res


    def h(cell1,cell2): #manathan distance
        x1,y1=cell1
        x2,y2=cell2
        return abs(x1-x2)+abs(y1-y2)

    def aStar(self,start,goal,m,h=h):
        size=len(m)
        g_score={cell:float('inf') for cell in self.tup}
        g_score[start]=0
        f_score={cell:float('inf') for cell in self.tup}
        f_score[start]=h(start,goal) #distance entre start et goal

        open=PriorityQueue()
        open.put((h(start,goal),h(start,goal),start))
        aPath={}#solution
        while not open.empty():
            currCell=open.get()[2] #cost du carreau
            if currCell==goal:
                break
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                if currCell[0]+d[0]<size and currCell[1]+d[1]<size and currCell[0]+d[0]>-1 and currCell[1]+d[1]>-1:
                    if m[currCell[0]+d[0]][currCell[1]+d[1]]>2:
                        if d==(0,1):
                            childCell=(currCell[0],currCell[1]+1)
                        elif d==(1,0):
                            childCell=(currCell[0]+1,currCell[1])
                        elif d==(-1,0):
                            childCell=(currCell[0]-1,currCell[1])
                        elif d==(0,-1):
                            childCell=(currCell[0],currCell[1]-1)

                        temp_g_score=g_score[currCell]+1
                        temp_f_score=temp_g_score+h(childCell,goal)#calcule des scores temporaire

                        if temp_f_score < f_score[childCell]:#mise a jour des données
                            g_score[childCell]=temp_g_score
                            f_score[childCell]=temp_f_score
                            open.put((temp_f_score,h(childCell,goal),childCell))
                            aPath[childCell]=currCell#mise a jour du chemin
        fwdPath={}#reconstitution de solution (inverser la liste des tuples)
        cell=goal
        try:
            while cell!=start:
                fwdPath[aPath[cell]]=cell
                cell=aPath[cell]
        except: #si il existe des parsonnes devant
            first_item = list(aPath.items())[0]
            fwdPath[first_item[1]]=first_item[0]
        return fwdPath

    def print_labyrinth(self): #fonction pour imprimer le labyrinthe
        for i in range(0,self.l):
            for j in range(0,self.l):
                if self.m[i][j]:
                    print("O",end="")
                else:
                    print("X",end="")
            print("")



    
