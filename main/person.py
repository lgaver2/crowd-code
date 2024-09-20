import re
from astar import Astar as ast
import numpy as np
class Person:
    def __init__(self,start,goal,speed,size):
        '''while True:
            pos=(rd.randrange(0,len(liste)),rd.randrange(0,len(liste)))
            if pos != liste[pos[0]][pos[1]]:
                self.start=pos
                break'''
        self.start=start
        self.goal=goal
        self.size=size
        self.speed=speed
        self.maze=ast(self.size)

    def move(self,s,share_tab,res_tab):
        path=self.maze.aStar(s,self.goal,share_tab)#cherche si il y a un chemin qui le conduit à la sortie sans rencontrer de personne ou de mur
        for _ in range(0,self.speed):
            
            if path!={}:
                x,y=path.popitem() #déclaration du chemin a prendre, x le point ou la personne est, y le prochain a prendre/ et enlever cette donnée
                if share_tab[y[0]][y[1]]==3:
                    res_tab[x[0]][x[1]]+=1
                    return share_tab, res_tab, x
                else:
                    share_tab[x[0]][x[1]]+=1
                    if y!=self.goal:
                        share_tab[y[0]][y[1]]-=1 #mise a jour du share_tab pour la position de la personne
                        res_tab[y[0]][y[1]]+=1
            
        return share_tab,res_tab,y #retourner le share_tab mis a jour et le prochain point de commencement
            
        #print(share_tab)
        #if share_tab[y[0]][y[1]]!=3:
        
        #else:
            #y=x
            #res_tab[x[0]][x[1]]+=1
        
           
