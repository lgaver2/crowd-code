from person import Person
import numpy as np
import matplotlib.pyplot as plt
import os
class Peaple:
    def __init__(self,person,goal,m,size,tn):
        self.number=len(person)
        self.size=size
        self.goal=goal
        self.m=m
        self.tn=tn
        starts=[]
        speed=[]
        for n in person:
            starts.append(n[0])
            speed.append(n[1])
        self.crowd = [Person(starts[i],goal,speed[i],size) for i in range(self.number)] #création des personnes
        self.current_start=[starts[i] for i in range(self.number)] #points de départs de chaque personnes
        self.share_tab=np.zeros((size,size))+m #création du tableau qui servira a représenter les obstacles et les personnes communes a tous et faire que share_tab soit le labyrinthe
        for s in starts:
            self.share_tab[s[0]][s[1]]-=1

    def e(n):
        if len(str(n))>=4:
            return "1"+str(n)
        elif len(str(n))>=3:
            return "10"+str(n)
        elif len(str(n))>=2:
            return "100"+str(n)
        else:
            return "1000"+str(n)

    def crowd_move(self,e=e):
        i=0
        to_remove=[] #listes des indices ayant atteint l'objectif
        res_tab=np.zeros((self.size,self.size))

        while self.crowd!=[]:
            j=0
            for n in self.crowd:
                #try: #si il y a un chemin permettant d'accéder à l'objectif
                    if self.current_start[j]!=self.goal:
                        self.share_tab,res_tab,self.current_start[j]=n.move(self.current_start[j],self.share_tab,res_tab) #mouvement de une personne
                        
                    else:
                        to_remove.append(j)
               # except: #si non ne bouje pas
                    #print("not move"+str(j)+str(i))
                    j+=1
            if to_remove!=[]:
                k=0
                for n in to_remove:
                    self.crowd.pop(n-k) #si atteint le but enlever de la liste et aussi sont point de départ
                    self.current_start.pop(n-k)
                    k+=1
                to_remove=[]
            
            #enregistrement du tableau
            if self.crowd!=[]:
                plt.figure()
                plt.imshow(self.share_tab)
                plt.title(str(i))
                plt.colorbar()
                plt.savefig("D:\Documents\TIPE\TIPE\crowd-code\img\\"+str(e(i))+".png")

            i+=1
        
        plt.figure()
        plt.imshow(res_tab+self.m)
        plt.colorbar()
        plt.title("influence")
        plt.savefig("res"+str(self.tn)+".png")
        
            