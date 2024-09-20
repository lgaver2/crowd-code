from map_create import Map_create as mc
from peaple import Peaple
from gif_macker import Gif_macker
import os
import glob
import numpy as np
import random as rd


def create_peaple(long_s,long_g,wide_s,wide_g):
    res=[]
    for i in range(long_s,long_g):
        for j in range(wide_s,wide_g):
            res.append(((i,j),rd.randint(1,3))) #vitesse moyenne de marche 
    return res


if __name__== "__main__":

    size=18 #taille du labyrinthe
    share_tab=np.zeros((size,size)) 
    img_folder="D:\Documents\TIPE\TIPE\crowd-code\img"
    test_num=int(input("test number"))#pour différencier les tests
    
    m=mc.open_doc("maze",size) #importation du labyrinthe
    #print(m)
    goal=(0,0) 
    
    '''s=ast(size)
    s.aStar((11,11),goal,m)'''
    person=create_peaple(10,15,2,15)

    p=Peaple(person,goal,m,size,test_num) #création de la foule
    p.crowd_move() #mouvement de la foule
    Gif_macker.create(img_folder,test_num)

    #enlever les fichier images
    res=glob.glob(f"{img_folder}/*.png")
    for img in res:
        os.remove(img)


    
